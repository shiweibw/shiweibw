'''
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
import uuid

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

if __name__ == '__main__':
	print(GenCode(200))