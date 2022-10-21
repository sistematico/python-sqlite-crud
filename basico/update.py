#!/usr/bin/env python

import sqlite3
from config import *

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("UPDATE usuarios SET fone = ?, criado_em = ? WHERE id = ?", (novo_fone, novo_criado_em, id_cliente))
row = cursor.fetchone()
connection.close()

if row:
    print(row[0])
else:
    print('Error getting data from database.')