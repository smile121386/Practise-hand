from selenium import webdriver
import unittest
import login


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.test_url = "https://192.168.1.140:8443/CDGServer3/index.jsp"
        self.driver.get(self.test_url)

    def test_login(self):
        login.test_login(self)

    def tearDown(self):
        self.driver.quit()


def suite():
    login_test_case = unittest.TestCase()
    login_test_case.addTest(Login("test_login"))


if __name__ == "__main__":
    unittest.main()
