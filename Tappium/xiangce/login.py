__author__ = 'Muse'
#coding=utf-8
from appium import webdriver
import  time
import logging

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.infinit.gallery'
desired_caps['appActivity'] = 'com.qihoo.gallery.home.HomePageActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(1)
user_btn=driver.find_element_by_class_name('android.widget.ImageButton')
user_btn.click()
# driver.get_screenshot_as_png()

# driver.get_screenshot_as_file(r'E:\batterystates\foo.png')
# print "png"
logging.info()
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
user_name = driver.find_element_by_id('text_avatar')


print user_name
if user_name.text =="231321321sadf":
    print "pass"
else:
    print "error!"
time.sleep(3)
driver.quit()
