import requests
from bs4 import BeautifulSoup
import re
from requests.exceptions import RequestException
from pyquery import PyQuery as pq

def get_page():
    url = 'https://www.gushiwen.org/gushi/tangshi.aspx'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求出错', url)
        return None

def parse_page(html):
    pattern = re.compile('<span><a href="(.*?)" target="_blank">(.*?)</a>(.*?)</span>',re.S)
    datas = re.findall(pattern, html)
    for data in datas:
        yield  data[0]

def get_detail_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求出错', url)
        return None

def parse_detail_page(html):
    pattern = re.compile('<h1 style=".*?">(.*?)</h1>', re.S)
    pattern1 = re.compile('<p class="source"><a href=.*?>(.*?)</a><span>(.*?)</span><a href=.*?>(.*?)</a>', re.S)
    pattern2 = re.compile('<div class="contson" id=.*?>(.*?)</div>', re.S)
    data = re.findall(pattern, html)
    data1 = re.findall(pattern1, html)[0]
    data2 = re.findall(pattern2, html)[0]
    data_ = "".join(data)
    data1_= "".join(data1)
    data2_ = str(data2).replace('<br />','\n')
    print(data_,'\n', data1_, data2_)


def main():
    html = get_page()
    for url in  parse_page(html):
        html = get_detail_page(url)
        data = parse_detail_page(html)
        print(data)



if __name__ == '__main__':
    main()
