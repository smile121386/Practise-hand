from selenium import webdriver


# a = {'1': 'admin', '2': 'abc'}
# a={'1', '2', '3'}
class LoginTest:
    def login_test(self,username, password):
        return username, password
        print(username, password)
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get('https://192.168.1.140:8443/CDGServer3/index.jsp')
        driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input').send_keys(username)
        driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').send_keys(password)
        driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
        driver.switch_to.alert.accept()
        # driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input').clear()
        # driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').clear()


my_login = LoginTest()
my_login.login_test(123456, 12345678)
# for k, v in a.items():
#     print(k, v)
# my_login = LoginTest()
# print(my_login.login_test(123, 12345678))
# print(LoginTest.login_test(123, 12345678, 12345678))
# my_login = LoginTest()
# print(my_login.login_test(123, 12345678))