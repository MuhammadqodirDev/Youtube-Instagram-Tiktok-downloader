import sqlite3

# Create SQLite database and table
def create_table():
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL
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


