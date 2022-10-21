#!/usr/bin/env python

import sqlite3
from config import *

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute("DELETE FROM usuarios;")
# https://stackoverflow.com/a/17359141/1844007
# cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name='usuarios';")

connection.commit()
connection.close()