from selenium import webdriver;
import yaml;

url="http://www.baidu.com"
# 初始化浏览器驱动
browser=webdriver.Chrome()
browser.maximize_window
browser.get(url)
browser.set_page_load_timeout(3)
browser.find_element_by_xpath("//*[@id='kw']").click()
browser.find_element_by_xpath("//*[@id='kw']").send_keys("百度一下")
browser.find_element_by_xpath("//*[@id='su']").click()
