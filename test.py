import xlwt,json
from collections import *

with open('test.txt','r') as f:
	student_dict = json.load(f,object_pairs_hook=OrderedDict)
	#content = f.read()
#print(content)
#student_dict = json.loads(content,object_pairs_hook=OrderedDict)
if isinstance(student_dict,dict):
	print('haha')
print(student_dict)
print(type(student_dict))