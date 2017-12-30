'''
第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
'''
import uuid
from MySQLcommand import *

#生成一个激活码
def GenCode(num,length=None):
	result = []
	while num > 0:
		id = str(uuid.uuid1()).replace('-', '')
		if length:
			id = id[:length]
		if id not in result:
			result.append(id)
		num -= 1
	return result

#save code to db
def savetomysql():
	test = MySQLcommand('root','123456',db='uuid0002')
	test.connectMySQL()
	test.createMySQLTable(table='uuid_for_0002')
	for code in GenCode(200):
		test.insertMySQL(code)	
	test.closeMysql

if __name__ == '__main__':
	savetomysql()


