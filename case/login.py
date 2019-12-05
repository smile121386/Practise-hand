# from selenium import webdriver
import time
import csv


# def fun(us="systemadmin", pw="Est@2018"):
# #     return us, pw
# #
# #
# # username, password = fun()
# # print(username, password)


# file_info = open("C:\\Users\\Administrator\\Desktop\\test.txt", "r")
# values = file_info.readlines()
# file_info.close()
# print(values)
# for items in values:
#     # data1 = items.split(',')[0]
#     # data2 = items.split(',')[1]
#     data = items.split(',')
#     print(data)
# #     print(data1, data2)
#     print(data[0])
# username, password = data[0]
# print(username, password)

users = []
pw = []
my_file = "C:\\Users\\Administrator\\Desktop\\test.csv"
data = csv.reader(open(my_file, "r"))
for items in data:
    name = items[0]
    p = items[1]
    users.append(name)
    pw.append(p)
print(users)
print(pw)

username = users[0]
password = pw[0]
print(username, password)
# print(items[1])
# username = items[0]
# print(username)


def test_login(self):
    driver = self.driver
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input').\
        send_keys(username)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').\
        send_keys(password)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
    time.sleep(3)
