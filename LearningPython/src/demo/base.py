from selenium import webdriver;
import time;
import yaml;
import os;
path=os.getcwd()
class Login:
    global dr 
    dr= webdriver.Chrome()
    #  初始化浏览器驱动    
    def __init__(self,driver):
       self.driver= dr
 
         
    # 登录模块封装
    def login(self):
           
        self.file=open(path+"/src/data/page_data.yaml",'r',encoding="utf-8")
        self.data=yaml.load(self.file,Loader=yaml.FullLoader)
        self.driver.maximize_window()
        self.driver.get(self.data['login'].get('url'))   
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.data['login'].get('quit')).click()
        self.driver.find_element_by_xpath(self.data['login'].get('username')).click()
        self.driver.find_element_by_xpath(self.data['login'].get('username')).send_keys(self.data['login'].get('user'))
        self.driver.find_element_by_xpath(self.data['login'].get('password')).click()
        self.driver.find_element_by_xpath(self.data['login'].get('password')).send_keys(self.data['login'].get('passwd'))
        self.driver.find_element_by_xpath(self.data['login'].get('login')).click()
                


        
