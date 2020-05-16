import mysql.connector

class MySQL:
    def __init__(self, host, user, passwd, port):
        self.session = None
        self.user = user
        self.host = host
        self.port = port
        self.passwd = passwd

    def connect(self):
        try:
            self.session = mysql.connector.connect(
                host = self.host,
                user = self.user,
                passwd = self.passwd,
                port = self.port
            )
            return self.session
        except mysql.connector.Error as err:
            return print(err)

    def close(self):
        self.session.close()

    def execute(self, command):
        try:
            pass
        except:
            pass

# print(mydb)