# -*- coding: utf-8 -*-
#__author__ = 'dev'

import sqlite3
import pprint
import json

names = ['Panel.sqlite', 'config.sqlite']


def get_table_name(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    res = cursor.fetchall()
    table_names = []
    for row in res:
        table_names.append(row[0])
        # print(row)
    return table_names


def get_columns(cursor, table_name):
    cmd = u"PRAGMA table_info({})".format(table_name)
    # print(us)
    # conn.execute(us)
    # cur = conn.cursor()
    cursor.execute(cmd)
    columns = cursor.fetchall()
    column_names = [None for i in range(len(columns))]
    for item in columns:
        column_names[item[0]] = item[1]
    # print(column_names)
    return column_names


def get_all_field(cursor, table):
    cmd = u"select * from {}".format(table)
    cursor.execute(cmd)
    rows = cursor.fetchall()
    # column_names = [None for i in range(len(columns))]
    # for row in rows:
    #     print(row)
    return rows

for name in names:
    print("db:%s"%(name))
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    table_names = get_table_name(cursor)
    for table in table_names:
        table_dict = {"1_tb_name": table}
        content_rows = []
        columns = get_columns(cursor, table)
        rows = get_all_field(cursor, table)
        for row in rows:
            content_dict = {}
            for i, column in enumerate(columns):
                content_dict[column] = row[i]
            content_rows.append(content_dict)
        table_dict['2_content'] = content_rows
        # print("table:%s"%(table))
        # pprint.pprint(table_dict)
        print(json.dumps(table_dict,sort_keys=True,
              indent=4, separators=(',', ': ')))