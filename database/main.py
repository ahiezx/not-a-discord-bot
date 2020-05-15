import mysql.connector

class MySQL:
    def __init__(self, host, user, passwd, port):
        self.current_open_connection = ""
        self.user = user
        self.host = host
        self.port = port
        self.passwd = passwd

    def connect(self):
        self.current_open_connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            port = self.port
        )
        return self.current_open_connection
    def close(self):
        self.current_open_connection.close()

# print(mydb)