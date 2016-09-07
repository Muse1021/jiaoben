#coding=utf-8
# import time
# from appium import webdriver
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '4.4.4'
# desired_caps['deviceName'] = 'Android Emulator'
# desired_caps['appPackage'] = 'com.qihoo.appstore'
# desired_caps['appActivity'] = '.home.LauncherActivity'
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# time.sleep(5)
# def NBsearch():
#     testele1 = driver.find_element_by_class_name("android.widget.Button")
#     print testele1
#     testele2= driver.find_element_by_id("com.qihoo.appstore:id/title")
#     print testele2
#     a = driver.find_element_by_name()
#     try:
#         testele = driver.find_element_by_class_name("android.widget.Button").find_elements_by_id("com.qihoo.appstore:id/title")
#         print testele
#         testele.click()
#     except:
#         pass
# el1 = driver.find_element_by_id("com.qihoo.appstore:id/btn_right")
# el1.click()
# driver.shake()
#
# time.sleep(4)
# driver.quit()
import sys
from adbmain import *
back()
print sys.path
