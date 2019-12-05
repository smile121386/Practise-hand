from selenium import webdriver
import time
import unittest
import login
import logout


class login_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.test_url = "https://192.168.1.140:8443/CDGServer3/index.jsp"

    def test_login(self):
        self.username = "SystemAdmin"
        self.passwd = "Est@2018"
        login.login(self)

    def test_logout(self):
        logout.logout(self)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
