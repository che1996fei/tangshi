import requests
import re
from requests.exceptions import RequestException


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
    data = re.findall('<h1 style=".*?">(.*?)</h1>', html, re.S)
    data1 = re.findall('<p class="source"><a href=.*?>(.*?)</a><span>(.*?)</span><a href=.*?>(.*?)</a>', html, re.S)
    if data1:
        data1 = data1[0]
    else:
        data1 = ""
    data2 = re.findall('<div class="contson" id=.*?>(.*?)</div>', html, re.S)
    if data2:
        data2 = data2[0]
    else:
        data2 = ""
    data3 = re.findall('<p><strong>(.*?)</strong>(.*?)</p>', html, re.S)
    if data3:
        data3 = data3[0][1]
    else:
        data3 = ""
    data4 = re.findall('<p style=" margin:0px;">(.*?)<a href=".*?>►.*?</a></p', html, re.S)
    if data4:
        data4 = data4[0]
    else:
        data4 = ""
    name = "".join(data)
    author= "".join(data1)
    content = str(data2).replace('<br />','\n')
    translation = data3.replace('<br />', ' ')
    author_life = "".join(data4)
    file = open('tangshi.txt', 'a', encoding='utf-8')
    file.write(name + '\n' + author + content + "译文：" + translation + '\n' + "作者：" + author_life)
    file.write('\n' + '=' * 50 + '\n')
    print("输出chengg")
    file.close()



def main():
    html = get_page()
    for url in  parse_page(html):
        html = get_detail_page(url)
        parse_detail_page(html)




if __name__ == '__main__':
    main()
