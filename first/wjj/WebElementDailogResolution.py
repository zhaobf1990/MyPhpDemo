#incoding=gbk
from selenium import webdriver
import time
import sys
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome()
driver.get('https://www.baidu.com')


#点击登录链接
# driver.find_element_by_name('tj_login').click()
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
print('yes')
#通过二次定位找到用户名输入框

# div=driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_2__content"]')
# div.send_keys('username')
try:
    element=WebDriverWait(driver,30).until(lambda  driver : driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_2__content"]' ))
    element.find_element_by_name('userName').send_keys('username')
    time.sleep(3)
    driver.find_element_by_name('password').send_keys('password')
    time.sleep(3)
#     driver.find_element_by_id('TANGRAM__PSP__8__submit').click()
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
driver.quit()

#失败，无法识别对象
