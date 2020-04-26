from selenium import webdriver
import time
import pyautogui
from Read_Excel import *


def find_fracas(driver, number, i):
    driver.find_element_by_xpath('//*[@id="quickSearchInput"]').send_keys(number)
    time.sleep(2)
    pyautogui.press('enter')
    edition = driver.find_element_by_xpath('//*[@id="customfield_10022-val"]').text
    write_excel(i, edition)
    time.sleep(2)


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://fracas.esafenet.com:8080/login.jsp')
driver.find_element_by_xpath('//*[@id="login-form-username"]').send_keys('yangxc')
driver.find_element_by_xpath('//*[@id="login-form-password"]').send_keys('yangxc0711~')
driver.find_element_by_xpath('//*[@id="login-form-submit"]').click()
time.sleep(10)
try:
    driver.find_element_by_xpath('//*[@id="whats-new-dialog"]/div/div[2]/a').click()
except:
    pass
a = 1
for i in read_test_data():
    find_fracas(driver, i, a)
    a += 1
