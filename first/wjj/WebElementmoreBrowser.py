#incoding=gbk
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
#获取当前窗口句柄
nowhandle=driver.current_window_handle
#打开登陆弹窗
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()

# driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
#加载完成后获取立即注册对象，并打开新的注册窗口
element=WebDriverWait(driver,30).until(lambda driver:driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_8__submitWrapper"]/a[1]'))
element.click()
time.sleep(1)
#获取所有窗口
allhandles=driver.window_handles
#循环判断窗口是否为当前窗口
for handle in allhandles:
    if handle !=nowhandle:
        driver.switch_to_window(handle)
        print('now register window')
        time.sleep(1)
#关闭当前窗口
        driver.close()
time.sleep(2)
#回到原来初始窗口
driver.switch_to_window(nowhandle)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_2__closeBtn"]').click() 
time.sleep(1)
driver.find_element_by_id('kw').send_keys('成功注册')   
#退出驱动程序关闭所有窗口
driver.quit()
