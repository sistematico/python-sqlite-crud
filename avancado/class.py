#!/usr/bin/env python

import sqlite3
from config import *

class Database:
    DB_FILE = "database.db"

    def __init__(self):
        self.connection = sqlite3.connect(self.DB_FILE)
        self.connection.set_trace_callback(print)
        # self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()

        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        
        # self.connection.close()

    def close(self):
        self.connection.close()

    def execute(self, payload, params):
        self.cursor.execute(payload, params)

    def executemany(self, payload, params):
        self.cursor.executemany(payload, params)

    def commit(self):
        self.connection.commit()

    def fetchone(self, query):
        self.cursor.execute(query)        
        row = self.cursor.fetchone()        
        
        if rows:
            return rows[0]
        else:
            return 0

    def query(self, query, params, ret=True):
        self.cursor.execute(query, params)        
        rows = self.cursor.fetchone()        
        self.connection.close()

        if ret:
            if rows:
                return rows[0]
            else:
                return 0

    def create_table(self):
        with open('sql/database.sql', 'r') as sql_file:
            self.connection.executescript(sql_file.read())