#!/usr/bin/env python

DB_FILE = '../data/database.db'
SQL_FILE = '../sql/database.sql'

sqldict = {
  "create": "CREATE TABLE IF NOT EXISTS {} ({})",
  "drop": "DROP TABLE IF EXISTS {}",
  "select": "SELECT ({}) FROM {}",
  "select_all": "SELECT * FROM {}",
  "insert": "INSERT OR IGNORE INTO",
  "update": "UPDATE {} SET {} WHERE {}",
  "delete": "DELETE FROM {} WHERE {}",
  "delete_all": "DELETE FROM {}",
  "search": "SELECT * FROM {} WHERE {}"
}
