from typing import List, Dict
import mysql.connector
import os
import datetime, decimal, uuid

class BasicModel:
    def connect_to_db(self):
        config = {
            'user': os.environ.get('MYSQL_ROOT_USER'),
            'password': os.environ.get('MYSQL_ROOT_PASSWORD'),
            'host': 'db',
            'port': '3306',
            'database': os.environ.get('MYSQL_DATABASE')
        }
        return mysql.connector.connect(**config)

    def format_mysql_values_to_json(self, value):
        if type(value) == datetime.datetime:
            return str(value)
        if type(value) == decimal.Decimal:
            return float(value)
        if type(value) == bytearray:
            return str(uuid.UUID(bytes=bytes(value)))
        return value

    def read_items(self, table):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table} where isActive = true")
        row_headers=[x[0] for x in cursor.description]
        all_rows_data = cursor.fetchall()
        json_data=[]
        for row_data in all_rows_data:
            row_values = []
            for value in row_data:
                row_values.append(self.format_mysql_values_to_json(value))
            json_data.append(dict(zip(row_headers, row_values)))
        cursor.close()
        connection.close()
        return json_data

    def read_item(self, table, id):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table} where id = UNHEX(REPLACE('{id}','-','')) and isActive = true")
        row_headers=[x[0] for x in cursor.description]
        all_rows_data = cursor.fetchall()
        json_data=[]
        for row_data in all_rows_data:
            row_values = []
            for value in row_data:
                row_values.append(self.format_mysql_values_to_json(value))
            json_data.append(dict(zip(row_headers, row_values)))
        cursor.close()
        connection.close()
        return json_data

if __name__ == '__main__':
    basic_model = BasicModel()
    print(basic_model.read_item('invoice', "149d6710-c3d4-11ea-a09e-0242ac120002"))
