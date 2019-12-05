import time
import pyautogui


def login(self):
    driver = self.driver
    driver.get(self.test_url)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input').send_keys(
        self.username)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').send_keys(
        self.passwd)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
    driver.switch_to.frame('oa_main_top')
    home_page = driver.find_element_by_xpath('//*[@id="nav_middle"]/a/font')
    self.assertEqual(home_page.text, "主页")
    time.sleep(5)
    # pyautogui.press("enter")
