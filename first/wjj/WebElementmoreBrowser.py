#incoding=gbk
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
#��ȡ��ǰ���ھ��
nowhandle=driver.current_window_handle
#�򿪵�½����
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()

# driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
#������ɺ��ȡ����ע����󣬲����µ�ע�ᴰ��
element=WebDriverWait(driver,30).until(lambda driver:driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_8__submitWrapper"]/a[1]'))
element.click()
time.sleep(1)
#��ȡ���д���
allhandles=driver.window_handles
#ѭ���жϴ����Ƿ�Ϊ��ǰ����
for handle in allhandles:
    if handle !=nowhandle:
        driver.switch_to_window(handle)
        print('now register window')
        time.sleep(1)
#�رյ�ǰ����
        driver.close()
time.sleep(2)
#�ص�ԭ����ʼ����
driver.switch_to_window(nowhandle)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_2__closeBtn"]').click() 
time.sleep(1)
driver.find_element_by_id('kw').send_keys('�ɹ�ע��')   
#�˳���������ر����д���
driver.quit()
