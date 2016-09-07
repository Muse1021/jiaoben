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
list_apps = driver.find_elements_by_id("common_content_root")
# a = driver.find_element_by_class_name('1').find_element_by_xpath()
# #driver.findElement(By.name("layouttemplate_LinearLayout")).findElements(By.className("android.widget.LinearLayout")).size();
# b = driver.find_element_by_name("layouttemplate_LinearLayout").find_element_by_class_name("android.widget.LinearLayout")
# b.size()
list_apps[0].click()
time.sleep(5)
driver.keyevent(4)
print "done"
time.sleep(4)
driver.quit()