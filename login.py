#!/usr/bin/env python
from selenium import  webdriver

driver = webdriver.Chrome('/home/django/Desktop/chromedriver')

driver.get("http://172.16.40.5:8090/httpclient.html")

user = driver.find_element_by_name("username")
user.send_keys("trump_user")
password = driver.find_element_by_name("password")
password.send_keys("trump_pw")

driver.find_element_by_name("btnSubmit").click()
driver.close()
