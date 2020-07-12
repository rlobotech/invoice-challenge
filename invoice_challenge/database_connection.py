from typing import List, Dict
import mysql.connector
import os
import json
import datetime, decimal, uuid

def connect_to_db():
    config = {
        'user': os.environ.get('MYSQL_ROOT_USER'),
        'password': os.environ.get('MYSQL_ROOT_PASSWORD'),
        'host': 'db',
        'port': '3306',
        'database': os.environ.get('MYSQL_DATABASE')
    }
    return mysql.connector.connect(**config)

def format_mysql_types_to_json(value):
    if type(value) == datetime.datetime:
        return str(value)
    if type(value) == decimal.Decimal:
        return float(value)
    if type(value) == bytearray:
        return str(uuid.UUID(bytes=bytes(value)))
    return value

def invoice() -> List[Dict]:
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM invoice')
    row_headers=[x[0] for x in cursor.description]
    all_rows_data = cursor.fetchall()
    json_data=[]
    for row_data in all_rows_data:
        row_values = []
        for value in row_data:
            row_values.append(format_mysql_types_to_json(value))
        json_data.append(dict(zip(row_headers, row_values)))
    cursor.close()
    connection.close()
    return json_data

def main():
    print (json.dumps({'invoice': invoice()}))

if __name__ == '__main__':
    main()
