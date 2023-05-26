from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
text = browser.find_element_by_id("s-bottom-layer-right").text
print("text:"+text)

