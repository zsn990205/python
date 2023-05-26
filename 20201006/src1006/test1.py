from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("秦霄贤")
driver.find_element_by_id("su").click()
time.sleep(3)
# 浏览器的放大
driver.maximize_window()
time.sleep(3)
# 浏览器的缩小
driver.minimize_window()
time.sleep(3)
# 设置浏览器的宽和高
driver.set_window_size(300,500)
time.sleep(3)
# 控制浏览器的滚动条到最低端
js = "var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(3)
# 控制浏览器的滚动条到最顶端
js = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)