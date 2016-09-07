#coding=utf-8
import random
import unittest  
from appium import webdriver
from adbmain import *
import  time
import re
import sys
class TestSequenceFunctions(unittest.TestCase):  

    def setUp(self,platformName = 'Android',
              platformVersion = '4.4.4',
              deviceName = 'Android Emulator',
              appPackage= 'com.qihoo.appstore',
              appActivity = '.home.LauncherActivity',
              appWaitActivity='com.oppo.camera.Camera'):

        self.platformName=platformName
        self.platformVersion=platformVersion
        self.deviceNamen=deviceName
        self.appPackage=appPackage
        self.appActivity=appActivity
        self.appWaitActivity=appWaitActivity
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
    def tearDown(self):
        print("teardown")
        driver.quit()

    def test_cebianlan(self):
        testxpath = driver.find_element_by_id("com.qihoo.appstore:id/btn_left")
    # print testxpath
        testxpath.click()
        but = driver.find_element_by_id("com.qihoo.appstore:id/slide_longin_btn_discon")
        text = but.text
        print(text)
        but.click()
        self.assertEqual(text,u"立即登录")

    def test_zhanghao(self):
        testxpath = driver.find_element_by_id("com.qihoo.appstore:id/btn_left")
    # print testxpath
        testxpath.click()
        but = driver.find_element_by_id("com.qihoo.appstore:id/slide_longin_btn_discon")
        but.click()
        text2 = driver.find_element_by_id("com.qihoo.appstore:id/slide_to_right").text
        self.assertEqual(text2,u'输入帐号登录')




  
if __name__ == '__main__':  
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)