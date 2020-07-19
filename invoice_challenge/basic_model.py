import invoice_challenge.helpers.model_helper as ModelHelper
import mysql.connector
import os

class BasicModel:
    def connect_to_db(self):
        config = {
            "user": os.environ.get("MYSQL_ROOT_USER"),
            "password": os.environ.get("MYSQL_ROOT_PASSWORD"),
            "host": os.environ.get("MYSQL_HOST"),
            "port": os.environ.get("MYSQL_PORT"),
            "database": os.environ.get("MYSQL_DATABASE")
        }
        return mysql.connector.connect(**config)

    def create_item(self, table, params):
        try:
            connection = self.connect_to_db()
            cursor = connection.cursor()

            columns, values = ModelHelper.format_json_to_create(params)
            query = f"INSERT INTO {table} {columns} VALUES {values}"
            cursor.execute(query)
            connection.commit()
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def read_items(self, table, query_addition):
        try:
            connection = self.connect_to_db()
            cursor = connection.cursor()

            query = f"SELECT * FROM {table} WHERE isActive = true {query_addition}"
            cursor.execute(query)

            columns_description = cursor.description
            rows_data = cursor.fetchall()
            json_data = ModelHelper.format_read_response_to_json(rows_data, columns_description)
            return json_data
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def read_item(self, table, id):
        try:
            connection = self.connect_to_db()
            cursor = connection.cursor()

            query = f"SELECT * FROM {table} " \
                    f"WHERE id = UNHEX(REPLACE('{id}','-','')) AND isActive = true"
            cursor.execute(query)

            columns_description = cursor.description
            rows_data = cursor.fetchall()
            json_data = ModelHelper.format_read_response_to_json(rows_data, columns_description)
            return json_data[0]
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def read_item_by_email(self, table, email, password):
        try:
            connection = self.connect_to_db()
            cursor = connection.cursor()

            query = f"SELECT * FROM {table} " \
                    f"WHERE email = {email} AND password = {password} AND isActive = true"
            cursor.execute(query)

            columns_description = cursor.description
            rows_data = cursor.fetchall()
            json_data = ModelHelper.format_read_response_to_json(rows_data, columns_description)
            return json_data[0]
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def update_item(self, table, id, params):
        try:
            connection = self.connect_to_db()
            cursor = connection.cursor()

            params_formated = ModelHelper.format_json_to_update(params)
            query = f"UPDATE {table} SET {params_formated} " \
                    f"where id = UNHEX(REPLACE('{id}','-','')) and isActive = true"
            cursor.execute(query)
            connection.commit()
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def delete_item(self, table, id):
        try:
            connection = self.connect_to_db()
            cursor = connection.cursor()

            query = f"UPDATE {table} SET isActive = false, deactiveAt = NOW() " \
                    f"where id = UNHEX(REPLACE('{id}','-','')) and isActive = true"
            cursor.execute(query)
            connection.commit()
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
