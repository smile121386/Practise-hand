from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://pm.esafenet.com:8090/login')
driver.find_element_by_xpath('//*[@id="username"]').send_keys('kongshanshan')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('kongshanshan123')
driver.find_element_by_xpath('//*[@id="login-submit"]').click()
driver.find_element_by_xpath('//*[@id="project-jump"]/span').click()
# driver.find_element_by_xpath('//*[@id="projects-quick-search"]').send_keys('CDG 小项目内部测试')
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="project-jump"]/div/div[2]/a/span').click()
ul = driver.find_element_by_xpath('//*[@id="project-jump"]/span')
ul.find_element_by_xpath('//*[@id="project-jump"]/div/div[2]/a[8]/span').click()
driver.find_element_by_xpath('//*[@id="main-menu"]/ul/li[5]/a').click()
driver.find_element_by_xpath('//*[@id="content"]/div[1]/a').click()
Select(driver.find_element_by_xpath('//*[@id="issue_assigned_to_id"]')).select_by_visible_text('<< 我 >>')
Select(driver.find_element_by_xpath('//*[@id="issue_custom_field_values_41"]')).select_by_visible_text('CDG_820_changxin')
Select(driver.find_element_by_xpath('//*[@id="issue_custom_field_values_42"]')).select_by_visible_text('功能测试')
Select(driver.find_element_by_xpath('//*[@id="issue_custom_field_values_60"]')).select_by_visible_text('win7-64bit-旗舰')
Select(driver.find_element_by_xpath('//*[@id="issue_custom_field_values_1"]')).select_by_visible_text('严重')
Select(driver.find_element_by_xpath('//*[@id="issue_custom_field_values_5"]')).select_by_visible_text('新需求引入')