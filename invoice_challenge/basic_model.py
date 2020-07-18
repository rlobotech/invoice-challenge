import invoice_challenge.model_helper as ModelHelper
import mysql.connector
import os

class BasicModel:
    def connect_to_db(self):
        config = {
            "user": os.environ.get("MYSQL_ROOT_USER"),
            "password": os.environ.get("MYSQL_ROOT_PASSWORD"),
            "host": "db",
            "port": "3306",
            "database": os.environ.get("MYSQL_DATABASE")
        }
        return mysql.connector.connect(**config)

    def create_item(self, table, params):
        connection = self.connect_to_db()
        cursor = connection.cursor()

        columns, values = ModelHelper.format_json_to_create(params)
        query = f"INSERT INTO {table} {columns} VALUES {values}"
        cursor.execute(query)
        connection.commit()

        cursor.close()
        connection.close()

    def read_items(self, table, query_addition):
        connection = self.connect_to_db()
        cursor = connection.cursor()

        query = f"SELECT * FROM {table} WHERE isActive = true {query_addition}"
        cursor.execute(query)

        columns_description = cursor.description
        rows_data = cursor.fetchall()
        json_data = ModelHelper.format_read_response_to_json(rows_data, columns_description)

        cursor.close()
        connection.close()

        return json_data

    def read_item(self, table, id):
        connection = self.connect_to_db()
        cursor = connection.cursor()

        query = f"SELECT * FROM {table} WHERE id = UNHEX(REPLACE('{id}','-','')) AND isActive = true"
        cursor.execute(query)

        columns_description = cursor.description
        rows_data = cursor.fetchall()
        json_data = ModelHelper.format_read_response_to_json(rows_data, columns_description)

        cursor.close()
        connection.close()

        return json_data[0]

    def update_item(self, table, id, params):
        connection = self.connect_to_db()
        cursor = connection.cursor()

        params_formated = ModelHelper.format_json_to_update(params)
        query = f"UPDATE {table} SET {params_formated} where id = UNHEX(REPLACE('{id}','-','')) and isActive = true"
        cursor.execute(query)
        connection.commit()

        cursor.close()
        connection.close()

    def delete_item(self, table, id):
        connection = self.connect_to_db()
        cursor = connection.cursor()

        query = f"UPDATE {table} SET isActive = false, deactiveAt = NOW() where id = UNHEX(REPLACE('{id}','-','')) and isActive = true"
        cursor.execute(query)
        connection.commit()

        cursor.close()
        connection.close()
