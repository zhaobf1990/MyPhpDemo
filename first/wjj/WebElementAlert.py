#incoding=gbk
from selenium import  webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(1)
#点击打开搜索设置
# driver.find_element_by_xpath('//*[@id="u1"]/a[8]').click()
move=driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
ActionChains(driver).move_to_element(move).perform()
driver.find_element_by_xpath('//*[@id="wrapper"]/div[5]/a[1]').click()
#获取保存设置
element=WebDriverWait(driver,30).until(lambda driver:driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]'))
element.click()
#获取网页上的警告信息
a=driver.switch_to_alert()
# print(a.text)
# 接受警告信息
time.sleep(1)
print(a.text)
a.accept()
time.sleep(1)
# print(a.text())
driver.quit()