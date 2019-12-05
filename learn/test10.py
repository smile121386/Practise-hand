import re
import requests
import json


def getAnser(qid, offset):
    # 利用知乎API请求json数据
    # qid:知乎问题号
    # offset:第几页

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    # 知乎API
    url = "https://www.zhihu.com/api/v4/questions/{}/answers?include=content&limit=10&offset={}&platform=desktop&sort_by=default".format(
        qid, offset)

    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    return res.text


def getBooksAndAnswers():
    # 获取所有书籍和回答数据
    offset = 0
    answerList = []  # 回答列表
    bookList = []  # 图书列表
    while True:
        qid = '35584877'
        print('Offset =', offset)
        # 知乎api请求
        html = getAnser(qid, offset)
        data = json.loads(html)
        if len(data['data'])==0:
            break
        for line in data['data']:
            # 保存回答数据
            answerList.append(line['content'])
        p = r'《(.*?)》'
        res = re.findall(p, html)
        for bookName in res:
            # 添加数据
            if bookName not in bookList and len(bookName)>1:
                bookList.append(bookName)
        offset += 10
    return answerList, bookList


def PopularBookStatistics(answerList, bookList):
    # 统计部分，根据爬取的图书进行二次搜索
    dic = {}
    f=open('book.txt','w+')
    for book in bookList:

        bookSum = 0
        for ans in answerList:
            if ans.find(book) > 0:
                bookSum += 1
        dic[book] = bookSum

    bookRank = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print('总书籍数量：', len(bookRank))
    for i in range(500):
        name = list(bookRank[i])[0]
        num = list(bookRank[i])[1]
        f.write('{} {}\n'.format(name,num))


if __name__ == '__main__':
    answerList, bookList = getBooksAndAnswers()
    PopularBookStatistics(answerList, bookList)
