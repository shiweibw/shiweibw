# -*- coding: utf-8 -*-  
'''
判断一个字符串，是汉字？是数字？是字母？非汉字，数字，字母？
'''

#判断一个unicode是否是数字
def is_number(uchar):
	if '\u0030' <= uchar <= '\u0039':
		return True
	else:
		return False

#判断一个unicode是否是汉字
def is_chinese(uchar):
	if '\u4e00' <= uchar <= '\u9fff' :
		return True
	else :
		return False

#判断一个unicode是否是英文字母
def is_alphabed(uchar):
	if('\u0041' <= uchar <= '\u005a') or ('\u0061' <= uchar <= '\u007a'):
		return True
	else:
		return False

#判断一个unicode是否非汉字，数字和英文字母
def is_other(uchar):
	if not (is_number(uchar) or is_chinese(uchar) or is_alphabed(uchar)):
		return True
	else:
		return False

if __name__ == '__main__':
	if is_number(10):
		print (1)
	if is_chinese('上海'):
		print(1)