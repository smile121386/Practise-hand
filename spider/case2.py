# import urllib.parse
# import urllib.request
#
#
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
#
# resutls = str(response.read()).split("\\n")
# for result in resutls:
#     print(result)

import re
html = '''s<li data-view="6"><a href="/4.mp3 singer="beyond">光辉岁月</a></li>
<li data-view="6"><a href="/4.mp3 singer="beyond">光辉</a></li>'''
r = re.findall('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
print(r)
print(type(r))
for result in r:
    print(result)
    print(result[0], result[1])
