#coding=utf-8
from appium import webdriver
from adbmain import *
import  time
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
class xiangce (object):
    def __init__(self,platformName = 'Android',platformVersion = '5.1.1',deviceName = 'Android Emulator',appPackage= 'com.infinit.gallery',appActivity = 'com.qihoo.gallery.home.HomePageActivity',appWaitActivity='com.oppo.camera.Camera'):
        self.platformName=platformName
        self.platformVersion=platformVersion
        self.deviceNamen=deviceName
        self.appPackage=appPackage
        self.appActivity=appActivity
        self.appWaitActivity=appWaitActivity
    def start_activity (self):
        global desired_caps
        desired_caps = {}
        desired_caps['platformName'] = self.platformName
        desired_caps['platformVersion'] = self.platformVersion
        desired_caps['deviceName'] = self.deviceNamen
        desired_caps['appPackage'] = self.appPackage
        desired_caps['appActivity'] = self.appActivity
        # desired_caps['appWaitActivity'] = self.appWaitActivity
        global driver
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def login(self):
        user_btn=driver.find_element_by_class_name('android.widget.ImageButton')
        user_btn.click()
        user_name = driver.find_element_by_id('text_avatar')
        username = str(user_name.text)
        print username
        if username == '未登录':
            login_btn = driver.find_element_by_id('image_avatar')
            login_btn.click()
            account = driver.find_element_by_id('qaet_autoComplete')
            account.send_keys("13785754658")
            #login_captcha = driver.find_element_by_id('login_captcha_text')
            time.sleep(1)
            login_click_btn1 = driver.find_element_by_id("login_click")
            login_click_btn1.click()
            password = driver.find_element_by_id('login_password')
            password.send_keys("paojiao")
            login_click_btn2 = driver.find_element_by_id("login_click")
            login_click_btn2.click()
            user_btn.click()
            return user_name.text
        elif user_name.text == '231321321sadf':
            return "已登陆，用户名为："+user_name.text
        else:
            return "error"
    def new_pic(self,num):
        action_take_photo = driver.find_element_by_id('action_take_photo')
        action_take_photo.click()
        driver.wait_activity('com.oppo.camera.Camera',4)
        now_activity = driver.current_activity
        shutter_button = driver.find_element_by_id('com.oppo.camera:id/shutter_button')
        for i in range(num):
            time.sleep(2)
            shutter_button.click()
        # driver.press_keycode('4')
        time.sleep(2)
        os.system("adb shell input keyevent 4")
        time.sleep(3)
        driver.wait_activity('com.qihoo.gallery.home.HomePageActivity',4)
        more_text_num = driver.find_element_by_id('more_text_num').text
        more_text = str(more_text_num)
        m = re.findall(r'(\w*[0-9]+)\w*',more_text)
        result = int(m[1])
        if result==num:
            print result
            print "pass"
        else:
            print "false"