"""
Test goes here

"""

import sqltie3

if __name__ == "__main__":
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('count * FROM users')
    num = cursor.fetchall()
    assert(num==2)
