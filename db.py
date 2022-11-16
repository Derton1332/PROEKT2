import sqlite3


def ensure_connection(func):
    def inner(*args, **kwargs):
        with sqlite3.connect('anketa.db') as conn:
            res = func(*args, conn=conn, **kwargs)
        return res

    return inner


@ensure_connection
def init_db(conn, force: bool = False):
    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS user_message')

    c.execute('''
        CREATE TABLE IF NOT EXISTS user message (
          id         INTEGER PRIMARY KEY,
          user_id    INTEGER NOT NULL,
          text       TEXT NOT NULL
          )  
    ''')

    conn.comit()


@ensure_connection
def add_message(conn, user_id: int, text: str):
    c = conn.cursor()
    c.execute('INSERT INTO user_message (user_id, text) VALUES (?,?)', (user_id, text))
    conn.comit()


@ensure_connection
def count_message(conn, user_id: int, text: str):
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM user_message WHERE user_id= ? LIMIT 1', (user_id))
    (res,) = c.fetchone()
    return res


@ensure_connection
def list_message(conn, user_id: int, limit: int = 10):
    c = conn.cursor()
    c.execute('SELECT id , text FROM user_massage WHERE user_id = ? ORDER BY id DESC LIMIT ?', (user_id))
    return c.fetchall()
