import requests
import os

url = 'http://192.168.1.41:8081/sec-server/s/rs/uni'
path = 'qq.rar'


def checkfile(url, path):
    # url = 'http://192.168.1.79:8080/sec-server/s/rs/uni'
    filename = open(path, 'rb')
    file = filename.read()
    filename.close()
    # print(file)
    data = {
        'method~name': 'checkFileIsEncryptionRest'

    }
    r = requests.post(url, headers=data, data=file)

    # print(r.headers)
    no = r.headers['data~returnFlag']
    return no
    # if no == '0':
    #     print('上传的文件是明文')
    # elif no == '1':
    #     print('上传的文件是密文')
    # else:
    #     print('出错')


# 文件加密
def encryption_file(url, path):
    filename = open(path, 'rb')
    file = filename.read()
    filename.close()
    # print(file)
    filesize = os.path.getsize(path)
    print(filesize)
    data = {
        'method~name': 'fileEncryptionRest',
        'data~counSize': str(filesize),
        'data~fileOffset': '0'
    }
    r = requests.post(url, headers=data, data=file)

    no = r.headers['data~returnFlag']
    # print(r.content)
    with open(path, 'wb') as fd:
        fd.write(r.content)
    return no
    # word = docx.Document()
    # print(type(r.content))
    # word.add_paragraph(r.text)
    # word.save('qq.docx')


# 文件解密
def decryption_file(url, path):
    filename = open(path, 'rb')
    file = filename.read()
    filename.close()
    # print(file)
    filesize = os.path.getsize(path)
    # print(filesize)
    data = {
        'method~name': 'fileDecryptionRest',
        'data~counSize': str(filesize),
        'data~fileOffset': '0'
    }
    r = requests.post(url, headers=data, data=file)

    no = r.headers['data~returnFlag']
    # print(r.content)

    with open(path, 'wb') as fd:
        fd.write(r.content)
    return no


# 压缩包加密
def encryption_package(url, path):
    filename = open(path, 'rb')
    file = filename.read()
    filename.close()
    filesize = os.path.getsize(path)
    name = path.split('\\')[-1]
    data = {
        'method~name': 'filePackageEncrypttion',
        'data~fileSize': str(filesize),
        'data~fileName': name,
        'data~fileOffset': '0'
    }
    r = requests.post(url, headers=data, data=file)
    no = r.headers['data~returnFlag']
    print(no)
    with open(path, 'wb') as fd:
        fd.write(r.content)
    # return no


# 压缩包解密
def decryption_package(url, path):
    filename = open(path, 'rb')
    file = filename.read()
    filename.close()
    filesize = os.path.getsize(path)
    name = path.split('\\')[-1]
    data = {
        'method~name': 'filePackageDecryption',
        'data~fileSize': str(filesize),
        'data~fileName': name,
        'data~fileOffset': '0'
    }
    r = requests.post(url, headers=data, data=file)
    no = r.headers['data~returnFlag']
    print(no)
    with open(path, 'wb') as fd:
        fd.write(r.content)


decryption_package(url, path)
