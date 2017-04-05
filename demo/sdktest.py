#!/usr/bin/env python
# coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep
import public.methods as t
class Test(unittest.TestCase,t.Methods):
    u'''快速注册'''
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps())
        #智能等待
        self.driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.quit()

    def test_0001(self):
        u'''启动游戏'''
        el1 = self.driver.find_element_by_id('com.xuanyi.mbzj.appgame:id/akeyLogin_btn').click()
        sleep(10)
if __name__ == '__main__':
    unittest.main()
