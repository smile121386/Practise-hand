import requests
import os
import random

from read_write_excel import read_excel_data

url = 'http://192.168.1.197:8081/sec-server/s/rs/uni'
path = 'qq.docx'
# filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 1, 1)
# parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=2)
# file_number, counsize_number, offset_number, return_flag = parameter_list[1:]


def check_file_number(path, file_number):
    if file_number == '1':
        filename = open(path, 'rb')
        file = filename.read()
        filename.close()
        return file
    elif file_number == '2':
        filename = open(path, 'r', encoding='UTF-8')
        file = filename.read()
        filename.close()
        return file
    elif file_number == '3':
        file = None
        return file


def check_counsize_number(counsize_number, filesize):
    if counsize_number == '1':
        file_counsize = str(filesize)
        return file_counsize
    elif counsize_number == '2':
        file_counsize = str(filesize + 1000000)
        return file_counsize
    elif counsize_number == '3':
        file_counsize = filesize
        return file_counsize
    elif counsize_number == '4':
        file_counsize = filesize
        return file_counsize
    elif counsize_number == '5':
        file_counsize = None
        return file_counsize


def check_offset_number(offset_number, last_number):
    if offset_number == '1':
        offset = '0'
        return offset
    elif offset_number == '2':
        offset = str(random.randrange(1, last_number))
        return offset
    elif offset_number == '3':
        offset = str(last_number)
        return offset
    elif offset_number == '4':
        offset = None
        return offset


def checkfile(url, path, file_number):
    file = check_file_number(path, file_number)
    data = {
        'method~name': 'checkFileIsEncryptionRest'

    }
    r = requests.post(url, headers=data, data=file)

    # print(r.headers)
    no = r.headers['data~returnFlag']
    # print(no)
    return no


def check_filename_number(path, filename_number):
    filename = path.split('\\')[-1]
    if filename_number == '1':
        name = filename
        return name
    elif filename_number == '2':
        name = filename.split('.')[0]
        return name
    elif filename_number == '3':
        name = 123
        return name
    elif filename_number == '4':
        name = None
        return name


# 文件加密
def encryption_file(url, path, file_number, counsize_number, offset_number):
    file = check_file_number(path, file_number)
    filesize = os.path.getsize(path)
    file_counsize = check_counsize_number(counsize_number, filesize)
    file_offset = check_offset_number(offset_number, filesize)
    # print(filesize)
    data = {
        'method~name': 'fileEncryptionRest',
        'data~counSize': file_counsize,
        'data~fileOffset': file_offset
    }
    r = requests.post(url, headers=data, data=file)

    no = r.headers['data~returnFlag']
    # print(no)
    with open(path, 'wb') as fd:
        fd.write(r.content)
    return no


# 文件解密
def decryption_file(url, path, file_number, counsize_number, offset_number):
    file = check_file_number(path, file_number)
    filesize = os.path.getsize(path)
    file_counsize = check_counsize_number(counsize_number, filesize)
    file_offset = check_offset_number(offset_number, filesize)
    data = {
        'method~name': 'fileDecryptionRest',
        'data~counSize': file_counsize,
        'data~fileOffset': file_offset
    }
    r = requests.post(url, headers=data, data=file)

    no = r.headers['data~returnFlag']
    # print(no)
    with open(path, 'wb') as fd:
        fd.write(r.content)
    return no


# 压缩包加密
def encryption_package(url, path, file_number, counsize_number, offset_number, filename_number):
    file = check_file_number(path, file_number)
    filesize = os.path.getsize(path)
    file_counsize = check_counsize_number(counsize_number, filesize)
    file_offset = check_offset_number(offset_number, filesize)
    name = check_filename_number(path, filename_number)
    data = {
        'method~name': 'filePackageEncrypttion',
        'data~fileSize': file_counsize,
        'data~fileName': name,
        'data~fileOffset': file_offset
    }
    r = requests.post(url, headers=data, data=file)
    no = r.headers['data~returnFlag']
    # print(no)
    with open(path, 'wb') as fd:
        fd.write(r.content)
    return no


# 压缩包解密
def decryption_package(url, path, file_number, counsize_number, offset_number, filename_number):
    file = check_file_number(path, file_number)
    filesize = os.path.getsize(path)
    file_counsize = check_counsize_number(counsize_number, filesize)
    file_offset = check_offset_number(offset_number, filesize)
    name = check_filename_number(path, filename_number)
    data = {
        'method~name': 'filePackageDecryption',
        'data~fileSize': file_counsize,
        'data~fileName': name,
        'data~fileOffset': file_offset
    }
    r = requests.post(url, headers=data, data=file)
    no = r.headers['data~returnFlag']
    # print(no)
    with open(path, 'wb') as fd:
        fd.write(r.content)
    return no


# encryption_file(url, path, '1', '1', '1')
