from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://192.168.1.140:8443/CDGServer3/index.jsp')
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input').\
    send_keys('systemadmin')
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').send_keys('12345678')
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
driver.implicitly_wait(10)
# windows = driver.window_handles
# driver.switch_to.window(windows[-1])
# print(driver.current_url)
# driver.get_screenshot_as_file("E:\\test\\1.png")
driver.switch_to.frame('oa_left_middle')
driver.find_element_by_xpath('//*[@id="outlooktitle3"]/table/tbody/tr/td').click()
driver.find_element_by_xpath('//*[@id="outlookdivin3"]/span[1]/table/tbody/tr/td/a').click()
driver.switch_to.default_content()
driver.implicitly_wait(10)
driver.switch_to.frame('oa_main')
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="addPolicyInfoBtn"]/span/span').click()
driver.find_element_by_xpath('//*[@id="addPolicyInfoDialog"]/div[1]/div/div/form/div/fieldset/div/input[3]').send_keys('123')
driver.find_element_by_xpath('//*[@id="addPolicyInfoDialog"]/div[2]/a[1]/span/span').click()
driver.find_element_by_xpath('/html/body/div[13]/div[2]/div[4]/a/span/span').click()

