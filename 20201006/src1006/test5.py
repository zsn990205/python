from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("秦霄贤")
driver.find_element_by_id("su").click()
time.sleep(3)
title = driver.title
print("title ="+title)
url = driver.current_url
print("url ="+url)