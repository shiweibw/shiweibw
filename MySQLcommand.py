import pymysql
class ConnectMysqlException(Exception):
	pass
class CreateTableException(Exception):
	pass

class MySQLcommand():
	def __init__(self,user,password,**kw):
		self.port = kw.setdefault('port',3306)
		self.db = kw.setdefault('db',None)
		self.table = kw.setdefault('table',None)
		self.host = kw.setdefault('host',"127.0.0.1")
		self.user = user
		self.password = password
    
	def connectMySQL(self):
		try:
			self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.password,charset="utf8")
			self.cus = self.conn.cursor()			
		except Exception as reason:
		 	print("connect mysql error: %s " % reason)
		 	raise ConnectMysqlException 

		if self.db is not None:
		 	sql = "CREATE DATABASE IF NOT EXISTS " + self.db
		 	self.cus.execute(sql)
		self.cus.execute("use " + self.db)
			
	def queryMySQLTable(self,table):
		result = False
		self.table = table
		sql = "show tables"
		self.cus.execute(sql)
		all_tables = self.cus.fetchall()
		for table_name in all_tables:
			if table_name[0] == self.table:
				result = True
		return result
        
		
	def createMySQLTable(self,table=None):
		if table:
			self.table = table
		sql = "CREATE TABLE IF NOT EXISTS " + self.table +\
		      " (code CHAR(32) not null) ENGINE=INNODB CHARSET='utf8'"     
		try:
			self.cus.execute(sql)
		except Exception as reason: 
			raise CreateTableException("fail to create Table")


 
	def insertMySQL(self,uuid):
		self.uuid = uuid
		sql = "INSERT INTO " + self.table + " (code) VALUE (" + "\'" + self.uuid + "\'" + ")"	
		try:
			self.cus.execute(sql)
			self.conn.commit()
		except Exception as reason:
			print("insert failed: %s" % reason)
			self.conn.rollback()
		
	def closeMysql(self):
		self.cus.close()
		self.conn.close()