import sqlite3 as sq
from date.data_users import info_users

with sq.connect('saper.db') as con:
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
    )""")

with sq.connect('saper.db') as con:
    cur = con.cursor()

    # cur.execute("INSERT INTO users VALUES (1, 'Алексей', 1, 22, 1000)")
    # cur.execute("INSERT INTO users VALUES (2, 'Миша', 1, 19, 800)")
    # cur.execute("INSERT INTO users VALUES (3, 'Федор', 1, 26, 1100)")
    # cur.execute("INSERT INTO users VALUES (4, 'Маша', 2, 18, 1500)")


    cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)



