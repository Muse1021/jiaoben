#coding=utf-8
from appium import webdriver
import  time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.qihoo.appstore'
desired_caps['appActivity'] = '.home.LauncherActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(3)
tabicons = driver.find_elements_by_id('tab_item_icon')
tabicons[4].click()
managetabs = driver.find_elements_by_id('manage_item_arrows')
managetabs[5].click()

time.sleep(8)
desired_caps['appWaitActivity'] = '.base.SelectActivity'
driver.currentActivity()
shengdian_btn=driver.find_element_by_id('onekey_opt_btn')
shengdian_btn.click()
# print "-------------------"
# print  settings
time.sleep(3)
driver.quit()
