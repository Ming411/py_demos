import requests

# 对html进行解析
from bs4 import BeautifulSoup as bs


def get_url_name(myurl):
    # user_agent 是为了模拟浏览器的请求头，如果不设置网站有反爬虫机制
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    header = {}
    header["user-agent"] = user_agent
    url = myurl
    # url = "https://book.douban.com/top250"
    response = requests.get(url, headers=header)

    # print(response)
    # print(response.text)  # 完整的网页

    bs_info = bs(response.text, "html.parser")
    # ret = bs_info.findAll("div", attrs={"class": "pl2"})[0]
    # print(ret)

    for tags in bs_info.findAll("div", attrs={"class": "pl2"}):
        # print(tags)
        for atags in tags.findAll("a"):
            print(atags.get_text())  # a 标签中的文本
            print(atags.get("href"))


# 1~9
# f-string 格式化字符串
urls = tuple(f"https://book.douban.com/top250?start={page*25}" for page in range(10))
from time import sleep

# 如果请求时间过短会导致被封,sleep间隔时间
for page in urls:
    get_url_name(page)
    sleep(5)
