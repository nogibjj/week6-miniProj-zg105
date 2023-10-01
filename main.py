import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
        )
    ''')

    # Update
    cursor.execute('INSERT INTO users (username) VALUES ('zg105'))
    cursor.execute('INSERT INTO users (username) VALUES ('yl794'))
    
    conn.commit()

    # Read
    cursor.execute('SELECT username FROM users')

    # Delete
    cursor.execute('DELETE from users where username = zg105')
    users = cursor.fetchall()
    
    for user in users:
        print(user)
    
    # Close the connection
    conn.close()
