# test_param.py

import pytest


class TestParam:
    '''
    pytest参数化
        1. 在测试用例上加注解@pytest.mark.parametrize("loginame,password",[(值1，值2)，(值1，值2)])
        2. fixture传参。
         1)在测试用例上加注解@pytest.mark.parametrize("login_data",data2,indirect=True)
    login_data 是fixture函数
    @pytest.fixture()
    def login_data(request):
        return request.param
    测试用例取数据时用字典的方式取
        2)测试用例不用写注解，定义fixture函数时，fixture注解中传入参数 @pytest.fixture(params=data3)
    '''

    data = [("aaa", "e10adc3949ba59abbe56e057f20f883e"), ("aaaa", "bbb")]

    @pytest.mark.parametrize("loginame,password", data)
    # @pytest.mark.skip
    def test_login(self, loginame, password):
        print("用户名密码", loginame, 1, password)
        print("kkk")

    @pytest.fixture()
    def login_data(self, request):
        return request.param

    data2 = [{"loginame": "aaa", "password": "e10adc3949ba59abbe56e057f20f883e"}
        , {"loginame": "", "password": "1"}]

    @pytest.mark.parametrize("login_data", data2, indirect=True)
    # @pytest.mark.skip
    def test_login2(self, login_data):
        print(login_data, type(login_data))
        print("用户名密码", login_data.get("loginame"), 1, login_data.get("password"))

    data3 = [{"loginame": "aaa", "password": "e10adc3949ba59abbe56e057f20f883e"}
        , {"loginame": "", "password": "1"}]

    @pytest.fixture(params=data3)
    def login_data3(self, request):
        print(request)
        return request.param

    def test_login3(self, login_data3):
        print(login_data3)
        pass


if __name__ == '__main__':
    pytest.main(['-s', 'test1.py'])