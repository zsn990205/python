from selenium import webdriver
# 引入鼠标的包
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()

driver.find_element_by_id("kw").send_keys("秦霄贤")
# 定位百度一下按钮
sul = driver.find_element_by_id("su")
# 右击
ActionChains(driver).context_click(sul).perform()
time.sleep(6)

# 双击
ActionChains(driver).double_click(sul).perform()