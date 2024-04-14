import sqlite3

# Create SQLite database and table
def create_table():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id TEXT NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()

# Initialize the table
create_table()



def create_url(url):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    
    # Insert the new URL into the table
    cursor.execute('INSERT INTO urls (url) VALUES (?)', (url,))
    
    # Get the ID of the newly inserted URL
    url_id = cursor.lastrowid
    
    conn.commit()
    conn.close()
    
    return url_id

def get_url_by_id(url_id):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    
    # Retrieve the URL from the table using the ID
    cursor.execute('SELECT url FROM urls WHERE id = ?', (url_id,))
    
    # Fetch the URL
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return result[0]
    else:
        return None





def create_user(telegram_id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    # Check if the user with the provided Telegram ID already exists
    cursor.execute('SELECT id FROM users WHERE telegram_id = ?', (telegram_id,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        # If the user already exists, return None or raise an exception
        conn.close()
        return None  # You can customize this to raise an exception if needed
    
    # Insert the new user into the table
    cursor.execute('INSERT INTO users (telegram_id) VALUES (?)', (telegram_id,))
    
    # Get the ID of the newly inserted user
    user_id = cursor.lastrowid
    
    conn.commit()
    conn.close()
    
    return user_id


def get_users():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    # Retrieve all user IDs from the table
    cursor.execute('SELECT telegram_id FROM users')
    
    # Fetch all user IDs
    results = cursor.fetchall()
    
    conn.close()
    
    # Extract the user IDs from the results
    user_ids = [row[0] for row in results]
    
    return user_ids


