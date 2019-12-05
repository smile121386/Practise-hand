from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://192.168.1.128:8443/CDGServer3/index.jsp")
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input').\
    send_keys("systemadmin")
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').send_keys("Est@2018")
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
window = driver.current_window_handle
time.sleep(3)
driver.find_element_by_xpath('//*[@id="outlookdivin0"]/span[2]/table/tbody/tr/td/a').click()
# login_name = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table/tbody/tr/td[1]/span[2]').text
# login_name = login_name.strip('欢迎：')
# print(login_name)
# if login_name == "系统管理员(SystemAdmin)":
#     print('登录成功')
# else:
#     print('登录失败')

# driver.get("https://www.baidu.com")
# driver.find_element_by_css_selector('#kw').send_keys('123')