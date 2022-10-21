#!/usr/bin/env python

import sqlite3
from config import *

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("INSERT OR IGNORE INTO usuarios (nome, email, idade) VALUES (?, ?, ?)", ("Lucas", "lucas@example.com", 39))
connection.commit()
connection.close()