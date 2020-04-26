from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


def assign_project_manager(receiver, initial_status='测试负责人审核', final_status='项目经理审核'):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://pm.esafenet.com:8090/login')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('yangxiaochuan')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('yxc19961021..')
    driver.find_element_by_xpath('//*[@id="login-submit"]').click()
    time.sleep(2)
    while True:
        driver.find_element_by_xpath('//*[@id="loggedas"]/a').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul[2]/li[1]/a').click()
        time.sleep(2)
        tbody = driver.find_element_by_xpath('//*[@id="content"]/form[2]/div/table/tbody')
        trs_list = tbody.find_elements_by_tag_name('tr')
        tbody_text = tbody.get_attribute('innerHTML')
        if initial_status in tbody_text:
            for tr in trs_list:
                td = tr.find_elements_by_tag_name('td')[5]
                if td.text == initial_status:
                    tr.find_element_by_xpath('./td[8]/a').click()
                    time.sleep(2)
                    founder = driver.find_element_by_xpath('//*[@id="content"]/div[2]/p/a[1]').text
                    driver.find_element_by_xpath('//*[@id="content"]/div[1]/a[1]').click()
                    time.sleep(2)
                    state = Select(driver.find_element_by_xpath('//*[@id="issue_status_id"]'))
                    state.select_by_visible_text(final_status)
                    time.sleep(2)
                    staff = Select(driver.find_element_by_xpath('//*[@id="issue_assigned_to_id"]'))
                    if final_status == '测试验证':
                        staff.select_by_visible_text(founder)
                    else:
                        staff.select_by_visible_text(receiver)
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="issue-form"]/input[6]').click()
                    time.sleep(2)
                    break
        else:
            break
    print('BUG已转完！')


assign_project_manager(receiver='SJCPX 程浩浩')


# def assign_tester():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get('http://pm.esafenet.com:8090/login')
#     time.sleep(1)
#     driver.find_element_by_xpath('//*[@id="username"]').send_keys('yangxiaochuan')
#     driver.find_element_by_xpath('//*[@id="password"]').send_keys('yxc19961021..')
#     driver.find_element_by_xpath('//*[@id="login-submit"]').click()
#     time.sleep(2)
#     while True:
#         driver.find_element_by_xpath('//*[@id="loggedas"]/a').click()
#         time.sleep(2)
#         driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul[2]/li[1]/a').click()
#         time.sleep(2)
#         tbody = driver.find_element_by_xpath('//*[@id="content"]/form[2]/div/table/tbody')
#         trs_list = tbody.find_elements_by_tag_name('tr')
#         tbody_text = tbody.get_attribute('innerHTML')
#         if '测试负责人审核' in tbody_text:
#             for tr in trs_list:
#                 td = tr.find_elements_by_tag_name('td')[5]
#                 if td.text == '测试负责人审核':
#                     founder = driver.find_element_by_xpath('//*[@id="content"]/div[2]/p/a[1]').text
#                     tr.find_element_by_xpath('./td[8]/a').click()
#                     time.sleep(2)
#                     driver.find_element_by_xpath('//*[@id="content"]/div[1]/a[1]').click()
#                     time.sleep(2)
#                     state = Select(driver.find_element_by_xpath('//*[@id="issue_status_id"]'))
#                     state.select_by_visible_text('测试验证')
#                     time.sleep(2)
#                     staff = Select(driver.find_element_by_xpath('//*[@id="issue_assigned_to_id"]'))
#                     staff.select_by_visible_text(founder)
#                     time.sleep(2)
#                     driver.find_element_by_xpath('//*[@id="issue-form"]/input[6]').click()
#                     time.sleep(2)
#                     break
#         else:
#             break
#     print('BUG已转完！')
