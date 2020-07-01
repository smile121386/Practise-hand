import unittest
from interface_module import *
from HTMLTestRunner import HTMLTestRunner
from read_write_excel import *


class est_interface(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://192.168.1.197:8081/sec-server/s/rs/uni'
        self.path = 'qq.docx'
        self.encryption_path = 'qq1.docx'
        self.empty_path = 'qq2.docx'

    def test_checkfile1(self):
        file_number = str(read_excel_data('CDG_API_Test.xlsx', 'checkFileIsEncryptionRest', 2, 2))
        code = checkfile(self.url, self.path, file_number)
        self.assertEqual(code, '0')

    def test_checkfile2(self):
        file_number = str(read_excel_data('CDG_API_Test.xlsx', 'checkFileIsEncryptionRest', 3, 2))
        code = checkfile(self.url, self.path, file_number)
        self.assertEqual(code, '0')

    def test_checkfile3(self):
        file_number = str(read_excel_data('CDG_API_Test.xlsx', 'checkFileIsEncryptionRest', 4, 2))
        code = checkfile(self.url, self.path, file_number)
        self.assertNotEqual(code, '0')

    def test_check_encryptionfile(self):
        code = checkfile(self.url, self.encryption_path, '1')
        self.assertEqual(code, '1')

    def test_check_emptyfile(self):
        code = checkfile(self.url, self.empty_path, '1')
        self.assertNotEqual(code, '0')

    def test_encryption_file1(self):
        filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 1, 1)
        parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=2)
        file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
        code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
        self.assertEqual(code, str(return_flag))

    def test_encryption_file2(self):
        filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 2, 1)
        parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=3)
        file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
        code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
        self.assertEqual(code, str(return_flag))

    def test_encryption_file3(self):
        filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 3, 1)
        parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=4)
        file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
        code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
        self.assertEqual(code, str(return_flag))

    def test_encryption_file4(self):
        filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 4, 1)
        parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=5)
        file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
        code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
        self.assertEqual(code, str(return_flag))

    def test_encryption_file5(self):
        filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 5, 1)
        parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=6)
        file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
        code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
        self.assertEqual(code, str(return_flag))

    # def test_encryption_file6(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 6, 1)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=7)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_encryption_file7(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 7, 1)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=8)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_encryption_file8(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 8, 1)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=9)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_encryption_file9(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 9, 1)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=10)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_encryption_file10(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 10, 1)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=11)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_encryption_file11(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 11, 1)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=12)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_encryption_file12(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 12, 1)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=13)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_encryption_file13(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 13, 1)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=14)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_encryption_file14(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 14, 1)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=15)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_encryption_file15(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 15, 1)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileEncryptionRest', row_number=16)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = encryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))

    def test_decryption_file1(self):
        filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 1, 2)
        parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=2)
        file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
        code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
        self.assertEqual(code, str(return_flag))

    def test_decryption_file2(self):
        filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 2, 2)
        parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=3)
        file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
        code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
        self.assertEqual(code, str(return_flag))

    def test_decryption_file3(self):
        filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 3, 2)
        parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=4)
        file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
        code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
        self.assertEqual(code, str(return_flag))

    def test_decryption_file4(self):
        filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 4, 2)
        parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=5)
        file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
        code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
        self.assertEqual(code, str(return_flag))

    def test_decryption_file5(self):
        filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 5, 2)
        parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=6)
        file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
        code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
        self.assertEqual(code, str(return_flag))

    # def test_decryption_file6(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 6, 2)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=7)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_decryption_file7(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 7, 2)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=8)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_decryption_file8(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 8, 2)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=9)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_decryption_file9(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 9, 2)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=10)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_decryption_file10(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 10, 2)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=11)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_decryption_file11(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 11, 2)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=12)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_decryption_file12(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 12, 2)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=13)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_decryption_file13(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 13, 2)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=14)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_decryption_file14(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 14, 2)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=15)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))
    #
    # def test_decryption_file15(self):
    #     filepath = read_excel_data('CDG_API_Test.xlsx', 'filepath', 15, 2)
    #     parameter_list = read_excel_data('CDG_API_Test.xlsx', 'fileDecryptionRest', row_number=16)
    #     file_number, counsize_number, offset_number, return_flag = parameter_list[1:]
    #     code = decryption_file(self.url, filepath, str(file_number), str(counsize_number), str(offset_number))
    #     self.assertEqual(code, str(return_flag))

def suite():
    loginTestCase = unittest.makeSuite(est_interface, 'test')
    # loginTestCase.addTest(est_interface('test_checkfile1'))
    # loginTestCase.addTest(est_interface('test_checkfile2'))
    # loginTestCase.addTest(est_interface('test_checkfile3'))
    # loginTestCase.addTest(est_interface('test_check_encryptionfile'))
    # loginTestCase.addTest(est_interface('test_check_emptyfile'))
    # loginTestCase.addTest(est_interface('test_encryption_file'))
    # loginTestCase.addTest(est_interface('test_decryption_file'))
    return loginTestCase


if __name__ == '__main__':
    with open('report.html', 'wb') as fb:
        test_run = HTMLTestRunner.HTMLTestRunner(stream=fb,
                                                 verbosity=2,
                                                 title='测试报告',  # 定义测试报告的标题
                                                 description='...')
        test_run.run(suite())
