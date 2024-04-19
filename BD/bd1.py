import sqlite3 as sq
from date.data_users import info_users


class operations_db:
    def __init__(self):
        self.connection = sq.connect('saper.db')
        self.cur = sq.connect('saper.db').cursor()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    sex INTEGER NOT NULL DEFAULT 1,
                    old INTEGER,
                    score INTEGER
                    )""")

    def insert_DB(self):
        self.cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)

    def Select_DB(self):
        self.cur.execute("SELECT * FROM users WHERE score > 1000 ORDER BY score DESC")
        result = cur.fetchall()
        print(result)

    @classmethod
    def classmethod_1(cls):
        return 'Hello, epti'


class Requests(operations_db):
    def __init__(self):
        operations_db.__init__(self)

    def create_table(self):
        print(2)


cls = Requests()

cls.create_table()

# MyClass = Connections('vasya' ,'pupkin') # Инициализация класса
# MyClass.create_table()
# my_data = MyClass.cur.execute('SELECT * FROM users').fetchall()
#
# print(my_data)
