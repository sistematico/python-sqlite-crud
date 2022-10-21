#!/usr/bin/env python

import sqlite3
from config import *

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("SELECT * FROM usuarios WHERE user_id = :user_id", { "user_id": int(user.id) })
row = cursor.fetchone()
connection.close()

if row:
    print(row[0])
else:
    print('Error getting data from database.')