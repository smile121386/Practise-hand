import re

import requests


def post_url(user):
    a = []
    user = user
    url = 'https://s.weibo.com/weibo?q=%s&Refer=index' % user

    return url


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}


def get_text(input_user):
    response = requests.get(post_url(input_user), headers=header)
    return response.text


def re_match(input_user):
    re_match = re.compile('<span>.*?粉丝.*?user_fans">(.*?)</a>', re.S)
    results = re.findall(re_match, get_text(input_user))
    return results[0]


users = ['胡歌', '张杰', '肖战']
for i in users:
    print('%s的粉丝数为%s' % (i, re_match(i)))
