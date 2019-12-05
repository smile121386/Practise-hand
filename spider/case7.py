import requests
import re


def get_one_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    reponse = requests.get(url, headers=headers)
    if reponse.status_code == 200:
        return reponse.text
    return None


def write_to_file(content):
    path = "./test.txt"
    with open(path, 'a', encoding='utf-8') as f:
        f.write(content)



def main(offset):
    url = 'https://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    # print(url)
    # print(html)
    re_title = re.compile('title="(.*?)"\s', re.S)
    re_rank = re.compile('<dd>.*?board-index-.*?">(.*?)</i>', re.S)
    get_name = re.findall(re_title, html)
    get_rank = re.findall(re_rank, html)
    title = get_name[::2]
    # print(get_rank)
    # print(get_rank, title)
    # print(title)
    i = 1
    while i <= 10:
        # print("第%s名:%s" % (get_rank[i-1], title[i-1]))
        content = "第%s名:%s\n" % (get_rank[i-1], title[i-1])
        write_to_file(content)
        i += 1

for i in range(10):
    main(offset=10 * i)
