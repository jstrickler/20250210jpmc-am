import sqlite3

conn = None

try:
    conn = sqlite3.connect('/blurch/mydatabase.db')
except sqlite3.DatabaseError as err:
    print(err)
    exit()
else:
    cursor = conn.cursor()
    # cursor.execute(...)
finally: # in all cases, even if an except block exits
    if conn is not None:
        conn.close()