#!/usr/bin/env python

import sqlite3
from config import *

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("SELECT * FROM usuarios WHERE rowid = ?;", (1,))
row = cursor.fetchone()
connection.close()

if row:
    print(row)
else:
    print('Error getting data from database.')