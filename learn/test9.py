from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.implicitly_wait(10)
test_url = "https://192.168.1.139:8443/CDGServer3/index.jsp"
driver.get(test_url)
username = driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input')
username.send_keys("SystemAdmin")
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').send_keys('Est@2018')
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
driver.switch_to.frame("oa_left_middle")
driver.find_element_by_xpath('//*[@id="outlookdivin0"]/span[1]/table/tbody/tr/td/a').click()
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame("oa_main")
driver.switch_to.frame("frmUserList")
user = driver.find_element_by_xpath('//*[@id="createTypeCheck"]')
selector = Select(user)
selector.select_by_value('1')
time.sleep(2)
