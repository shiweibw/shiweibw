
# -*- coding: utf-8 -*- 
__author__ = 'shiweibw'
'''
Parse the given XML input and convert it into a dictionary.

`xml_input` can either be a `string` or a file-like object.

If `xml_attribs` is `True`, element attributes are put in the dictionary
    among regular child elements, using `@` as a prefix to avoid collisions. If
    set to `False`, they are just ignored.

the dictionary is stored in item
'''

try:
    from defusedexpat.pyexpat import expat
except ImportError:
    from xml.parsers.expat import ParserCreate
from xml.sax.saxutils import XMLGenerator
from xml.sax.xmlreader import AttributesImpl
try:  # pragma no cover
    from cStringIO import StringIO
except ImportError:  # pragma no cover
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
try:  # pragma no cover
    from collections import OrderedDict
except ImportError:  # pragma no cover
    try:
        from ordereddict import OrderedDict
    except ImportError:
        OrderedDict = dict

try:  # pragma no cover
    _basestring = basestring
except NameError:  # pragma no cover
    _basestring = str
try:  # pragma no cover
    _unicode = unicode
except NameError:  # pragma no cover
    _unicode = str
try:
	import io
except ImportError:
	print('no this module: io')





class ParsingInterrupted(Exception):
    pass


class xml2dict(object):
    def __init__(self,
                 item_depth=0,
                 item_callback=lambda *args: True,
                 xml_attribs=True,
                 attr_prefix='@',
                 cdata_key='#text',
                 force_cdata=False,
                 cdata_separator='',
                 postprocessor=None,
                 dict_constructor=OrderedDict,
                 strip_whitespace=True,
                 namespace_separator=':',
                 namespaces=None,
                 force_list=None,
                 xml_input=None):
        self.path = []
        self.stack = []
        self.data = []
        self.item = None
        self.item_depth = item_depth
        self.xml_attribs = xml_attribs
        self.item_callback = item_callback
        self.attr_prefix = attr_prefix
        self.cdata_key = cdata_key
        self.force_cdata = force_cdata
        self.cdata_separator = cdata_separator
        self.postprocessor = postprocessor
        self.dict_constructor = dict_constructor
        self.strip_whitespace = strip_whitespace
        self.namespace_separator = namespace_separator
        self.namespaces = namespaces
        self.namespace_declarations = OrderedDict()
        self.force_list = force_list
        self._parser = ParserCreate()
        self._parser.StartElementHandler = self.startElement
        self._parser.EndElementHandler = self.endElement
        self._parser.CharacterDataHandler = self.characters

        if xml_input:
        	self.parseXml(xml_input)
        	self.close()

    def _build_name(self, full_name):
        if not self.namespaces:
            return full_name
        i = full_name.rfind(self.namespace_separator)
        if i == -1:
            return full_name
        namespace, name = full_name[:i], full_name[i+1:]
        short_namespace = self.namespaces.get(namespace, namespace)
        if not short_namespace:
            return name
        else:
            return self.namespace_separator.join((short_namespace, name))

    def _attrs_to_dict(self, attrs):
        if isinstance(attrs, dict):
            return attrs
        return self.dict_constructor(zip(attrs[0::2], attrs[1::2]))

    def startNamespaceDecl(self, prefix, uri):
        self.namespace_declarations[prefix or ''] = uri

    def startElement(self, full_name, attrs):
        name = self._build_name(full_name)
        attrs = self._attrs_to_dict(attrs)
        if attrs and self.namespace_declarations:
            attrs['xmlns'] = self.namespace_declarations
            self.namespace_declarations = OrderedDict()
        self.path.append((name, attrs or None))
        if len(self.path) > self.item_depth:
            self.stack.append((self.item, self.data))
            if self.xml_attribs:
                attr_entries = []
                for key, value in attrs.items():
                    key = self.attr_prefix+self._build_name(key)
                    if self.postprocessor:
                        entry = self.postprocessor(self.path, key, value)
                    else:
                        entry = (key, value)
                    if entry:
                        attr_entries.append(entry)
                attrs = self.dict_constructor(attr_entries)
            else:
                attrs = None
            self.item = attrs or None
            self.data = []
            '''
            print('==start==')
            print('item == %s' % str(type(self.item)))
            print(self.item)
            print('data == %s' % str(type(self.data)))
            print(self.data)
            print('stack == %s' % str(type(self.stack)))
            print(self.stack)
            print('path == %s' % str(type(self.path)))
            print(self.path)
            print('=================')
            '''


    def endElement(self, full_name):
        name = self._build_name(full_name)
        if len(self.path) == self.item_depth:
            item = self.item
            if item is None:
                item = (None if not self.data
                        else self.cdata_separator.join(self.data))

            should_continue = self.item_callback(self.path, item)
            if not should_continue:
                raise ParsingInterrupted()
        if len(self.stack):
            data = (None if not self.data
                    else self.cdata_separator.join(self.data))
            item = self.item
            self.item, self.data = self.stack.pop()
            if self.strip_whitespace and data:
                data = data.strip() or None
            if data and self.force_cdata and item is None:
                item = self.dict_constructor()
            if item is not None:
                if data:
                    self.push_data(item, self.cdata_key, data)
                self.item = self.push_data(self.item, name, item)
            else:
                self.item = self.push_data(self.item, name, data)
        else:
            self.item = None
            self.data = []
        self.path.pop()
        
        #print('==end==')
        #print('item == %s' % str(type(self.item)))
        #print(self.item)
        #print('data == %s' % str(type(self.data)))
        #print(self.data)
        #print('stack == %s' % str(type(self.stack)))
        #print(self.stack)
        #print('path == %s' % str(type(self.path)))
        #print(self.path)
        #print('=================')
        


    def characters(self, data):
        if not self.data:
            self.data = [data]
        else:
            self.data.append(data)
        '''
        print('==chara==')
        print('data == %s' % str(type(data)))
        print(data)
        print('=================')
        '''


    def push_data(self, item, key, data):
        if self.postprocessor is not None:
            result = self.postprocessor(self.path, key, data)
            if result is None:
                return item
            key, data = result
        if item is None:
            item = self.dict_constructor()
        try:
            value = item[key]
            if isinstance(value, list):
                value.append(data)
            else:
                item[key] = [value, data]
        except KeyError:
            if self._should_force_list(key, data):
                item[key] = [data]
            else:
                item[key] = data
        return item

    def _should_force_list(self, key, value):
        if not self.force_list:
            return False
        try:
            return key in self.force_list
        except TypeError:
            return self.force_list(self.path[:-1], key, value)

    def parseXml(self,xml_input):
        if isinstance(xml_input,str):
            self._parser.Parse(xml_input)
        try:
            if isinstance(xml_input,file):
                self._parser.ParseFile(xml_input)
        except Exception:
            if isinstance(xml_input,io.TextIOWrapper):
                self._parser.ParseFile(xml_input) 
    def get_result(self):
        return self.item       

    def close(self):
        self._parser.Parse("",0)
        del self._parser
            
if __name__ == '__main__':
    xml = "<a prox='x'><b>中文</b><b>2</b></a>"
    print(type(xml))
    result_dict = xml2dict(xml_input=xml).item
    print(result_dict)




'''
# -*- coding: utf-8 -*-  
from __future__ import print_function
# __future__ 模块很有用

#import StringIO
import sys,gzip
from io import StringIO
from io import BytesIO
from xml.parsers.expat import ParserCreate
from collections import OrderedDict
import time


xmltodict 源码：https://github.com/martinblech/xmltodict/blob/master/xmltodict.py

xml 转换成jason
思路：xml 转换成字典，通过jason的方法将字典转换为jason的数据

class xml2dict(object):
	def __init__(self,data=None,namespaces=None,attr_prefix='@',xml_attribs=True,dict_constructor=OrderedDict):
		#用OrderedDict 来代替一个普通的字典，OrderedDict可以保持顺序。
		self.namespaces = namespaces
		self._parser = ParserCreate()
		self._parser.StartElementHandler = self.start_element
		self._parser.EndElementHandler = self.end_element
		self._parser.CharacterDataHandler = self.char_data
		self.result = None
		self.attr_prefix = attr_prefix
		self.xml_attribs = xml_attribs
		self.dict_constructor = dict_constructor

		if data:
			self.parseXml(data)
			self.close()

	def _build_name(self,full_name):
		if not self.namespaces:
			return full_name

	def _attrs_to_dict(self,attrs):
		if isinstance(attrs,dict):
			return attrs
		return self.dict_constructor(zip(attrs[0::2],attrs[1::2]))

	def start_element(self,full_name,attrs):
		assert self._data.strip() == ''
		name = self._build_name(full_name)
		self._stack.append([name])
		self._data = ''

	def end_element(self,name):
		last_name = self._stack.pop()
		assert last_name[0] == name
		if len(last_name) == 1:
			data = self._data
		else:
			data = [{k:v} for k, v in last_name[1:]]

		if self._stack:
			self._stack[-1].append((name,data))
		else:
			self.result = {name:data}

		self._data = ''

	def char_data(self,char_value):
		self._data = char_value

	def parseXml(self,data):
		self._stack = []
		self._data = ""
		self._parser.Parse(data)

	def close(self):
		self._parser.Parse("",0)
		del self._parser

def parserXML(xml_input,):
	pass
'''