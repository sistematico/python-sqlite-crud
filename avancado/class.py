#!/usr/bin/env python

import sqlite3
from config import *

class Database:
    def __init__(self):
        try:
            self.connection = sqlite3.connect(DB_FILE)
            self.cursor = self.connection.cursor()

        except sqlite3.Error as e:
            print("Error connecting to database!")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
    
    def close(self):        
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            self.connection = None


    def execute(self, table, query, data, where = None, update = None):
        sql = self.build_query(table, query, data, where, update)
        self.cursor.execute(sql, data)

    def executemany(self, payload, params):
        self.cursor.executemany(payload, params)

    def fetchone(self, query):
        self.cursor.execute(query)        
        row = self.cursor.fetchone()        
        return row[0] if row else 'Nenhum resultado.'

    def fetchmany(self, query):
        self.cursor.execute(query)        
        rows = self.cursor.fetchall()        
        return rows[0] if rows else 'Nenhum resultado.'

    def create_table(self):
        if self.connection:
            with open(SQL_FILE, 'r') as sql_file:
                self.connection.executescript(sql_file.read())

    def build_query(self, table, query, data, where = None, update = None):
        placeholder = ''
        fields = ''

        for key in data:
            placeholder = f'{placeholder} :{key}'
            fields = f'{fields} {key},'

        fields = ''.join(fields[0:-1]).strip()

        queryf = sqldict[query]
        
        if query == 'search':
            queryf = queryf.format(table, where)
        elif query == 'update':
            queryf = queryf.format(table, update, where)
        else:
            queryf = queryf.format(fields, table) if query != 'update' and query != 'search' else queryf.format(table, update, where)
            queryf = f'{queryf} {table}'
            queryf = f'{queryf} ({fields}) VALUES ({placeholder.strip()})'
        
        return queryf


data = [
  ('Lucas Brum', 'lucas@example.com', 18),
  ('João da Silva', 'joao@example.net', 22),
  ('Ana Maria', 'ana@example.org', 27)
]

with Database() as db:
    #db.executemany("INSERT OR IGNORE INTO usuarios (nome, email, idade) VALUES (?, ?, ?)", data)
    #result = db.fetchmany("SELECT * FROM usuarios;")
    #print(result)
    
    #db.build_query('usuarios', 'insert', {'nome': 'Lucas', 'apelido': 'Sistematico'})
    #db.build_query('usuarios', 'create', {'nome': 'Lucas', 'apelido': 'Sistematico'})
    #db.build_query('usuarios', 'select', {'nome': 'Lucas', 'apelido': 'Sistematico'})
    #db.build_query('usuarios', 'update', {'nome': 'Lucas', 'apelido': 'Sistematico'}, 'rowid = 1', 'nome = :nome')
    #db.build_query('usuarios', 'search', {'nome': 'Lucas', 'apelido': 'Sistematico'}, 'nome LIKE "%Lucas%"')

    db.execute('usuarios', 'search', {'nome': 'Lucas', 'apelido': 'Sistematico'}, 'nome LIKE "%Lucas%"')

