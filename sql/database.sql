DROP TABLE IF EXISTS usuarios;

DROP TABLE IF EXISTS grupos;

PRAGMA foreign_keys = ON;
        
CREATE TABLE IF NOT EXISTS grupos(
  id INTEGER PRIMARY KEY, 
  gid INTEGER UNIQUE, 
  nome TEXT, 
  flags INTEGER DEFAULT 0000
);

CREATE TABLE IF NOT EXISTS usuarios(
  id INTEGER PRIMARY KEY,
  uid INTEGER,
  gid INTEGER,
  apelido TEXT,
  nome TEXT,
  email TEXT UNIQUE, 
  idade INTEGER,
  warnings INTEGER NOT NULL DEFAULT 0,
  likes INTEGER NOT NULL DEFAULT 0,
  FOREIGN KEY(gid) REFERENCES grupos (gid)
);

CREATE UNIQUE INDEX IF NOT EXISTS usuarios_idx ON usuarios (uid,gid);     