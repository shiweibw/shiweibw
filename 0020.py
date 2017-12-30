'''第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，
点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31
日通话详单.xls 文件。写代码，对每月通话时间做个统计。'''

import xlrd
import re
from collections import OrderedDict

def analy_phone(infile):
	a = '对方号码'
	b = '通信时长'

    #打开execl文件,并通过索引获取sheet对象
	data = xlrd.open_workbook(infile)
	table = data.sheet_by_index(0)
	result = {}

	index_data = False

	#确定电话号码和通信时长的列数：
	for rows in range(table.nrows):
		data = table.row_values(rows)
		if a in data and b in data:
			col_num = data.index(a)
			col_time = data.index(b)
			start_row = rows
			break

	for row in range(start_row+1,table.nrows):
		time_data = table.row_values(row)[col_time].split(':')
		time_seconds = int(time_data[0])*3600 + int(time_data[1])*60 + int(time_data[2])

        #设置缺省值。
		result.setdefault((table.row_values(row)[col_num]),[0,0])
        #统计通话时长
		result[table.row_values(row)[col_num]][0] += time_seconds
		#统计通话次数
		result[table.row_values(row)[col_num]][1] += 1
	
	#打印结果
	output = OrderedDict(sorted(result.items(), key=lambda t: t[1][1],reverse = True))

	#max_num = max(result.items(),key=lambda x:x[1][1])
	#print('联系最频繁用户:%s,    通话次数:%s,    通话时长:%s' % (str(max_num[0]),str(max_num[1][1]),str(max_num[1][0])+'s'))
	#print('其余通话详情：')
	for key,value in output.items():
		print('用户:%s通话次数:%s通话总时长:%s' % (str(key).ljust(20),str(value[1]).ljust(5),str(value[0])+'s'))



	#print(max_num)

if __name__ == '__main__':
	analy_phone('D:\\Python\\Python_Xue_Xi_Bi_Ji_20160709\\Python每天一道练习题\\13761652322_通话详单.xls')








					









