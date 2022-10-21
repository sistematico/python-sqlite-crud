#!/usr/bin/env python

import sqlite3
from config import *

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("SELECT * FROM usuarios")
rows = cursor.fetchall()
for row in rows:
  print(row)
connection.close()






