#!/usr/bin/env python

import os
import sqlite3

db_file = r'database.db'

if os.path.exists(db_file):
    os.remove(db_file)
else:
    print(f"O arquivo {db_file} não existe.")

connection = sqlite3.connect(db_file)
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id integer PRIMARY KEY, nome text, email text UNIQUE, idade integer)")
connection.close()