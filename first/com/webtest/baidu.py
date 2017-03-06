import os
from selenium import  webdriver
import time
import sys

# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# browser = webdriver.Chrome(chromedriver)
try:
    browser=webdriver.Chrome(r'C:\Users\feng\AppData\Local\Google\Chrome\Application\chromedriver.exe');
    browser.get("http://www.baidu.com")
    time.sleep(2)

    # browser.find_element_by_name("tj_login")[1].click();
    browser.find_element_by_xpath('//*[@id="u1"]/a[7]').click();
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id=\"TANGRAM__PSP_8__userName\"]").send_keys("’‘∞€∑„")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
# browser.find_element_by_id("kw").send_keys("’‘∞€∑„")
# browser.find_element_by_id("su").submit()

time.sleep(2)
browser.quit();