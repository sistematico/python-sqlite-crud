#!/usr/bin/env python

import sqlite3
from config import *

data = [
  ('Lucas Brum', 'lucas@example.com', 18),
  ('João da Silva', 'joao@example.net', 22),
  ('Ana Maria', 'ana@example.org', 27)
]

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.executemany("INSERT OR IGNORE INTO usuarios (nome, email, idade) VALUES (?, ?, ?)", data)
connection.commit()
connection.close()