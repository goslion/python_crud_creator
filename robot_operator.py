import pymysql

    return pymysql.connect(host=host,user=username,port=port,password=password,database=database,cursorclass=pymysql.cursors.DictCursor)

    connect = get_connection()
    cur = connect.cursor()
    sql = f"insert into qa (id,question,answer) values('{id}','{question}','{answer}');"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"delete from qa where id='{id}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"delete from qa where question='{question}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"delete from qa where answer='{answer}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"update qa set question='{question}',answer='{answer}' where id='{id}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"update qa set id='{id}',answer='{answer}' where question='{question}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"update qa set id='{id}',question='{question}' where answer='{answer}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"select id,question,answer from qa where id='{id}';"
    cur.execute(sql)
    res = cur.fetchall()
    result_set = []
    for r in res:
        result_set.append(r)
    return result_set

    connect = get_connection()
    cur = connect.cursor()
    sql = f"select id,question,answer from qa where question='{question}';"
    cur.execute(sql)
    res = cur.fetchall()
    result_set = []
    for r in res:
        result_set.append(r)
    return result_set

    connect = get_connection()
    cur = connect.cursor()
    sql = f"select id,question,answer from qa where answer='{answer}';"
    cur.execute(sql)
    res = cur.fetchall()
    result_set = []
    for r in res:
        result_set.append(r)
    return result_set

    connect = get_connection()
    cur = connect.cursor()
    sql = f"insert into questions (id,question) values('{id}','{question}');"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"delete from questions where id='{id}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"delete from questions where question='{question}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"update questions set question='{question}' where id='{id}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"update questions set id='{id}' where question='{question}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"select id,question from questions where id='{id}';"
    cur.execute(sql)
    res = cur.fetchall()
    result_set = []
    for r in res:
        result_set.append(r)
    return result_set

    connect = get_connection()
    cur = connect.cursor()
    sql = f"select id,question from questions where question='{question}';"
    cur.execute(sql)
    res = cur.fetchall()
    result_set = []
    for r in res:
        result_set.append(r)
    return result_set

    connect = get_connection()
    cur = connect.cursor()
    sql = f"insert into stopwords (id,word) values('{id}','{word}');"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"delete from stopwords where id='{id}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"delete from stopwords where word='{word}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"update stopwords set word='{word}' where id='{id}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"update stopwords set id='{id}' where word='{word}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"select id,word from stopwords where id='{id}';"
    cur.execute(sql)
    res = cur.fetchall()
    result_set = []
    for r in res:
        result_set.append(r)
    return result_set

    connect = get_connection()
    cur = connect.cursor()
    sql = f"select id,word from stopwords where word='{word}';"
    cur.execute(sql)
    res = cur.fetchall()
    result_set = []
    for r in res:
        result_set.append(r)
    return result_set

    connect = get_connection()
    cur = connect.cursor()
    sql = f"insert into synonyms (id,words) values('{id}','{words}');"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"delete from synonyms where id='{id}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"delete from synonyms where words='{words}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"update synonyms set words='{words}' where id='{id}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"update synonyms set id='{id}' where words='{words}';"
    cur.execute(sql)
    connect.commit()

    connect = get_connection()
    cur = connect.cursor()
    sql = f"select id,words from synonyms where id='{id}';"
    cur.execute(sql)
    res = cur.fetchall()
    result_set = []
    for r in res:
        result_set.append(r)
    return result_set

    connect = get_connection()
    cur = connect.cursor()
    sql = f"select id,words from synonyms where words='{words}';"
    cur.execute(sql)
    res = cur.fetchall()
    result_set = []
    for r in res:
        result_set.append(r)
    return result_set
