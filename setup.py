import sqlite3
conn = sqlite3.connect('visitors.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE visitors (id INTEGER PRIMARY KEY, groups char(100) NOT NULL, fio char(100) NOT NULL, datetime char(100) NOT NULL, ip char(100) )")
conn.commit()
