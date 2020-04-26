from time import sleep
from configparser import ConfigParser
from selenium.webdriver.support.ui import Select


def get_clientID():
    cfg = ConfigParser()
    cfg.read(r'C:\Users\Administrator\Desktop\UniqueClientCode.ini')
    return cfg.get('ClientUnique', 'ClientIDID')


def export_offline_policy(driver, user):
    oa_left_middle = driver.find_element_by_xpath('//*[@id="oa_left_middle"]')
    driver.switch_to.frame(oa_left_middle)
    organization_management = driver.find_element_by_xpath('//*[@id="outlooktitle0"]/table/tbody/tr/td')
    organization_management.click()
    sleep(2)
    user_management = driver.find_element_by_xpath('//*[@id="outlookdivin0"]/span[1]/table/tbody/tr/td/a')
    user_management.click()
    sleep(2)
    driver.switch_to.default_content()
    oa_main = driver.find_element_by_xpath('//*[@id="oa_main"]')
    driver.switch_to.frame(oa_main)
    frmUserList = driver.find_element_by_xpath('//*[@id="frmUserList"]')
    driver.switch_to.frame(frmUserList)
    sleep(2)
    username_search = driver.find_element_by_xpath('//*[@id="userId"]')
    username_search.send_keys(user)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="search"]').click()
    sleep(2)
    user_management_tbody = driver.find_element_by_xpath('//*[@id="tbUserList"]/tbody')
    user_management_trs = user_management_tbody.find_elements_by_tag_name('tr')
    for tr in user_management_trs[0:-1]:
        userid = tr.find_element_by_xpath('./td[3]').text
        if userid == user:
            tr.find_element_by_xpath('./td[last()]/a').click()
            sleep(2)
            break
        else:
            pass
    export_policy_button = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[12]/td[2]/input[3]')
    export_policy_button.click()
    sleep(2)
    Select(driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[1]/td[2]/select')).\
        select_by_visible_text('离线客户端策略')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="passWord"]').send_keys('Admin@123')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="rePassWord"]').send_keys('Admin@123')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="uDiskId"]').send_keys(get_clientID())
    sleep(2)
    driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[10]/td[2]/input[2]').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[11]/td/input[1]').click()
    sleep(2)
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    sleep(10)
