'''第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，
否则打印出 Human Rights。
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
'''

from cmd import Cmd
import sys

class CmdTest(Cmd):
	def __init__(self,filter_db):
		Cmd.__init__(self)
		self.prompt = "> "
		self.intro = "Welcome to my Shell"
		self.filter_db = filter_db
		try:
			f = open(filter_db,'r')
			self.word = list(map(lambda s:s.strip(),f.readlines()))
		except Exception as e:
			raise e
		finally:
			if f:
				f.close()
		

	#当无法识别输入的command时调用该方法
	def default(self,line):
		#any() 函数用于判断给定的可迭代参数 iterable 是否全部为空对象
		if any([i in line for i in self.word]):
			print('Freedom')
		else:
			print('Human Rights')
	def help_exit(self):
		print('输入exit退出程序')
	def do_exit(self,line):
		print("Exit:",line)
		sys.exit()
if __name__ == '__main__':
	filter_db = "D:\\Python\\Python_Xue_Xi_Bi_Ji_20160709\\Python每天一道练习题\\filter_db.txt"
	cmd=CmdTest(filter_db)

	#运行cmd解析器
	cmd.cmdloop()




