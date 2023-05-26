from selenium import webdriver
# 引入键盘的包
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()

driver.find_element_by_id("kw").send_keys("秦霄贤")
driver.find_element_by_id("su").click()
time.sleep(3)

# 复制
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")
time.sleep(3)
# 剪贴
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"x")
time.sleep(4)
driver.find_element_by_id("kw").send_keys("杨洋")
driver.find_element_by_id("su").click()