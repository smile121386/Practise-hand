import sys

import requests
from urllib import parse

url = "http://192.168.1.197:8081/sec-server/s/rs/uni"
a = r'水电/费'
src_path = parse.quote(a)
print(src_path.upper())

def encryption_file(url):
    # file = check_file_number(path, file_number)
    # filesize = os.path.getsize(path)
    # file_counsize = check_counsize_number(counsize_number, filesize)
    # file_offset = check_offset_number(offset_number, filesize)
    # print(filesize)
    src_path = parse.quote('smb://192.168.1.70/820/1.docx')
    print(src_path)
    data = {
        'method~name': 'cxCheckFileByPathRest',
        'data~srcPath': 'smb%3a%2f%2f192.168.1.70%2f820%2f1.docx',
        'data~srcUsername': '3e975e26c06cd594dea73a6684',
        'data~srcPassword': '359a5d28c560e6d19ef5'
    }
    r = requests.post(url, headers=data)

    no = r.headers['data~returnFlag']
    print(no)


print(encryption_file.__name__)
json = str({
    "Type": "1",
    "TimeSpan": "5",
    "ReadNum": "2",
    "bReadTimeLimited": "1",
    "BeginTime": "2015-05-27",
    "EndTime": "2015-05-31",
    "bPrint": "0",
    "bNetWork": "0",
    "bRevert": "0",
    "ReadOnly": "0",
    "PassWordText": "密码填写哈哈哈",
"WatermarkText": "水印内容填写哈哈",
"IsDelete":"0"
})
n = parse.quote(json)
print(n)
# %E6%B0%B4%E7%94%B5/%E8%B4%B9
# %E6%B0%B4%E7%94%B5%E8%B4%B9