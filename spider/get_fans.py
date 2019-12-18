import re

import requests

users = ['胡歌', '张杰', '肖战', '谢娜']


def get_text(user):
    url = 'https://s.weibo.com/weibo?q=%s&Refer=index' % user
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
    response = requests.get(url, headers=header)
    return response.text


def get_fans(input_user):
    re_rule = re.compile('<span>.*?粉丝.*?user_fans">(.*?)</a>', re.S)
    results = re.findall(re_rule, get_text(input_user))
    return results[0]


for i in users:
    print('%s的粉丝数为%s' % (i, get_fans(i)))
