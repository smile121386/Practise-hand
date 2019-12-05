# import requests
#
# data = {'name': 'germey', 'age': 22}
# r = requests.get('http://httpbin.org/get', params=data)
# print(type(r))
# print(r.json())
# print(type(r.json()))

# t = [1,2,3,4]
# print(t[0:4])

# content= 'Extra stings Hello 1234567 World This is a Regex Demo Extra stings'
# import re
# content = '''Extra stings Hello 1234567 World
# This is a Regex Demo Extra stings'''
# r = re.search('Hello.*?(\d+).*?Demo', content, re.S)
# print(r)
# print(r.group())
# print(r.group(1))

import re
html = '''<div id="songs-list" >
<h2 class ＝title ">经典老歌</h2>
<p class="introduction"> 经典老歌y1J
</p>
<ul id="list" class="list-group">
<li data-view="2 ">一路上有你</li>
<li data-view="7">
<a href ＝"/2.mp3 singer="任贤齐">沧海一卢笑</a>
</li>
<li data-view="4" class=" active">
<a href ＝"/ .mp3 singer="齐泰">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3 singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/S.mp3 singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href ＝"/6.mp3 singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''
# r = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(r)
# print(r.group(1), r.group(2))
r = re.findall('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
print(r)
for result in r:
    print("歌手：%s \t歌曲：%s" % (result[0], result[1]))

