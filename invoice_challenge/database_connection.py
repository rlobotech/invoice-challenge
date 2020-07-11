from typing import List, Dict
import mysql.connector
import json

def connect_to_db():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'invoice_challenge'
    }
    return mysql.connector.connect(**config)

def invoice() -> List[Dict]:
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM invoice')
    results = [{document: description} for (document, description) in cursor]
    cursor.close()
    connection.close()

    return results

def main():
    # return json.dumps({'invoice': invoice()})
    print (json.dumps({'invoice': invoice()}))

if __name__ == '__main__':
    main()
