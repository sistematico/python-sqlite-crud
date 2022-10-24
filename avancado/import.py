#!/usr/bin/env python

import sqlite3
from config import *

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

with open(SQL_FILE, 'r') as sqlfile:
  connection.executescript(sqlfile.read())
  connection.commit()

connection.close()