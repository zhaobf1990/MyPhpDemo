#coding=utf-8
from selenium import webdriver

import time

driver=webdriver.Chrome()
driver.get("http://ins.chediandian.com/?token=DE8537F5250B9695D93F1BB48D6D2F57")
driver.implicitly_wait(30)


js="javascript:clientOpenUrl('大地保险', 'https://ins.chediandian.com/'+'Flow/Step1?companyId=7&city='+$('#city').val(),true);"
driver.execute_script(js)