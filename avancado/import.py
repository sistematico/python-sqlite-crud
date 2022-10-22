#!/usr/bin/env python

import sqlite3
from config import *

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

with open(SQL_FILE, 'r') as sql_file:
  connection.executescript(sql_file.read())

connection.commit()
connection.close()