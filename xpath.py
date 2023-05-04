""" 
爬取某一本书的书名
"""
import requests
import lxml.etree


url = "https://book.douban.com/subject/4908885/"

user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"

header = {"user-agent": user_agent}


response = requests.get(url, headers=header)
selector = lxml.etree.HTML(response.text)
# selector.xpath('//*[@id="wrapper"]/h1/span') # 直接复制元素的xpath
name = selector.xpath('//*[@id="wrapper"]/h1/span/text()')

print(name)
