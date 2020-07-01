# class MyClass:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def info(self):
#         print("学生：%s； 分数：%s"%(self.name, self.score))
#
#     def get_score(self):
#         return self.score
#
#     def set_score(self, score):
#         if score >= 0 and score <= 100:
#             self.score = score
#             return self.score
#         else:
#             print("请输入0-100")
#
# my_class = MyClass('xiaomeng', 90)
# my_class.info()
# my_class.set_score(101)
# my_class.info()

import unittest
from test2 import *
from HTMLTestRunner import HTMLTestRunner


class est_interface(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://192.168.1.41:8081/sec-server/s/rs/uni'
        self.path = 'qq.docx'
        self.encryption_path = 'qq1.docx'

    def test_checkfile(self):
        code = checkfile(self.url, self.path)
        self.assertEqual(code, '0')

    def test_check_encryptionfile(self):
        code = checkfile(self.url, self.encryption_path)
        self.assertEqual(code, '1')

    def test_encryption_file(self):
        code = encryption_file(self.url, self.path)
        self.assertEqual(code, '0')

    def test_decryption_file(self):
        code = decryption_file(self.url, self.encryption_path)
        self.assertEqual(code, '0')


def suite():
    loginTestCase = unittest.makeSuite(est_interface, 'test')
    return loginTestCase


if __name__ == '__main__':
    with open('report.html', 'wb')as fb:
        test_run = HTMLTestRunner.HTMLTestRunner(stream=fb,
                                                 verbosity=2,
                                                 title='测试报告',  # 定义测试报告的标题
                                                 description='...')
        test_run.run(suite())
