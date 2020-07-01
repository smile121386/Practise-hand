from selenium import webdriver
import time
from read_write_excel import *
from login import *


def approval(driver, username, password):
    driver.find_element_by_xpath('//*[@id="login_img"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
    time.sleep(1)
    oa_left_middle = driver.find_element_by_xpath('//*[@id="oa_left_middle"]')
    driver.switch_to.frame(oa_left_middle)
    driver.find_element_by_xpath('//*[@id="outlookdivin0"]/span[1]/table/tbody/tr/td/a').click()
    time.sleep(1)
    driver.switch_to.default_content()
    oa_main = driver.find_element_by_xpath('//*[@id="oa_main"]')
    driver.switch_to.frame(oa_main)
    driver.find_element_by_xpath('//*[@id="check"]').click()
    time.sleep(1)
    tbody = driver.find_element_by_xpath('//*[@id="myForm"]/table[2]/tbody')
    trs_list = tbody.find_elements_by_tag_name('tr')
    execute = trs_list[-1].find_elements_by_tag_name('input')[0]
    execute.click()
    time.sleep(1)
    try:
        driver.switch_to.alert.accept()
        time.sleep(1)
    except:
        pass
    driver.switch_to.default_content()
    oa_main_top = driver.find_element_by_xpath('//*[@id="oa_main_top"]')
    driver.switch_to.frame(oa_main_top)
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table/tbody/tr/td[4]/a/span[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[2]/img').click()


def approval_all_flow(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    for user_list in read_excel_data('test_data.xlsx', 'approver_list'):
        for user in user_list:
            username = '%s.local' % user
            password = read_test_data('login_data')[-1][2]
            approval(driver, username, password)


if __name__ == '__main__':
    approval_all_flow(read_test_data('login_data')[-1][0])
