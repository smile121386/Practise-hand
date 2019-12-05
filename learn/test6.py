from selenium import webdriver
import time
import unittest

from selenium.webdriver.common.keys import Keys


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.test_url = "http://admin:admin@192.168.1.236:8888/"

    def test_login(self):
        driver = self.driver
        driver.get(self.test_url)
        driver.find_element_by_xpath('//*[@id="files"]/tbody/tr[3]/td[1]/a').click()
        # driver.switch_to.alert.authenticate('admin', 'admin')
        driver.implicitly_wait(2)
        driver.find_element_by_xpath('//*[@id="files"]/tbody/tr[2]/td[1]/a').click()
        driver.implicitly_wait(2)
        driver.find_element_by_xpath('//*[@id="files"]/tbody/tr[5]/td[1]/a').click()
        driver.implicitly_wait(2)
        for i in range(1, 100):
            driver.find_element_by_xpath('//*[@id="files"]/tbody/tr[4]/td[1]/a').click()
            # time.sleep(20)
            js = " window.open('chrome://settings/privacy')"
            driver.execute_script(js)

            time.sleep(2)

            handles = driver.window_handles
            driver.switch_to.window(handles[-1])
            driver.find_element_by_xpath('//*[@id="clearBrowsingDataTrigger"]').click()
            driver.find_element_by_xpath('//*[@id="clearBrowsingDataConfirm"]').click()
            driver.close()
            driver.switch_to.window(1)






# def suite():
#     test_case = unittest.makeSuite(LoginTest, "test")
#     return test_case


if __name__ == "__main__":
    unittest.main()
