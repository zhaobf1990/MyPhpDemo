#incoding=gbk
from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get("http://instest.chediandian.com")
browser.maximize_window()
time.sleep(3)
browser.find_element_by_name('licenseNo')
quit()


