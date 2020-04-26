from time import sleep
from datetime import datetime
from selenium.webdriver.support.ui import Select


def make_permission_template(driver):
    oa_main_top_frame = driver.find_element_by_xpath('//*[@id="oa_main_top"]')
    driver.switch_to.frame(oa_main_top_frame)
    login_username_text = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table/tbody/tr/td[1]/span[2]').text
    driver.switch_to.default_content()
    oa_left_middle_frame = driver.find_element_by_xpath('//*[@id="oa_left_middle"]')
    driver.switch_to.frame(oa_left_middle_frame)
    my_workbench = driver.find_element_by_xpath('//*[@id="outlooktitle0"]/table/tbody/tr/td')
    my_workbench.click()
    sleep(2)
    my_template = driver.find_element_by_xpath('//*[@id="outlookdivin0"]/span[2]/table/tbody/tr/td/a')
    my_template.click()
    sleep(2)
    driver.switch_to.default_content()
    oa_main_frame = driver.find_element_by_xpath('//*[@id="oa_main"]')
    driver.switch_to.frame(oa_main_frame)
    add_button = driver.find_element_by_xpath('//*[@id="wncontrol"]/div/div/div[1]/table/tbody/tr/td[1]/a/span/span')
    add_button.click()
    sleep(2)
    now_datetime = datetime.now()
    now_datetime_str = now_datetime.strftime('%Y%m%d%H%M%S')
    permission_template_name = driver.find_element_by_xpath('//*[@id="templetName"]')
    if '文档管理员' in login_username_text:
        fill_template_name = 'public{time}'.format(time=now_datetime_str)
        permission_template_name.send_keys(fill_template_name)
        sleep(2)
    else:
        fill_template_name = 'test{time}'.format(time=now_datetime_str)
        permission_template_name.send_keys(fill_template_name)
        sleep(2)
    confidentiality_level = driver.find_element_by_xpath('//*[@id="secrelevel"]')
    Select(confidentiality_level).select_by_visible_text('核心商密(Core business secret)')
    sleep(2)
    permission_template_describe = driver.find_element_by_xpath('//*[@id="description"]')
    permission_template_describe.send_keys('请问123QWas')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="app_manager_dialog_template"]/div[2]/a[1]/span/span').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[11]/div[2]/div[3]/a/span/span').click()
    sleep(2)
    my_template_tbody = driver.find_element_by_xpath('//*[@id="wncontrol"]/div/div/div[2]/div[2]/div[2]/table/tbody')
    my_template_trs = my_template_tbody.find_elements_by_tag_name('tr')
    for tr in my_template_trs:
        if tr.find_element_by_xpath('./td[2]/div[1]').text == fill_template_name:
            tr.find_element_by_xpath('./td[1]/div[1]/input[1]').click()
            sleep(2)
            break
    empower_button = driver.find_element_by_xpath('//*[@id="wncontrol"]/div/div/div[1]/table/tbody/tr/td[4]/a/span')
    empower_button.click()
    sleep(2)
    add_department = driver.find_element_by_xpath('//*[@id="reTemplateToolbarAddGrupBtn"]/span/span')
    add_department.click()
    sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="selectGroupList"]/ul/li/div/span[1]').click()
        sleep(2)
    except:
        pass
    driver.find_element_by_xpath('//*[@id="selectGroupList"]/ul/li/div/span[3]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="save_template_group"]/span/span').click()
    sleep(3)
    driver.find_element_by_xpath('/html/body/div[last()-2]/div[2]/div[3]/a/span/span').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="common_template_groupListDialog"]/div[2]/a/span/span').click()
    sleep(2)
    page_list = driver.find_element_by_xpath('//*[@id="reTemplateDialogInnerDIV"]/div/div/div/div/div[3]/table/tbody/tr/td[1]/select')
    Select(page_list).select_by_visible_text('50')
    sleep(2)
    template_authorization_tbody = driver.find_element_by_xpath('//*[@id="reTemplateDialogInnerDIV"]/div/div/div/div/div[2]/div[2]/div[2]/table/tbody')
    template_authorization_trs = template_authorization_tbody.find_elements_by_tag_name('tr')
    for tr in template_authorization_trs:
        tr.find_element_by_xpath('./td[4]/div[1]/input[3]').click()
        sleep(2)
    driver.find_element_by_xpath('//*[@id="reTemplateDialogAffirm"]/span/span').click()
    sleep(3)
    driver.find_element_by_xpath('/html/body/div[last()-2]/div[2]/div[3]/a/span/span').click()
    sleep(2)



