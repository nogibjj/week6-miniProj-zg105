[![CI](https://github.com/Jason-Guo1999/IDS706-Python-Template/actions/workflows/main.yml/badge.svg)](https://github.com/Jason-Guo1999/IDS706-Python-Template/actions/workflows/main.yml)
# IDS706-Week5-MiniProj
This project uses sqlite3 library to interact with a SQL database and do CRUD tasks. 
- ``workflows`` is for github actions, enables automated CI/CD for the project

- ``Makefile`` lists make instruments

- ``requirements.txt`` lists the dependencies for the project, add sqlite3 dependency
  
- ``main.py`` connect to sqltie3 database. Create a new table of users, then add two new users, perform inquiry. 

- ``test_main.py`` test if I have inserted two users.

## CRUD operations

- ``Create``:    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,username TEXT NOT NULL,)''')
- ``Read``:      cursor.execute('SELECT username FROM users')
- ``Update``:    cursor.execute('INSERT INTO users (username) VALUES ('zg105'))
- ``Delete``:    cursor.execute('DELETE from users where username = zg105')
