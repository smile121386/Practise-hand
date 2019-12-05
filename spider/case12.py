import requests
import re


def get_one_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    reponse = requests.get(url, headers=headers)
    if reponse.status_code == 200:
        return reponse.text
    return None


def main(offset):
    url = 'http://www.cqvip.com/main/search.aspx?p='+str(offset)+'&k=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98%E6%8A%80%E6%9C%AF%E5%9C%A8%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B'
    name = '胡小华'
    html = str(get_one_page(url))
    print(html)
    # if name in html:
    #     print(url)
    # else:
    #     print('no')


# for i in range(10):
#     main(offset=i)
main(1)