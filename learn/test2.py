from selenium import webdriver
import unittest
import test1
a = {1, 2, 'systemadmin'}
b = {1, 2, 12345678}


class Suite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.test_url = "https://192.168.1.140:8443/CDGServer3/index.jsp"
        cls.driver.get(cls.test_url)

    def test_login(self):
        for q in a:
            test1.LoginTest(q)
