from selenium import webdriver
import time
from read_write_excel import *
from datetime import datetime


def login(driver, url, username, password):
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="login_img"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
    time.sleep(2)


def entry_organization_and_management(driver):
    oa_left_middle = driver.find_element_by_xpath('//*[@id="oa_left_middle"]')
    driver.switch_to.frame(oa_left_middle)
    driver.find_element_by_xpath('//*[@id="outlooktitle0"]/table/tbody/tr/td').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="outlookdivin0"]/span[1]/table/tbody/tr/td/a').click()
    time.sleep(2)
    driver.switch_to.default_content()
    oa_main = driver.find_element_by_xpath('//*[@id="oa_main"]')
    driver.switch_to.frame(oa_main)


def return_homepage(driver):
    driver.switch_to.default_content()
    oa_main_top = driver.find_element_by_xpath('//*[@id="oa_main_top"]')
    driver.switch_to.frame(oa_main_top)
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table/tbody/tr/td[2]/a/span[1]').click()
    time.sleep(2)
    driver.switch_to.default_content()


def create_organization(driver, organization_name):
    entry_organization_and_management(driver)
    driver.find_element_by_xpath('//*[@id="0_span"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="create"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="groupName"]').send_keys(organization_name)
    driver.find_element_by_xpath('//*[@id="btnSave"]').click()
    time.sleep(2)
    driver.switch_to.alert.accept()
    time.sleep(2)
    return_homepage(driver)


def create_user(driver, organization_name):
    entry_organization_and_management(driver)
    driver.find_element_by_xpath('//*[@id="0_switch"]').click()
    time.sleep(2)
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
    time.sleep(2)
    for i in range(3):
        driver.find_element_by_xpath('//*[@id="tbUserList"]/thead[2]/tr/td/input[3]').click()
        time.sleep(2)
        now_time = datetime.now()
        now_time_str = now_time.strftime('%m%d%H%M%S')
        add_user = 'cs%s' % now_time_str
        driver.find_element_by_xpath('//*[@id="userName"]').send_keys(add_user)
        driver.find_element_by_xpath('//*[@id="surName"]').send_keys(add_user)
        driver.find_element_by_xpath('//*[@id="btnSave"]').click()
        time.sleep(2)
        user_list.append('{user}.local'.format(user=add_user))
    write_approver_data(user_list)
    user_list = []
    return_homepage(driver)
    # return user_list


def add_approver(driver):
    user_list = read_test_data('approver_list')
    for i in range(2, 10):
        oa_left_middle = driver.find_element_by_xpath('//*[@id="oa_left_middle"]')
        driver.switch_to.frame(oa_left_middle)
        driver.find_element_by_xpath('//*[@id="outlooktitle6"]/table/tbody/tr/td').click()
        driver.find_element_by_xpath('//*[@id="outlookdivin6"]/span[2]/table/tbody/tr/td/a').click()
        time.sleep(2)
        driver.switch_to.default_content()
        oa_main = driver.find_element_by_xpath('//*[@id="oa_main"]')
        driver.switch_to.frame(oa_main)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[%s]/td[6]/a' % i).click()
        time.sleep(2)
        while True:
            table1 = driver.find_element_by_xpath('//*[@id="table1"]')
            trs_list = table1.find_elements_by_tag_name('tr')
            if len(trs_list) == 2:
                break
            else:
                parent_td = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[7]/td[2]')
                delete_approver = parent_td.find_elements_by_tag_name('table')[-1].find_elements_by_tag_name('input')[-1]
                delete_approver.click()
                time.sleep(2)
                driver.switch_to.alert.accept()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/form/table/tbody/tr[8]/td/input[2]').click()
                time.sleep(2)
                driver.switch_to.alert.accept()
                time.sleep(2)
        driver.find_element_by_xpath('//*[@id="bn1"]').click()
        time.sleep(2)
        tbody = driver.find_element_by_xpath('//*[@id="myForm"]/table[2]/tbody')
        trs_list = tbody.find_elements_by_tag_name('tr')
        add_user = trs_list[-1].find_elements_by_tag_name('input')[-2]
        add_user.click()
        time.sleep(2)
        treeValue1 = driver.find_element_by_xpath('//*[@id="treeValue1"]')
        driver.switch_to.frame(treeValue1)
        for user in user_list[0]:
            driver.find_element_by_xpath('//*[@id="userName"]').send_keys(user)
            driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[2]/input').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/p/input[3]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="userName"]').clear()
            time.sleep(2)
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/input[1]').click()
        time.sleep(2)
        driver.switch_to.default_content()
        oa_main = driver.find_element_by_xpath('//*[@id="oa_main"]')
        driver.switch_to.frame(oa_main)
        while True:
            tbody = driver.find_element_by_xpath('//*[@id="myForm"]/table[2]/tbody')
            trs_list = tbody.find_elements_by_tag_name('tr')
            tr_list = trs_list[:-2]
            if len(tr_list) == 3:
                break
            else:
                for tr in tr_list:
                    tds_list = tr.find_elements_by_tag_name('td')
                    if tds_list[2].text not in user_list[0]:
                        tds_list[-1].find_elements_by_tag_name('a')[0].click()
                        time.sleep(2)
                        driver.switch_to.alert.accept()
                        time.sleep(2)
                        break
        tbody = driver.find_element_by_xpath('//*[@id="myForm"]/table[2]/tbody')
        trs_list = tbody.find_elements_by_tag_name('tr')
        tr_list = trs_list[:-2]
        for i in range(1, len(tr_list)+1):
            driver.find_element_by_xpath('//*[@id="myForm"]/table[2]/tbody/tr[%s]/td[5]/a[2]' % i).click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="selectGroupList"]/ul/li/div/span[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="selectGroupList"]/ul/li/div/span[3]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="save_template_group"]/span/span').click()
            time.sleep(2)
            try:
                hwnd1 = driver.find_element_by_xpath('/html/body/div[16]/div[2]/div[3]/a/span/span')
                hwnd1.click()
            except:
                try:
                    hwnd2 = driver.find_element_by_xpath('/html/body/div[15]/div[2]/div[3]/a/span/span')
                    hwnd2.click()
                except:
                    pass
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="setApprovalUser_range_groupListDialog"]/div[2]/a/span/span').click()
            time.sleep(2)
        trs_list[-1].find_elements_by_tag_name('td')[0].find_elements_by_tag_name('input')[0].click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        trs_list[-1].find_elements_by_tag_name('td')[0].find_elements_by_tag_name('input')[-1].click()
        time.sleep(2)
        node_list = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[7]/td[2]')
        add_apply_level = node_list.find_elements_by_tag_name('table')[-1].find_elements_by_tag_name('input')[0]
        add_apply_level.click()
        time.sleep(2)
        second_node = node_list.find_elements_by_tag_name('table')[0].find_elements_by_tag_name('tr')[-1]
        add_apply = second_node.find_elements_by_tag_name('td')[-1].find_elements_by_tag_name('a')[0]
        add_apply.click()
        time.sleep(2)
        treeValue2 = driver.find_element_by_xpath('//*[@id="treeValue2"]')
        driver.switch_to.frame(treeValue2)
        for user in user_list[1]:
            driver.find_element_by_xpath('//*[@id="userName"]').send_keys(user)
            driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[2]/input').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/p/input[3]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="userName"]').clear()
            time.sleep(2)
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/input[1]').click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.switch_to.default_content()
        oa_main = driver.find_element_by_xpath('//*[@id="oa_main"]')
        driver.switch_to.frame(oa_main)
        time.sleep(2)
        tbody = driver.find_element_by_xpath('//*[@id="table1"]/tbody')
        trs_list = tbody.find_elements_by_tag_name('tr')
        second_apply = trs_list[-1].find_elements_by_tag_name('td')[-1].find_elements_by_tag_name('a')[-1]
        second_apply.click()
        time.sleep(2)
        approver_tbody = driver.find_element_by_xpath('//*[@id="myForm"]/table[2]/tbody')
        approver_tr_list = approver_tbody.find_elements_by_tag_name('tr')[:-2]
        for q in range(1, len(approver_tr_list)+1):
            driver.find_element_by_xpath('//*[@id="myForm"]/table[2]/tbody/tr[%s]/td[5]/a[2]' % q).click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="selectGroupList"]/ul/li/div/span[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="selectGroupList"]/ul/li/div/span[3]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="save_template_group"]/span/span').click()
            time.sleep(2)
            try:
                hwnd1 = driver.find_element_by_xpath('/html/body/div[16]/div[2]/div[3]/a/span/span')
                hwnd1.click()
            except:
                try:
                    hwnd2 = driver.find_element_by_xpath('/html/body/div[15]/div[2]/div[3]/a/span/span')
                    hwnd2.click()
                except:
                    pass
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="setApprovalUser_range_groupListDialog"]/div[2]/a/span/span').click()
            time.sleep(2)
        tbody = driver.find_element_by_xpath('//*[@id="myForm"]/table[2]/tbody')
        trs_list = tbody.find_elements_by_tag_name('tr')
        trs_list[-1].find_elements_by_tag_name('td')[0].find_elements_by_tag_name('input')[0].click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        trs_list[-1].find_elements_by_tag_name('td')[0].find_elements_by_tag_name('input')[-1].click()
        time.sleep(2)
        driver.switch_to.default_content()
        oa_main = driver.find_element_by_xpath('//*[@id="oa_main"]')
        driver.switch_to.frame(oa_main)
        time.sleep(2)

        node_list = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[7]/td[2]')
        add_apply_level = node_list.find_elements_by_tag_name('table')[-1].find_elements_by_tag_name('input')[0]
        add_apply_level.click()
        time.sleep(2)
        second_node = node_list.find_elements_by_tag_name('table')[0].find_elements_by_tag_name('tr')[-1]
        add_apply = second_node.find_elements_by_tag_name('td')[-1].find_elements_by_tag_name('a')[0]
        add_apply.click()
        time.sleep(2)
        treeValue3 = driver.find_element_by_xpath('//*[@id="treeValue3"]')
        driver.switch_to.frame(treeValue3)
        for user in user_list[2]:
            driver.find_element_by_xpath('//*[@id="userName"]').send_keys(user)
            driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[2]/input').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/p/input[3]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="userName"]').clear()
            time.sleep(2)
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/input[1]').click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.switch_to.default_content()
        oa_main = driver.find_element_by_xpath('//*[@id="oa_main"]')
        driver.switch_to.frame(oa_main)
        time.sleep(2)
        tbody = driver.find_element_by_xpath('//*[@id="table1"]/tbody')
        trs_list = tbody.find_elements_by_tag_name('tr')
        second_apply = trs_list[-1].find_elements_by_tag_name('td')[-1].find_elements_by_tag_name('a')[-1]
        second_apply.click()
        time.sleep(2)
        approver_tbody = driver.find_element_by_xpath('//*[@id="myForm"]/table[2]/tbody')
        approver_tr_list = approver_tbody.find_elements_by_tag_name('tr')[:-2]
        for q in range(1, len(approver_tr_list)+1):
            driver.find_element_by_xpath('//*[@id="myForm"]/table[2]/tbody/tr[%s]/td[5]/a[2]' % q).click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="selectGroupList"]/ul/li/div/span[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="selectGroupList"]/ul/li/div/span[3]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="save_template_group"]/span/span').click()
            time.sleep(2)
            try:
                hwnd1 = driver.find_element_by_xpath('/html/body/div[16]/div[2]/div[3]/a/span/span')
                hwnd1.click()
            except:
                try:
                    hwnd2 = driver.find_element_by_xpath('/html/body/div[15]/div[2]/div[3]/a/span/span')
                    hwnd2.click()
                except:
                    pass
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="setApprovalUser_range_groupListDialog"]/div[2]/a/span/span').click()
            time.sleep(2)
        tbody = driver.find_element_by_xpath('//*[@id="myForm"]/table[2]/tbody')
        trs_list = tbody.find_elements_by_tag_name('tr')
        trs_list[-1].find_elements_by_tag_name('td')[0].find_elements_by_tag_name('input')[0].click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        trs_list[-1].find_elements_by_tag_name('td')[0].find_elements_by_tag_name('input')[-1].click()
        time.sleep(2)
        driver.switch_to.default_content()
        oa_main = driver.find_element_by_xpath('//*[@id="oa_main"]')
        driver.switch_to.frame(oa_main)
        time.sleep(2)
        tbody = driver.find_element_by_xpath('//*[@id="table1"]/tbody')
        tr_list = tbody.find_elements_by_tag_name('tr')[1:]
        for tr in tr_list:
            countersign = tr.find_elements_by_tag_name('td')[2].find_element_by_tag_name('input')
            countersign.clear()
            time.sleep(2)
            countersign.send_keys('3')
            time.sleep(2)
        tbody = driver.find_element_by_xpath('/html/body/form/table/tbody')
        trs_list = tbody.find_elements_by_tag_name('tr')
        determine = trs_list[-1].find_elements_by_tag_name('input')[1]
        determine.click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        return_homepage(driver)




def all_test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    login(driver, read_test_data('login_data')[-1][0], read_test_data('login_data')[-1][1], read_test_data('login_data')[-1][2])
    organization_list = ['审批组1', '审批组2', '审批组3']
    # clear_test_sheet('approver_list')
    # for i in organization_list:
    #     create_organization(driver, i)
    #     create_user(driver, i)
    add_approver(driver)


if __name__ == '__main__':
    all_test()

