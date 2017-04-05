#!/usr/bin/env python
# coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep
import public.methods as t
class Test_Case(unittest.TestCase,t.Methods):
    u'''换购'''
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps())
        #智能等待
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
    def test_0001(self):
        u'''支付宝充值金币'''
        el = self.driver.find_element_by_name('特卖商城').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyCoinBtn').click() #点击充值
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/aliyPay').click()   #点击支付宝
        try:
            self.up_swipe(self.driver)
        except:
            self.up_swipe(self.driver)
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/submitPayBtn').click() #立即支付
        el5 = self.driver.find_element_by_name('支付宝账号')
        try:
            self.assertEqual(el5.text.encode('utf-8'), '支付宝账号')
        except:
            self.screencap(self.driver, name='7test_0001')
            self.assertEqual(el5.text.encode('utf-8'), '支付宝账号')
    def test_0002(self):
        u'''微信充值金币'''
        el = self.driver.find_element_by_name('特卖商城').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyCoinBtn').click()  # 点击充值
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/weixingPay').click()  # 点击微信
        try:
            self.up_swipe(self.driver)
        except:
            self.up_swipe(self.driver)
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/submitPayBtn').click()  # 立即支付
        el5 = self.driver.find_element_by_id('android:id/text2')
        try:
            self.assertEqual(el5.text.encode('utf-8'), '微信安全支付')
        except:
            self.screencap(self.driver, name='7test_0002')
            self.assertEqual(el5.text.encode('utf-8'), '微信安全支付')
    def test_0003(self):
        u'''点击banner图1'''
        el = self.driver.find_element_by_name('特卖商城').click()
        sleep(5)
        #el2 = self.driver.find_element_by_xpath('//android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ImageView').click()
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/view_pager').click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='7test_0003')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
    def test_0004(self):
        u'''点击banner图2'''
        el = self.driver.find_element_by_name('特卖商城').click()
        el2 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/view_pager')
        el2[1].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='7test_0004')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
    def test_0005(self):
        u'''推荐-家居专区'''
        el = self.driver.find_element_by_name('特卖商城').click()
        while(True):
            try:
                el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/fitmentBtn').click()
                break
            except:
                self.up_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
        el3[0].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='7test_0005')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
    def test_0006(self):
        u'''推荐-精品专区'''
        el = self.driver.find_element_by_name('特卖商城').click()
        while(True):
            try:
                el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/choicenessBtn').click()
                break
            except:
                self.up_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
        el3[0].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='7test_0006')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
    def test_0007(self):
        u'''推荐-数码专区'''
        el = self.driver.find_element_by_name('特卖商城').click()
        while(True):
            try:
                el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/numericalCodeBtn').click()
                break
            except:
                self.up_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
        el3[0].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='7test_0007')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
    def test_0008(self):
        u'''推荐-彩妆专区'''
        el = self.driver.find_element_by_name('特卖商城').click()
        while(True):
            try:
                el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/beautyBtn').click()
                break
            except:
                self.up_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
        el3[0].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='7test_0008')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
    def test_0009(self):
        u'''点击banner图3'''
        el = self.driver.find_element_by_name('特卖商城').click()
        while(True):
            try:
                el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/beautyBtn')
                break
            except:
                self.up_swipe(self.driver)
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/view_pager').click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/btnBack')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '返回')
        except:
            self.screencap(self.driver, name='7test_0009')
            self.assertEqual(el4.text.encode('utf-8'), '返回')

    def test_0010(self):
        u'''top键'''
        el = self.driver.find_element_by_name('特卖商城').click()
        while (True):
            try:
                el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/toTopBtn').click() #top键
                break
            except:
                self.up_swipe(self.driver)
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyCoinBtn') #充值金币
        try:
            self.assertEqual(el3.text.encode('utf-8'), '充值金币')
        except:
            self.screencap(self.driver, name='7test_0010')
            self.assertEqual(el3.text.encode('utf-8'), '充值金币')
