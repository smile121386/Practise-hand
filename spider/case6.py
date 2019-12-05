import requests
import re


def get_one_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    reponse = requests.get(url, headers=headers)
    if reponse.status_code == 200:
        return reponse.text
    return None


def main():
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    # print(html)
    get_title = re.compile('title="(.*?)"\s', re.S)
    get_data = re.findall(get_title, html)
    title = get_data[::2]
    # print(title)
    i = 1
    while i <=10:
        print("第%d名:%s" % (i, title[i-1]))
        i += 1


main()
