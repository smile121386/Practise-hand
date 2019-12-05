from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('QQ')
# driver.find_element_by_xpath('//*[@id="su"]').click()
# windows = driver.window_handles
# driver.switch_to.window(windows[-1])
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="5"]/h3/a').click()
driver.get('https://192.168.1.128:8443/CDGServer3/index.jsp')
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input'). \
    send_keys("systemadmin")
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').send_keys("Est@2018")
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
windows = driver.window_handles
driver.switch_to.window(windows[-1])
time.sleep(2)
print(driver.current_url)
driver.find_element_by_xpath('//*[@id="outlooktitle1"]/table/tbody/tr/td').click()
