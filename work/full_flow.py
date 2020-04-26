from selenium import webdriver
from public_module import user_login
from my_template import make_permission_template
from export_policy import export_offline_policy


def full_flow():
    driver = webdriver.Chrome()
    url = 'https://192.168.1.28:8443/'
    username = 'SystemAdmin'
    password = 'Est@Spc820'
    user = 'sp1.local'
    user_login(driver, url, username, password)
    export_offline_policy(driver, user)


full_flow()
