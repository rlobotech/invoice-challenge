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

    def format_json_to_create(self, params):
        json_list = list(params.items())
        columns = "(id, "
        values = "(UNHEX(REPLACE(UUID(), '-', '')), "
        for key, value in json_list:
            if(value == None):
                continue
            columns += f"{key}, "
            values += f"'{value}', "
        columns = columns[:-2] + ")"
        values = values[:-2] + ")"
        return columns, values

    def format_json_to_update(self, params):
        json_list = list(params.items())
        string_result = ""
        for key, value in json_list:
            if(value == None):
                continue
            string_result += f"{key} = '{value}', "
        string_result = string_result[:-2]
        return string_result

    def create_item(self, table, params):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        columns, values = self.format_json_to_create(params)
        cursor.execute(f"INSERT INTO {table} {columns} VALUES {values}")
        connection.commit()

    def read_items(self, table, extra_query):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        query = f"SELECT * FROM {table} WHERE isActive = true {extra_query}"
        cursor.execute(query)
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
        cursor.execute(f"SELECT * FROM {table} WHERE id = UNHEX(REPLACE('{id}','-','')) AND isActive = true")
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

    def update_item(self, table, id, params):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        params_formated = self.format_json_to_update(params)
        cursor.execute(f"UPDATE {table} SET {params_formated} where id = UNHEX(REPLACE('{id}','-','')) and isActive = true")
        connection.commit()

    def delete_item(self, table, id):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {table} SET isActive = false, deactiveAt = NOW() where id = UNHEX(REPLACE('{id}','-','')) and isActive = true")
        connection.commit()
