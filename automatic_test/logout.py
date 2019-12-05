import time


def logout(self):
    driver = self.driver
    # iframe = driver.find_element_by_xpath("//*[@id=\"oa_main_top\"]")
    # driver.switch_to.frame(iframe)
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table/tbody/tr/td[4]/a/span[1]').click()
    time.sleep(2)

