#!/usr/bin/env python

import sqlite3
from config import *

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("UPDATE OR IGNORE usuarios SET email = ?, idade = ? WHERE id = ?", ("joao@example.com.br", 39, 2))
connection.commit()
connection.close()