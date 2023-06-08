import sqlite3

conn = sqlite3.connect("data.db")
t1 = "CREATE TABLE IF NOT EXISTS num(number TEXT);"


def create_tabel():
    with conn:
        conn.execute(t1)


create_tabel()


def add_num(num):
    with conn:
        conn.execute("INSERT INTO num(number) VALUES (?);", (num,))


def get_num():
    # I don't know why i did not use .fetch_all()
    # anywhere in this function
    # and it still works
    with conn: # I know i don't need commit() while using 'with'
        cur = conn.cursor()
        data = cur.execute("SELECT * FROM num;")
        return data # but .fetch_all() ?


def delete_data():
    with conn:
        conn.execute("DELETE FROM num;")