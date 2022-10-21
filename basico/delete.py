#!/usr/bin/env python

import sqlite3
from config import *

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("DELETE FROM clientes WHERE id = ?", (1,))
connection.close()