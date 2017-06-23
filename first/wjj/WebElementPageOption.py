# incoding=gbk
from selenium import webdriver
import time
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import re

# from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://insm.chediandian.com/Login')
driver.maximize_window()
driver.implicitly_wait(30)
# 输入账户名以及密码后登陆
driver.find_element_by_id('Name').send_keys('wujiaojiao')
driver.find_element_by_id('Password').send_keys('wujiaojiao')
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/table/tbody/tr[3]/td/input').send_keys(Keys.ENTER)
# 查找用户询价链接按钮
driver.find_element_by_xpath("//ul[@class='bui-menu']/li[3]/a").click()

frame = driver.find_element_by_xpath('//*[@id="J_homeTab"]/div/div[2]/div[2]/iframe')
driver.switch_to.frame(frame)
# 获取查询时间
driver.find_element_by_name('endTime').click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='todayBtn']/button").click()
# 获取跟踪状态
time.sleep(1)
driver.find_element_by_name("traceStatus").click()
# time.sleep(1)
driver.find_element_by_xpath("//*[@id='searchForm']/div/div[11]/div/select/option[1]").click()
m=driver.find_element_by_class_name('bui-ext-mask')
# time.sleep(1)
driver.find_element_by_id('btnSearch').click()


# driver.implicitly_wait(60)
flag = 1
total = 0
while flag == 1:
    try:
        text = driver.find_element_by_id("totalPage").text
        total =int(re.findall(r'(\w*[0-9]+)\w*', text)[0])
        flag = 0
    except:
        driver.implicitly_wait(5)
print(total)
time.sleep(10)
# text1 = driver.find_element_by_class_name('bui-pb-page').text
page=int(driver.find_element_by_xpath("//*[@id='curPage']/input").get_attribute("value"))


if page <= total:
    driver.find_element_by_xpath('//*[@id="next"]/button').click()
    time.sleep(10)
print('')




# driver.quit()
