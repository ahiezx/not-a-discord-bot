import mysql.connector

class MySQL:
	def __init__(self, host, user, passwd, port, db):
		self.session = None
		self.user = user
		self.host = host
		self.port = port
		self.passwd = passwd
		self.db = db

	def connect(self):
		try:
			self.session = mysql.connector.connect(
			host = self.host,
			user = self.user,
			passwd = self.passwd,
			port = self.port,
			database = self.db
			)
		except mysql.connector.Error as err:
			self.session = mysql.connector.connect(
			host = self.host,
			user = self.user,
			passwd = self.passwd,
			port = self.port,
			# database = self.db
			)
			mycursor = self.session.cursor()
			mycursor.execute("CREATE DATABASE " + self.db)
			self.session.commit()
			self.connect()

		return self.session

	def close(self):
		self.session.close()

	def execute(self, command):
		try:
			pass
		except:
			pass

# print(mydb)