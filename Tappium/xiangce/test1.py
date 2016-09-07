#coding=utf-8
from appium import webdriver
import  time
def start ():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'com.qihoo.appstore'
    desired_caps['appActivity'] = '.home.LauncherActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(5)
    testxpath = driver.find_elements_by_xpath("//android.widget.ImageView[@NAF='true']")
    print testxpath
    testxpath[1].click()
    driver.quit()
start()