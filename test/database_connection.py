from os import environ
import mysql.connector
import pytest

class DatabaseConnection(object):
    def setup_method(self):
        environ["MYSQL_ROOT_USER"] = "root"
        environ["MYSQL_ROOT_PASSWORD"] = "password"
        environ["MYSQL_HOST"] = "localhost"
        environ["MYSQL_PORT"] = "3306"
        environ["MYSQL_DATABASE"] = "invoice_challenge_test"
        db = self.connect_to_mysql()
        database = f"CREATE DATABASE invoice_challenge_test"
        db.cursor().execute(database)
        db.cursor().close()

    def teardown_method(self):
        db = self.connect_to_mysql()
        database = f"DROP DATABASE IF EXISTS invoice_challenge_test;"
        del environ["MYSQL_ROOT_USER"]
        del environ["MYSQL_ROOT_PASSWORD"]
        del environ["MYSQL_HOST"]
        del environ["MYSQL_PORT"]
        del environ["MYSQL_DATABASE"]
        db.cursor().execute(database)
        db.cursor().close()

    def connect_to_mysql(self):
        config = {
            "user": environ.get("MYSQL_ROOT_USER"),
            "password": environ.get("MYSQL_ROOT_PASSWORD"),
            "host": environ.get("MYSQL_HOST"),
            "port": environ.get("MYSQL_PORT")
        }
        return mysql.connector.connect(**config)

    def fill_database(self):
        db = self.connect_to_db()
        tables = f"""CREATE TABLE IF NOT EXISTS invoice (
                          id BINARY(16) PRIMARY KEY,
                          document VARCHAR(255),
                          description VARCHAR(255),
                          amount DECIMAL(19, 2),
                          referenceMonth DATETIME,
                          referenceYear INT,
                          createdAt DATETIME NOT NULL DEFAULT NOW(),
                          isActive BOOLEAN NOT NULL DEFAULT true,
                          deactiveAt DATETIME
                        )"""
        db.cursor().execute(tables)
        db.cursor().close()

    def connect_to_db(self):
        config = {
            "user": environ.get("MYSQL_ROOT_USER"),
            "password": environ.get("MYSQL_ROOT_PASSWORD"),
            "host": environ.get("MYSQL_HOST"),
            "port": environ.get("MYSQL_PORT"),
            "database": environ.get("MYSQL_DATABASE")

        }
        return mysql.connector.connect(**config)
