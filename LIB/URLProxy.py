# -*- coding: utf-8 -*-  
'''
get Proxy IP
'''
import os,re
from bs4 import BeautifulSoup
from urllib.request import Request,urlopen,ProxyHandler,build_opener,install_opener

def get_proxy_info():
	# use urllib to get html data
	url = 'http://www.xicidaili.com/nn/1'
	#url = 'http://www.baidu.com'
	req = Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240')
	response = urlopen(req)
	html_data = response.read().decode('utf-8')
	#html_data = response.read()
	#print(html_data)

	# use BeautifulSoup to parse html data
	soup = BeautifulSoup(html_data,'html.parser')

	#for line in soup.table.findall('')
	all_tr = soup.select("#ip_list tr")
	#select id=iplist 的标签下的所有tr标签(空格 是后代选择器). all_tr 是一个列表。

	i=0
	for each_tr in all_tr:
		#print(each_tr)
		all_td = each_tr.select('td')
		if all_td == []:
			continue
		
		ip = all_td[1].string
		port = all_td[2].string
		#print('Host: %s  %s' % (str(ip),str(port)))

		# check whether the proxy is available

		#proxy_info = str(ip).strip() + ':' + str(port).strip()
		proxy_info = '135.245.48.34:8000'

		proxy_support = ProxyHandler({'http':proxy_info})
		opener = build_opener(proxy_support)
		#opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54')]
		try:
			response = opener.open('http://icanhazip.com')
			if response.getcode() == 200 :
				print(proxy_info)
				break			
			else:
				print("%s is not available. error: " % (proxy_info,str(response.getcode())))	
		except Exception as e:
			print("%s is not available. error: " % (proxy_info,e))

	return proxy_info
	
if __name__ == '__main__':
	get_proxy_info()




