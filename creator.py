import sys
import os
import pymysql

indentwidth = 4


class IndentedCodeWriter(object):

    def __init__(self, output):
        self.level = 0
        self.output = output

    def indent(self):
        self.level += 1

    def dedent(self):
        self.level -= 1

    def write(self, line):
        if line.strip():
            if indentwidth > 0:
                indent = " " * indentwidth
                line = line.replace("\t", indent)
            else:
                indent = "\t"
            self.output.write("%s%s\n" % (indent * self.level, line))
        else:
            self.output.write("\n")

    def skip(self):
        self.level = 0
        self.output.write("\r\r")


def createCodeIndenter(output):
    return IndentedCodeWriter(output)


def get_connection(host, port, username, password, database):
    return pymysql.connect(host=host, user=username, port=port, password=password, database=database,
                           cursorclass=pymysql.cursors.DictCursor)


def generate(host, port, username, password, database):
    output = database + "_operator.py"
    connect = get_connection(host=host, port=port, username=username, password=password, database=database)
    server_info = connect.get_server_info()
    host_info = connect.get_host_info()
    print("server address:", host_info.split(" ")[-1])
    print("server info:", server_info)
    tables = query_tables(connect=connect)
    print("tables:", tables)
    open_pyfile(output=output)
    generate_connection_function(host=host, port=port, username=username, password=password,
                                 database=database)
    generate_tables_function(tables=tables, connect=connect)
    close_pyfile()
    print("output:", output)


def generate_tables_function(tables, connect):
    for tb in tables:
        structure = query_table_structure(connect=connect, table=tb)
        generate_insert_function(table=tb, sequence=structure)
        generate_delete_function(table=tb, sequence=structure)
        generate_update_function(table=tb, sequence=structure)
        generating_query_function(table=tb, sequence=structure)
        print("structure: ", structure)


def query_tables(connect):
    sql = "show tables"
    cur = connect.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    tables = []
    for table in res:
        tables.append(list(table.values())[0])
    return tables


def query_table_structure(connect, table):
    cur = connect.cursor()
    sql = "desc " + table
    cur.execute(sql)
    description = cur.fetchall()
    field_sequence = []
    for field in description:
        field_sequence.append(field['Field'])
    return field_sequence


def open_pyfile(output):
    global _pyfile
    if sys.hexversion >= 0x03000000:
        if not os.path.exists(output):
            _pyfile = open(output, 'wt', encoding='utf8')
        else:
            _pyfile = open(output, 'a+', encoding='utf8')
    else:
        if not os.path.exists(output):
            _pyfile = open(output, 'wt')
        else:
            _pyfile = open(output, 'a+', encoding='utf8')


def close_pyfile():
    _pyfile.close()


def write_con_cur(indenter):
    indenter.indent()
    indenter.write("connect = get_connection()")
    indenter.write("cur = connect.cursor()")


def write_exe_com(indenter):
    indenter.write("cur.execute(sql)")
    indenter.write("connect.commit()")


def generate_insert_function(table, sequence):
    indenter = createCodeIndenter(output=_pyfile)
    field_string = ",".join(sequence)
    value_string = ",".join(["'{" + f + "}'" for f in sequence])
    sql = f"sql = f\"insert into {table} ({field_string}) values({value_string});\""
    function_string = f"def insert_{table}({field_string}):"
    print("create:", function_string)
    indenter.write(function_string)
    write_con_cur(indenter=indenter)
    indenter.write(sql)
    write_exe_com(indenter=indenter)
    indenter.skip()


def generate_delete_function(table, sequence):
    indenter = createCodeIndenter(output=_pyfile)
    for field in sequence:
        generate_delete_function_by_field(field=field, indenter=indenter, table=table)


def generate_delete_function_by_field(field, indenter, table):
    indenter.level = 0
    fd = "'{" + field + "}'"
    sql = f"sql = f\"delete from {table} where {field}={fd};\""
    function_string = f"def delete_{table}_by_{field}({field}):"
    print("create:", function_string)
    indenter.write(function_string)
    write_con_cur(indenter=indenter)
    indenter.write(sql)
    write_exe_com(indenter=indenter)
    indenter.skip()


def generate_update_function(table, sequence):
    indenter = createCodeIndenter(output=_pyfile)
    for field in sequence:
        generate_update_function_by_field(field=field, sequence=sequence, indenter=indenter, table=table)


def generate_update_function_by_field(field, sequence, indenter, table):
    indenter.level = 0
    key = field
    copy_fields = sequence.copy()
    copy_fields.remove(key)
    parameter_string = ",".join(sequence)
    set_string = ",".join([cf + "=" + "'{" + cf + "}'" for cf in copy_fields])
    where_string = "'{" + key + "}'"
    sql = f"sql = f\"update {table} set {set_string} where {key}={where_string};\""
    function_string = f"def update_{table}_by_{key}({parameter_string}):"
    print("create:", function_string)
    indenter.write(function_string)
    write_con_cur(indenter=indenter)
    indenter.write(sql)
    write_exe_com(indenter=indenter)
    indenter.skip()


def generating_query_function(table, sequence):
    indenter = createCodeIndenter(output=_pyfile)
    for field in sequence:
        generate_query_function_by_field(indenter=indenter, field=field, sequence=sequence, table=table)


def generate_query_function_by_field(indenter, field, sequence, table):
    indenter.level = 0
    key = field
    select_string = ",".join(sequence)
    function_string = f"def query_{table}_by_{key}({key}):"
    where_string = "'{" + key + "}'"
    sql = f"sql = f\"select {select_string} from {table} where {key}={where_string};\""
    print("create:", function_string)
    indenter.write(function_string)
    write_con_cur(indenter=indenter)
    indenter.write(sql)
    indenter.write("cur.execute(sql)")
    indenter.write("res = cur.fetchall()")
    indenter.write("result_set = []")
    indenter.write("for r in res:")
    indenter.indent()
    indenter.write("result_set.append(r)")
    indenter.dedent()
    indenter.write("return result_set")
    indenter.skip()


def generate_connection_function(host, port, username, password, database):
    indenter = createCodeIndenter(output=_pyfile)
    indenter.write("import pymysql")
    indenter.skip()
    indenter.write(
        f"def get_connection(host='{host}', port={port}, username='{username}', password='{password}', database='{database}'):")
    indenter.indent()
    indenter.write(
        "return pymysql.connect(host=host,user=username,port=port,password=password,database=database,cursorclass=pymysql.cursors.DictCursor)")
    indenter.skip()


if __name__ == '__main__':
    generate(host='127.0.0.1', port=3306, username='root', password='123456', database='robot')
