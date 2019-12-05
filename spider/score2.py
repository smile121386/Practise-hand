import re
import openpyxl

with open('html.html', 'r', encoding='utf-8') as f:
    html = f.read()
pattern = re.compile('<tr(.*?)</tr>', re.S)
results = re.findall(pattern, html)
wb = openpyxl.Workbook('test.xlsx')
# sheet = wb.active
# ws1 = wb.create_sheet('my_sheet')
# ws2 = wb.get_sheet_by_name('my_sheet')

del results[0]
j = 0
b=[]
for i in results:

    p = re.compile('<td>(.*?)</td>', re.S)
    w = re.findall(p, i)
    if w[2] == '任选':
        pass
    else:
        # print('学科：%s，成绩：%s' % (w[4], w[8]))
        a = int(w[4]) * float(w[8])
        print(a)
        j = j + a
        print('j:%s' % j)


print(j)
