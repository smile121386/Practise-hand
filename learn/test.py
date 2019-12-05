from selenium import webdriver
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.test_url = "https://192.168.1.140:8443/CDGServer3/index.jsp"

    def test_login(self):
        driver = self.driver
        driver.get(self.test_url)
        driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input').send_keys(
            'SystemAdmin')
        driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').send_keys(
            'Est@2018')
        driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
        driver.switch_to.frame('oa_main_top')
        home_page = driver.find_element_by_xpath('//*[@id="nav_middle"]/a/font')
        self.assertEqual(home_page.text, "主页")

    def test_strategic(self):
        driver = self.driver
        driver.switch_to.default_content()
        driver.implicitly_wait(10)
        driver.switch_to.frame('oa_left_middle')
        driver.find_element_by_xpath('//*[@id="outlooktitle3"]/table/tbody/tr/td').click()
        driver.find_element_by_xpath('//*[@id="outlookdivin3"]/span[1]/table/tbody/tr/td/a').click()
        driver.switch_to.default_content()
        driver.implicitly_wait(10)
        driver.switch_to.frame('oa_main')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="addPolicyInfoBtn"]/span/span').click()
        driver.find_element_by_xpath('//*[@id="addPolicyInfoDialog"]/div[1]/div/div/form/div/fieldset/div/input[3]').\
            send_keys('123')
        driver.find_element_by_xpath('//*[@id="addPolicyInfoDialog"]/div[2]/a[1]/span/span').click()
        tips = driver.find_element_by_xpath('/html/body/div[13]/div[2]/div[2]')
        self.assertEqual(tips.text, "操作成功")
        driver.find_element_by_xpath('/html/body/div[13]/div[2]/div[4]/a/span/span').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# def suite():
#     test_case = unittest.makeSuite(LoginTest, "test")
#     return test_case


if __name__ == "__main__":
    unittest.main()
