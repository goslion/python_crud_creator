# python_crud_creator
#### python pymysql crud function creator!

### 简介

#### 不想写重复增删改查，于是有了这个玩意

#### 一个python pymysql的crud(增删改查)生成器



### 有如下功能：

1.  根据指定的数据库，生成数据库中所有表的增删改查方法，生成py文件可以直接使用
2.  可以控制生成增删改查中的哪些方法，比如只要增加，注释掉其余的方法即可
3.  只支持单个字段的查询，修改，删除
4.  查询出的结果为字典对象，可以直接使用

### 有待优化：

1. 更加细粒度的过程控制，精确到字段及函数
2. 多字段的复杂查询，修改，删除
3. 复杂的SQL语句封装
4. 优化代码结构，函数式编程

### 以下是英文机翻:

Here is the English Translation:

### BriefIntroduction

#### I don't want to write duplicate additions, deletions, changes and queries, so I have this thing

#### A crud generator of Python pymysql

### It has the following functions:

1.  According to the specified database, the method of adding, deleting, modifying and querying all tables in the database is generated. The PY file can be used directly
2.  You can control which methods are used to generate add, delete, modify, and query. For example, you only need to add and comment out the remaining methods
3.  Only single field query, modification and deletion are supported
4. The result is a dictionary object, which can be used directly

### To be optimized:

1. More fine-grained process control, accurate to fields and functions
2. Multi field complex query, modify, delete
3. Complex SQL statement encapsulation
4. Optimize the code structure, functional programming






