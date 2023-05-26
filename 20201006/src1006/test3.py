from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

browser.find_element_by_id("kw").send_keys("杨洋")
# submit也可代替click
browser.find_element_by_id("su").submit()
time.sleep(6)
browser.find_element_by_id("kw").clear()
browser.find_element_by_id("kw").send_keys("秦霄贤")
browser.find_element_by_id("su").click()
time.sleep(6)
browser.quit()