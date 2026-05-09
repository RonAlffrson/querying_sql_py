import sqlite3
import pandas as pd


try:
    sqlite_conn = sqlite3.connect('Chinook_Sqlite.db')
    cursor = sqlite_conn.cursor()

    query = "SELECT Name FROM Artist LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)

    df = pd.read_sql_query(query, sqlite_conn)


    # print(df)
except sqlite3.Error as error:
    print('Error occurred -', error)
finally:
    if sqlite_conn:
        sqlite_conn.close()
        print('SQLite Connection closed')    
