import pymysql

data = {
    'id': '011',
    'name': 'bob',
    'age': 20
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'insert into {table}({keys}) values({values})'.format(table=table, keys=keys, values=values)
db = pymysql.connect(host='localhost', user='root', password='123456', db='spiders')
cursor = db.cursor()
try:
    cursor.execute(sql, tuple(data.values()))
    print('successful')
    db.commit()
except:
    print('failed')
    db.rollback()

db.close()
