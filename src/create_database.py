import sqlite3
import os
import glob

mypath = 'dataset'
userid = None

patern = "*.*"
os.chdir(mypath)
filelist = glob.glob(patern)
for f in filelist:
	print('Removing ',f,' ....')
	os.remove(f) 

os.chdir('..')
conn = sqlite3.connect('database.db')
c = conn.cursor()
sql1 = """
DROP TABLE IF EXISTS users;
CREATE TABLE users (
           id integer unique primary key autoincrement,
           name text
);
"""
sql2 = """
DROP TABLE IF EXISTS attendance;
CREATE TABLE attendance (
           id integer unique primary key autoincrement,
           userid integer,
           name text,
           cekinout integer(4) not null default (strftime('%s','now'))
);
"""

c.executescript(sql1)
c.executescript(sql2)
conn.commit()
conn.close()