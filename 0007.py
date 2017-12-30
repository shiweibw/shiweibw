'''
**第 0007 题：**有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
'''

import os,os.path

def analy_code(code_path):
	Code_lines = 0          #代码行数
	Blank_lines = 0         #空白行数 内容为\n strip()后为''
	Comment_lines = 0       #注释行数
	is_comment = False      
	start_comment_line = 0  #记录以''' 或 """开头的注释位置

	with open(code_path,'r',encoding='utf-8') as f:
		for index,line in enumerate(f,start=1):
			#print("==Begin== %s" % str(index))
			line = line.strip()

            #看到''' 或者 """ 就修改is_comment 标签
			if line.startswith("'''") or line.startswith('"""') or line.endswith("'''") or line.endswith('"""'):
				is_comment = not is_comment
				Comment_lines += 1
				continue

			if is_comment:
				Comment_lines += 1
			else:
				#单行注释
				if line.startswith('#'):
					Comment_lines += 1

				#空白行
				elif line == '':
					Blank_lines += 1

				#代码行	
				else:
					Code_lines += 1
		print('Code_lines is %s\nBlank_lines is %s\nComment_lines is %s' % (str(Code_lines),str(Blank_lines),str(Comment_lines)))

if __name__ == '__main__':
	analy_code('0001.py')
			





	

