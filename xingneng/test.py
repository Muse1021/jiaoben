from appium import webdriver
import  time
import sys
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.4'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.qihoo.appstore'
desired_caps['appActivity'] = 'com.qihoo.appstore.home.MainActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
driver.start_activity('com.android.settings','com.oppo.settings.SettingsActivity')
driver.wait_activity('com.oppo.settings.SettingsActivity',4)
driver.quit()