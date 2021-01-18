import os

import pytest


b = 'bbb'


@pytest.fixture(scope='class')
def test_start():
    print('------------start-----------')


@pytest.fixture(scope='class')
def test_0():
    print('-------------0------------')


@pytest.mark.usefixtures("test_0")
@pytest.mark.usefixtures("test_start")
class TestCase(object):
    def setup_class(self):
        self.a = 1
        print('--------aaaa------')

    def test_1(self):
        print('----------1--------')
        # print('a:{0}'.format(self.a))

    @pytest.mark.parametrize('b_parame', [b])
    def test_2(self, b_parame):
        print('------------------{0}-------------'.format(b_parame))
        print('--------2-----------')

    def teardown_method(self):
        print('------------0000------------')


@pytest.fixture(scope='module', autouse=True)
def test_end():
    print('--------------end--------------')


class TestCase1(object):
    @pytest.mark.parametrize('b_parame', [b])
    def test_1(self, b_parame):
        print('------------------{0}-------------'.format(b_parame))
        print('-------------testcase1------------')


if __name__ == "__main__":
    pytest.main(['-s', '-p', 'no:warnings', 'test2.py'])
    # pytest.main(["-s", "--alluredir=report\\test", "test2.py"])
    # os.system("allure serve report/test")
