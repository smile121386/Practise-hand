py2：import unittest #导入csv模块
from time import sleep
from selenium import webdriver
from JLR_CAL.fine import baidumodule
class baidu(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Chrome(r"E:\python\chromedriver.exe")
    #     self.driver.maximize_window()#最大化窗口
    #     self.driver.implicitly_wait(10)#隐式等待
    #     self.search = baidumodule(self.driver) #将driver传给aidumodule这个类
    #
    # def tearDown(self):
    #     self.driver.quit()

    @classmethod
    def setUpClass(cls):  # 类中最先执行
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()  # 最大化窗口
        cls.driver.implicitly_wait(10)  # 隐式等待
        cls.search = baidumodule(cls.driver)  # 将driver传给aidumodule这个类

    @classmethod
    def tearDownClass(cls):  # 类中最后执行
        cls.driver.quit()

    def test_search(self):
        search = self.search
        driver = self.driver
        search.login('selenium')
        sleep(1)
        title = driver.title
        self.assertEqual(title,'selenium_百度搜索')
        sleep(2)

    def test_search1(self):
        search = self.search
        driver = self.driver
        search.login('python')
        sleep(1)
        title = driver.title
        self.assertEqual(title,'python_百度搜索')
        sleep(2)

if __name__ == "__main__":
        unittest.main()
