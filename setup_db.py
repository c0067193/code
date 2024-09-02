import sqlite3


conn = sqlite3.connect('camera_app.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')


cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("testuser", "testpassword"))


conn.commit()
conn.close()

print("Database setup complete. User 'testuser' with password 'testpassword' created.")