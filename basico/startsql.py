#!/usr/bin/env python

import os
import sqlite3
from config import *

if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
else:
    print(f"O arquivo {DB_FILE} não existe.")

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, email TEXT UNIQUE, idade INTEGER);")
connection.close()