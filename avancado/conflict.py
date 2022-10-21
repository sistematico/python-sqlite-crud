#!/usr/bin/env python

import sqlite3
from config import *

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute("""
  INSERT INTO usuarios(nome, email, idade)
  values (:nome, :email, :idade) 
  ON CONFLICT(email) 
  DO UPDATE SET idade = idade + 1;
  """, 
  {"nome": "Lucas", "email": "sistematico@gmail.com", "idade": 39}
)

connection.commit()
connection.close()