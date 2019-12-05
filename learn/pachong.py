from urllib import request
from http import cookiejar


cookie_support = request.HTTPCookieProcessor(cookiejar.CookieJar())
opener = request.build_opener(cookie_support, request.HTTPHandler)
request.install_opener(opener)

content = request.urlopen('http://movie.douban.com/').read().decode('utf-8')
print(content)