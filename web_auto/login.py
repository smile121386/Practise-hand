from selenium import webdriver
import time
from read_excel import read_login_data
from datetime import datetime


def login(driver, url, username, password):
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="login_img"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
    time.sleep(1)


def entry_organization_and_management(driver):
    oa_left_middle = driver.find_element_by_xpath('//*[@id="oa_left_middle"]')
    driver.switch_to.frame(oa_left_middle)
    driver.find_element_by_xpath('//*[@id="outlooktitle0"]/table/tbody/tr/td').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="outlookdivin0"]/span[1]/table/tbody/tr/td/a').click()
    time.sleep(1)
    driver.switch_to.default_content()
    oa_main = driver.find_element_by_xpath('//*[@id="oa_main"]')
    driver.switch_to.frame(oa_main)


def return_homepage(driver):
    driver.switch_to.default_content()
    oa_main_top = driver.find_element_by_xpath('//*[@id="oa_main_top"]')
    driver.switch_to.frame(oa_main_top)
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table/tbody/tr/td[2]/a/span[1]').click()
    time.sleep(1)
    driver.switch_to.default_content()


def create_organization(driver, organization_name):
    entry_organization_and_management(driver)
    driver.find_element_by_xpath('//*[@id="0_span"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="create"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="groupName"]').send_keys(organization_name)
    driver.find_element_by_xpath('//*[@id="btnSave"]').click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    return_homepage(driver)


def create_user(driver, organization_name):
    entry_organization_and_management(driver)
    driver.find_element_by_xpath('//*[@id="0_switch"]').click()
    time.sleep(1)
    list_organization = driver.find_element_by_xpath('//*[@id="0_ul"]')
    lis = list_organization.find_elements_by_tag_name('li')
    for li in lis:
        id = li.find_elements_by_tag_name('span')
        if id[0].text == organization_name:
            id[0].click()
            break
        else:
            pass
    user_list_frame = driver.find_element_by_xpath('//*[@id="frmUserList"]')
    driver.switch_to.frame(user_list_frame)
    user_list = []
    for i in range(3):
        driver.find_element_by_xpath('//*[@id="tbUserList"]/thead[2]/tr/td/input[3]').click()
        time.sleep(1)
        now_time = datetime.now()
        now_time_str = now_time.strftime('%m%d%H%M%S')
        add_user = 'cs%s' % now_time_str
        driver.find_element_by_xpath('//*[@id="userName"]').send_keys(add_user)
        driver.find_element_by_xpath('//*[@id="surName"]').send_keys(add_user)
        driver.find_element_by_xpath('//*[@id="btnSave"]').click()
        time.sleep(2)
        user_list.append(add_user)
    return_homepage(driver)
    return user_list


def add_approver(driver, user_list):
    oa_left_middle = driver.find_element_by_xpath('//*[@id="oa_left_middle"]')
    driver.switch_to.frame(oa_left_middle)
    driver.find_element_by_xpath('//*[@id="outlooktitle6"]/table/tbody/tr/td').click()
    driver.find_element_by_xpath('//*[@id="outlookdivin6"]/span[2]/table/tbody/tr/td/a').click()
    time.sleep(1)
    driver.switch_to.default_content()
    oa_main = driver.find_element_by_xpath('//*[@id="oa_main"]')
    driver.switch_to.frame(oa_main)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[6]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="bn1"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="myForm"]/table[2]/tbody/tr[3]/td/input[2]').click()
    time.sleep(1)
    treeValue1 = driver.find_element_by_xpath('//*[@id="treeValue1"]')
    driver.switch_to.frame(treeValue1)
    for i in user_list:
        driver.find_element_by_xpath('//*[@id="userName"]').send_keys(i)
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[2]/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/p/input[3]').click()
        time.sleep(1)
    driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/input[1]').click()
    time.sleep(2)
    driver.switch_to.default_content()
    oa_main = driver.find_element_by_xpath('//*[@id="oa_main"]')
    driver.switch_to.frame(oa_main)
    for i in range(1, 5):
        driver.find_element_by_xpath('//*[@id="myForm"]/table[2]/tbody/tr[%s]/td[5]/a[2]' % i).click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="selectGroupList"]/ul/li/div/span[1]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="selectGroupList"]/ul/li/div/span[3]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="save_template_group"]/span/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[16]/div[2]/div[3]/a/span/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="setApprovalUser_range_groupListDialog"]/div[2]/a/span/span').click()
        


def all_test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    login(driver, read_login_data()[0], read_login_data()[1], read_login_data()[2])
    organization_list = ['审批组1', '审批组2', '审批组3']
    users_list = []
    for i in organization_list:
        create_organization(driver, i)
        user_list = create_user(driver, i)
        users_list.append(user_list)



all_test()
