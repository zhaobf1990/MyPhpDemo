# coding=utf-8
from selenium import webdriver
import unittest, time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class CarInsurance(unittest.TestCase):
    def setUp(self):
        # mobileEmulation = {'deviceName': 'Apple iPhone 6'}
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('mobileEmulation', mobileEmulation)
        # self.browser= webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        self.browser = webdriver.Chrome()
        self.base_url = "https://ins.chediandian.com/?token=DE8537F5250B9695D93F1BB48D6D2F57"
             # driver.get("http://ins.chediandian.com/?token=DE8537F5250B9695D93F1BB48D6D2F57")
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_China_Continent_Insurance(self):
        browser = self.browser
        browser.get(self.base_url)
        # browser.maximize_window()
        browser.implicitly_wait(30)
        # url = 'https://ins.chediandian.com/Flow/Step1?companyId=7&city=+$("#city").val()';
        js = "javascript:clientOpenUrl('大地保险', 'https://ins.chediandian.com/'+'Flow/Step1?companyId=7&city='+$('#city').val(),true);"
        # js = "javascript:clientOpenUrl('大地保险', 'https://ins.chediandian.com/'+'Flow/Step1?companyId=7&city='+$('#city').val(),true);"
        # js = "javascript:clientOpenUrl('大地保险', " + url + ",true);"
        browser.execute_script(js)
        time.sleep(5)

    def tearDown(self):
        self.browser.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
