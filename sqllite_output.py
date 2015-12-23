# -*- coding: utf-8 -*-
#__author__ = 'dev'

import sqlite3
names= ['Panel.sqlite']
conn = sqlite3.connect('Panel.sqlite')
res = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
table_names = []
for row in res:
    table_names.append(row)
    print(row)
