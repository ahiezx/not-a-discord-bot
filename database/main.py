import mysql.connector

class MySQL:
    def __init__(self, host, user, passwd, port):
        self.session = ""
        self.user = user
        self.host = host
        self.port = port
        self.passwd = passwd

    def connect(self):
        self.session = mysql.connector.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            port = self.port
        )
        return self.session
    def close(self):
        self.session.close()

# print(mydb)