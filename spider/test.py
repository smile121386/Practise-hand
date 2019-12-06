import requests


def post_url(user):
    a = []
    user = user
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
    url = 'https://s.weibo.com/weibo?q=%s&Refer=index'%user
    a.append(user)
    a.append(url)
    response = requests.get(url,headers=header)
    return response.text

print(post_url('张杰'))