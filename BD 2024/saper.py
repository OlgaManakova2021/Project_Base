import sqlite3 as sq
from data_users import info_users

with sq.connect('saper.db') as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
    )""")

# with sq.connect('saper.db') as con:
#     cur = con.cursor()
#     cur.execute("INSERT INTO users VALUES (1, 'olga', 2, 22, 1000)")

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE score > 900 ORDER BY score DESC")
    result = cur.fetchall()
    print(result)

# with sq.connect('saper.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE users SET score = score+100 WHERE name LIKE 'М%'")

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM users WHERE user_id = 5")

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    print(result)