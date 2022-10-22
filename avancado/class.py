#!/usr/bin/env python

import sqlite3
from config import *

class Database:

    def __init__(self):
        self.connection = sqlite3.connect(DB_FILE)
        self.cursor = self.connection.cursor()

    def __exit__(self):
        self.connection = sqlite3.connect(DB_FILE)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def insert(self, payload, params):
        self.cursor.execute(payload, params)
        self.connection.commit()

    def execute(self, payload, params):
        self.cursor.execute(payload, params)

    def executemany(self, payload, params):
        self.cursor.executemany(payload, params)

    def commit(self):
        self.connection.commit()

    def fetchone(self, query):
        self.cursor.execute(query)        
        row = self.cursor.fetchone()        
        return row[0] if row else 'Nenhum resultado.'

    def fetchmany(self, query):
        self.cursor.execute(query)        
        rows = self.cursor.fetchall()        
        self.connection.close()
        return rows[0] if rows else 'Nenhum resultado.'

    def create_table(self):
        with open(SQL_FILE, 'r') as sql_file:
            self.connection.executescript(sql_file.read())

db = Database()
result = db.fetchmany("SELECT * FROM usuarios;")
print(result)

