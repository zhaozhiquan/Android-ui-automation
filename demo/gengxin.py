#!/usr/bin/env python
# coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep, strftime
import HTMLTestRunner
import random
import shutil
import public.methods as t

class IHG1(unittest.TestCase,t.Methods):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'GT-I9500'
        # desired_caps['app'] = PATH('')
        desired_caps['appPackage'] = 'com.xuanyi.mbzj.appgame'
        desired_caps['appActivity'] = 'com.xuanyi.mbzj.SplashActivity'
        desired_caps['unicodeKeyboard'] = 'True'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        #智能等待
        self.driver.implicitly_wait(30)
    def tearDown(self):
        self.driver.quit()
    def test_0001(self):
        el = self.driver.find_element_by_id('com.xuanyi.mbzj.appgame:id/akeyLogin_btn').click()
        sleep(10)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(IHG1)
    unittest.TextTestRunner(verbosity=2).run(suite)
    '''now_time = strftime("%Y-%m-%d %H_%M_%S")
    filename = 'D:/test_result/'+now_time+"-result.html"
    fp = open(filename, 'wb')
    case_shuo_ming = u'测试情况'
    HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=case_shuo_ming).run(suite)
    fp.close()'''