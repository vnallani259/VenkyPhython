
import sqlite3
try:
    
    db = sqlite3.connect('data/mydb')

    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTSusers(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)''')
    
    db.commit()

except Exception as e:
    
    db.rollback()
    raise e
finally:
    
    db.close()
