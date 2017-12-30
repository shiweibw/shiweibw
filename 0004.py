'''
**第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
'''

#用于存储结果
result={}


def proceline(line):
	global result
	words = line.split()
	if len(words) == 0:
		return
		#空白行直接跳过,不处理.
	else:
		for word in words:				
			if word.isalpha():
				word = word				
			elif word[:-1].isalpha():
				word = word[:-1]
			else:
				break
			#单词改为小写
			word = word.casefold()	

			#用字典计数		
			result[word] = result.get(word,0)+1
						


def checkword(file_name):	
	with open(file_name,'r') as f:
		for line in f:
			proceline(line)
	print(result)

if __name__ == '__main__':
	checkword('doc_for_4.txt')





