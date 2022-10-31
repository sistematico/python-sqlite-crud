#!/usr/bin/env python

import sqlite3
from config import *

class Database:
    def __init__(self):
        try:
            self.connection = sqlite3.connect(DB_FILE) 
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print("Erro: " + e.args[0])

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

    def create(self, table, data):
        sql = self.build_query(table, 'create', data)
        self.cursor.execute(sql)

    # def executemany(self, payload, params):
    #     self.cursor.executemany(payload, params)

    # def fetchone(self, query):
    #     self.cursor.execute(query)        
    #     row = self.cursor.fetchone()        
    #     return row[0] if row else 'Nenhum resultado.'

    # def fetchmany(self, query):
    #     self.cursor.execute(query)        
    #     rows = self.cursor.fetchall()        
    #     return rows[0] if rows else 'Nenhum resultado.'

    def create_table(self):
        if self.connection:
            with open(SQL_FILE, 'r') as sql_file:
                self.connection.executescript(sql_file.read())

    def build_query(self, table, action, data = None, where = None, update = None):
        query = sqldict[action]
        placeholder = ''
        fields = ''

        if data:
            for key in data:
                placeholder = f'{placeholder} :{key}'
                fields = f'{fields} {key},'

            fields = ''.join(fields[0:-1]).strip()
        
        match action:
            case 'create':
                query = query.format(table, fields)
            case 'drop':
                query = query.format(table)
            case 'search':
                query = query.format(table, where)
            case 'update':
                query = query.format(table, update, where)
            case _:
                query = query.format(fields, table)
                query = f'{query} {table}'
                query = f'{query} ({fields}) VALUES ({placeholder.strip()})'

        return query


# data = [
#   ('Lucas Brum', 'lucas@example.com', 18),
#   ('João da Silva', 'joao@example.net', 22),
#   ('Ana Maria', 'ana@example.org', 27)
# ]

with Database() as db:
    #db.executemany("INSERT OR IGNORE INTO usuarios (nome, email, idade) VALUES (?, ?, ?)", data)
    #result = db.fetchmany("SELECT * FROM usuarios;")
    #print(result)
    
    #db.build_query('usuarios', 'create', {'nome': 'Lucas', 'apelido': 'Sistematico'})
    #db.build_query('usuarios', 'insert', {'nome': 'Lucas', 'apelido': 'Sistematico'})
    #db.build_query('usuarios', 'select', {'nome': 'Lucas', 'apelido': 'Sistematico'})
    #db.build_query('usuarios', 'update', {'nome': 'Lucas', 'apelido': 'Sistematico'}, 'rowid = 1', 'nome = :nome')
    #db.build_query('usuarios', 'search', {'nome': 'Lucas', 'apelido': 'Sistematico'}, 'nome LIKE "%Lucas%"')
    print(db.build_query('usuarios', 'drop'))

    # db.execute('usuarios', 'search', {'nome': 'Lucas', 'apelido': 'Sistematico'}, 'nome LIKE "%Lucas%"')

