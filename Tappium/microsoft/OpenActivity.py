#encoding:utf-8
from appium import webdriver
import  time
from adbmain import *
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.4'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.qihoo.appstore'
desired_caps['appActivity'] = 'com.qihoo.appstore.home.MainActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
def openappstore():
    driver.start_activity('com.qihoo.appstore','com.qihoo.appstore.home.MainActivity')
    driver.wait_activity('com.oppo.settings.SettingsActivity',4)
    time.sleep(5)
    btn_search = driver.find_element_by_id("com.qihoo.appstore:id/btn_search")
    btn_search.click()
    search_edit = driver.find_element_by_id("com.qihoo.appstore:id/search_edit")
    search_edit.send_keys("http://m.autohome.com.cn/?showTitleBar=0&microwebview=1&360appstore=1")
    time.sleep(5)
    common_list_download_proxy = driver.find_element_by_id("com.qihoo.appstore:id/common_list_download_proxy")
    common_list_download_proxy.click()
    time.sleep(3)
    driver.press_keycode(4)
    common_dialog_title = driver.find_element_by_id("com.qihoo.appstore:id/common_dialog_title")
    return common_dialog_title.text
    # try:
    #     common_dialog_negative_btn = driver.find_element_by_id("com.qihoo.appstore:id/common_dialog_negative_btn")
    #     common_dialog_negative_btn.click()
    # except:
    #     pass
def addtime():
    driver.start_activity('com.android.settings','com.oppo.settings.SettingsActivity')
    driver.wait_activity('com.oppo.settings.SettingsActivity',4)
    Sliding_screen(1)
    time.sleep(2)
    try:
        riqi = driver.find_element_by_xpath("//android.widget.TextView[@text='日期和时间']")
        riqi.click()
    except BaseException:
        print("no such element: "+"riqi")
    time.sleep(1)
    try:
        riqi_set = driver.find_element_by_xpath("//android.widget.LinearLayout[@index=2]")
        riqi_set.click()
    except BaseException:
        print("no such element: "+"riqi_set")
    time.sleep(1)
    try:
        increments = driver.find_elements_by_id("oppo:id/increment")
        increments[2].click()
    except BaseException:
        print("no such element: "+"increments")

    time.sleep(4)
    try:
        btn_insure = driver.find_element_by_id("android:id/button1")
        btn_insure.click()
    except:
        print "no such element:"+"btn_insure"
