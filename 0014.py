'''
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}

第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}

第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]


'''

import xlwt,json
from collections import *

def write_excel(infile,outfile):
	with open(infile,'r') as f:
		py_data = json.load(f,object_pairs_hook=OrderedDict)
		#py_data = OrderedDict(json.load(f))
	#infile是json格式的数据。通过json.load转换给python的dict格式的数据。再通过OrderDict转化给有序的字典。
	#print(student_dict)

	#创建excel
	excel = xlwt.Workbook(encoding = 'utf-8')

	#创建sheet
	sheet = excel.add_sheet('sheet_0014')

	#往sheet里写数据
	if isinstance(py_data,dict):
		write_dict_to_exl(sheet,py_data)
	elif isinstance(py_data,list):
		write_list_to_exl(sheet,py_data)

	#保存excel数据
	excel.save(outfile)

def write_dict_to_exl(sheet_obj,data):
	assert isinstance(data,dict),"the input is not the dict"
	row = 0
    #往单元格里写数据
	for k,v in data.items():
		sheet_obj.write(row, 0,k)
		col = 1
        
        # 如果dict中的value是字符串，把它转换为列表
		if isinstance(v,str):
			v = v.split(' ',0)

		for i in v:
			sheet_obj.write(row,col,i)
			col += 1
		row += 1

def write_list_to_exl(sheet_obj,data):
	assert isinstance(data,list),"the input is not the list" 
	row = 0
	for line in data:
		col = 0
		#如果列表(line)中的元素不是又一个列表，要把它转换为列表
		if isinstance(line,str):
			line = line.split(' ',0)
		for content in line:
			sheet_obj.write(row,col,content)
			col += 1
		row += 1



	


if __name__ == '__main__':

	#14题
	write_excel("D:\\Python\\Python_Xue_Xi_Bi_Ji_20160709\\Python每天一道练习题\\0014.json","0014.xls")

	#15题
	write_excel("D:\\Python\\Python_Xue_Xi_Bi_Ji_20160709\\Python每天一道练习题\\0015.json","0015.xls")

	#16题
	write_excel("D:\\Python\\Python_Xue_Xi_Bi_Ji_20160709\\Python每天一道练习题\\0016.json","0016.xls")


'''
import xlwt 
 
 
style = xlwt.XFStyle() # 初始化样式 
font = xlwt.Font() # 为样式创建字体 
font.name = 'Times New Roman' 
font.bold = True # 黑体 
font.underline = True # 下划线 
font.italic = True # 斜体字 
style.font = font # 设定样式 

worksheet.write(1, 0, 'Formatted value', style) # 带样式的写入 
workbook.save('formatting.xls') # 保存文件
'''