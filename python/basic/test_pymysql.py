#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 11:55
# @Author  : Cxibo
# @File    : test_pymysql.py
# @Software: PyCharm
import pymysql


def connect_sakila_db():
    config = {'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': '123456',
              'database': 'sakila'}
    # return pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
    #                        database='sakila')
    return pymysql.connect(**config)


def connect_baidubaike_db():
    config = {'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': '123456',
              'database': 'baidubaike'}
    # return pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
    #                        database='sakila')
    return pymysql.connect(**config)


def query_actor_(n):
    # sql_str = ("SELECT COUNT(*) FROM actor")
    sql_str = ("SELECT * FROM actor")
    conn = connect_sakila_db()
    cur = conn.cursor()
    cur.execute(sql_str)
    rows = cur.fetchall()
    print(cur.description)
    print(cur.rowcount)
    for row in rows:
        print(row)
    cur.close()
    conn.close()


def test():
    # query_actor_(1)
    print(connect_baidubaike_db().cursor())
    pass


if __name__ == "__main__":
    test()
