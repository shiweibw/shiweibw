'''第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。'''

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
			self.words = list(map(lambda s:s.strip(),f.readlines()))
		except Exception as e:
			raise e
		finally:
			if f:
				f.close()
		

	#当无法识别输入的command时调用该方法
	def default(self,line):
		self.line = line
		words = [filter_word for filter_word in self.words if filter_word in line]
		if words != []:
			for x in words:
				self.line = self.line.replace(x,"*"*len(x))
		print(self.line)
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




