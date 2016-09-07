#coding=utf-8
from appium import webdriver
import  time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.4'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.qihoo.appstore'
desired_caps['appActivity'] = '.home.LauncherActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
testxpath = driver.find_elements_by_xpath("//android.widget.LinearLayout[@index=2]")
testxpath[3].click()
TAB_bibei = driver.find_element_by_xpath("//android.widget.TextView[@text='必备']")
TAB_bibei.click()
list_app3 = driver.find_element_by_xpath("//android.widget.RelativeLayout[@index=3]")
list_app3.click()
driver.keyevent(4)
print "done"
time.sleep(5)
time.sleep(4)
driver.quit()