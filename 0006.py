'''**第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记
最重要的词。'''

import os,os.path



def proceline(result,line):
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
	#用于存储结果
	result={}
	with open(file_name,'r') as f:
		for line in f:
			proceline(result,line)
	return result

def get_imp_word(inputdir):
	for text in os.listdir(inputdir):
		result = checkword(inputdir+"//"+text)
		word = max(result.items(),key=lambda x:x[1])[0]
		print('The important word in %s ==> %s' % (text,word))

if __name__ == '__main__':
	dir = "D:\\Python\\Python_Xue_Xi_Bi_Ji_20160709\\txt_for_6"
	get_imp_word(dir)