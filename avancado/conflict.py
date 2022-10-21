#!/usr/bin/env python

import os
import sqlite3

db_file = r'database.db'

connection = sqlite3.connect(db_file)
cursor = connection.cursor()
cursor.execute("""
  INSERT INTO usuarios(nome, email, idade)
  values (:nome, :email, :idade) ON CONFLICT(email) 
  DO UPDATE SET idade = idade + 1;
""", {"nome": "Lucas", "email": "sistematico@gmail.com", "idade": 39})
connection.commit()
connection.close()