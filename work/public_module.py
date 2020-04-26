from time import sleep


def user_login(driver, url, username, password):
    driver.get(url)
    driver.maximize_window()
    try:
        driver.find_element_by_xpath('//*[@id="details-button"]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()
        sleep(2)
    except:
        pass
    driver.find_element_by_xpath('//*[@id="login_img"]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
    sleep(2)
    oa_main_frame = driver.find_element_by_xpath('//*[@id="oa_main"]')
    driver.switch_to.frame(oa_main_frame)
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/a/span/span').click()
        sleep(2)
    except:
        pass
    driver.switch_to.default_content()
    sleep(2)