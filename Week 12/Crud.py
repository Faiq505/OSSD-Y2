import sqlite3

def create_database():

    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    '''

    cursor.execute(create_table)

    conn.commit()
    conn.close()


def add_user():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    insert = 'INSERT INTO users(name, age) VALUES(?, ?)'
    cursor.execute(insert, ("Faiqali", 21))

    conn.commit()
    conn.close()


create_database()   # Creates table only if it doesn't exist
add_user()          # Inserts data

print("Database ready and user added successfully!")