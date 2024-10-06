import pandas as pd
import pyodbc


class Database:

    _server = ""
    _database = ""
    _connection_string = ""

    def __init__(self, server, database, username, password):
        self._server = server
        self._database = database
        self._connection_string = "Driver={SQL Server Native Client 11.0};"
        "Server=" + self._server + ";"
        "Database=" + self._database + ";"
        "uid=" + username + ";pwd=" + password + ";"
        "Trusted_Connection=yes;"

    def get_data_in_dataframe(self, query):
        connection = pyodbc.connect(self._connection_string)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        df = pd.DataFrame(rows)
        connection.close()
        return df
