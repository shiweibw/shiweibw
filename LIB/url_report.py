# -*- coding: utf-8 -*-  
'''
get URL response, the data is with XML format
'''

from urllib.request import Request,urlopen,ProxyHandler,build_opener,install_opener
from urllib.error import URLError,HTTPError
import sys,gzip,pymysql,os
from io import StringIO
from io import BytesIO

try:
	from URLProxy import get_proxy_info
except ImportError:
	path = "D:\Python\Python_Xue_Xi_Bi_Ji_20160709\\2017_Program\LIB"
	sys.path.append(path)
	from URLProxy import get_proxy_info


class url_report():
	def __init__(self,url,decoding='utf-8'):
		self.url = url
		self.decoding = decoding
	
	def get_data(self):
		'''
		response = urllib.request.urlopen(url)
		urlopen()方法可以实现最基本请求的发起，但这几个简单的参数并不足以构建一个完整的请求，
		如果请求中需要加入headers（请求头）等信息，我们就可以利用更强大的Request类来构建一个请求。
		'''
		
		#实例化Request类，生成一个对象
		self.req = Request(self.url)
		#设置header头部信息
		self.req.add_header('Host','wthrcdn.etouch.cn')
		self.req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54')
		self.req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
		self.req.add_header('Accept-Language','en-US,en;q=0.5')
		self.req.add_header('Connection','keep-alive')


		#open url,得到response对象 
		try:
			response = urlopen(self.req)		
		except URLError as e:
			if hasattr(e,'reason'):
				#表示异常类型为URLError
				print('Failed to reach a server,Reason:\n' + str(e.reason))
			if hasattr(e,'code'):
				#表示异常类型为HTTPError，HTTPError为URLError的子类
				print('The server couldn\'t fulfill the request. Error_code:\n' + str(e.code))

			#设置代理 
			print('use proxy to re-open the url...')
			proxy_info = get_proxy_info()
			proxy_support = ProxyHandler({'http':proxy_info})
			opener = build_opener(proxy_support)
			opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54')]
			response = opener.open(self.req)		

		#response为gzip压缩过的。处理gzip压缩过的网页
		if response.info().get('Content-Encoding') == 'gzip':
			buf = BytesIO( response.read())
			f = gzip.GzipFile(fileobj=buf)
		else:
			f = response

		data = f.read().decode(self.decoding)

		return data

if __name__ == '__main__':
	url = 'http://www.tianqihoubao.com/aqi/shanghai-201312.html'
	url_object = url_report(url,'gbk')
	url_object.get_data()