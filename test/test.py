import xlrd
from selenium import webdriver

work_book = xlrd.open_workbook('test.xlsx')
sheet = work_book.sheet_by_name('login_info')
value = sheet.row_values(0)
print(int(value[2]))
driver = webdriver.Chrome()
driver.get(value[0])
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input').send_keys(value[1])
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').\
    send_keys(int(value[2]))
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
