'''第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
{
	"1" : ["张三", 150, 120, 100],
	"2" : ["李四", 90, 99, 95],
	"3" : ["王五", 60, 66, 68]
}
</students>
</root>

第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：

<?xmlversion="1.0" encoding="UTF-8"?>
<root>
<citys>
<!--
	城市信息
-->
{
	"1" : "上海",
	"2" : "北京",
	"3" : "成都"
}
</citys>
</root>

第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下

所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!--
	数字信息
-->

[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]

</numbers>
</root>

'''

#import xlwt
import xlrd
from xml.etree.ElementTree import Element, SubElement, ElementTree,Comment
from xml.dom import minidom

#用Comment()来生成element实例,用这个实例来代表comment
comments = {'0014.xls':[Comment('学生信息表"id" : [名字, 数学, 语文, 英文]'),'students'],
			'0015.xls':[Comment('城市信息'),'citys'],
			'0016.xls':[Comment('数字信息'),'numbers']}

def write_to_xml(infile,outfile):   
	#生成根节点
	root = Element('root')

	

	#生成根节点下面的子节点 students or citys or numbers
	child = SubElement(root,comments[infile.strip()][1])
	
	#把comment这个element实例，添加到子节点head下
	child.append(comments[infile.strip()][0])

	#students的内容
	content = read_from_exl(infile)	
	child.text = str(content)

	#生成xml树的对象tree，然后将 xml 内容写成一个文件
	tree = ElementTree(root)
	tree.write(outfile, encoding='utf-8',xml_declaration=True)
	

def read_from_exl(infile):
	if comments[infile.strip()][1] == 'numbers':
		result=[]
	else:
		result={}
	data = xlrd.open_workbook(infile)
	table = data.sheet_by_index(0)

	for row in range(table.nrows):
		data = table.row_values(row)
		if type(result) is list:
			result.append(data)
		else:
			result[data[0]] = data[1:]
	return result
'''
def prettyXml(element,indent,newline,level=0):
	# elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行    
	if element:
		if element.text == None or element.text.isspace(): 
			#element.text没有内容,则换行
			element.text = newline + indent * (level + 1)
		else:
			element.text = newline+indent*(level+1) + element.text.strip() + newline+indent*(level+1)
	# 将elemnt转成list		
	temp = list(element)     
	for subelement in temp:    
		if temp.index(subelement) < (len(temp) - 1): 
		# 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致    
			subelement.tail = newline + indent * (level + 1)    
		else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个    
			subelement.tail = newline + indent * level    
		prettyXml(subelement, indent, newline, level = level + 1) # 对子元素进行递归操作    
'''
            

if __name__ == '__main__':
	write_to_xml('0014.xls','result_14.xml')
	write_to_xml('0015.xls','result_15.xml')
	write_to_xml('0016.xls','result_16.xml')

	'''
	#ElementTree.parse(f) =>Returns an ElementTree instance 	
	with open('result.xml') as f:
		tree = ElementTree.parse(f)

	#得到根元素，Element类   
	root = tree.getroot()

	#执行美化方法,for linux：newline='\n'
	prettyXml(root, '\t', '\r\n')
	#显示出美化后的XML内容
	ElementTree.dump(root)
	'''