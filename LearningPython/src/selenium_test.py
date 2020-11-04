from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("http://www.baidu.com")
# time.sleep(3)
browser.find_element_by_xpath("//*[@id='kw']").click()
browser.find_element_by_xpath("//*[@id='kw']").send_keys("今天是什么日子？")
browser.find_element_by_xpath("//*[@id='su']").click()
# browser.close()