#!/usr/bin/env python
# coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep
import public.methods as t
class Test_Case(unittest.TestCase,t.Methods):
    u'''0购'''
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps())
        #智能等待
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
    def test_0001(self):
        u'''全部分类遍历'''
        el = self.driver.find_element_by_name('金币云购').click()
        el2 = self.driver.find_element_by_name('全部分类').click()
        a = ['家用电器','美食天地','护肤彩妆','居家用品','汽车车品','手机数码','电脑平板','休闲娱乐','公益慈善','0元夺金']
        # '潮流新品'
        for i in a:
            el3 = self.driver.find_element_by_name(i).click()
            el5 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/yungouImg')
            try:
                self.assertIsNotNone(el5[0])
            except:
                self.screencap(self.driver, name='8test_0001' + i.decode('utf-8'))
                self.assertIsNotNone(el5[0])
    def test_0002(self):
        u'''新品'''
        el = self.driver.find_element_by_name('金币云购').click()
        el2 = self.driver.find_element_by_name('新品').click()
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/yungouImg')
        el3[0].click()
        while(True):
            try:
                el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/submitYunguoBtn').click()
                break
            except:
                self.up_swipe(self.driver)
        el5 = self.driver.find_element_by_id('com.iexbuy.ihg:id/submitPayBtn')
        try:
            self.assertEqual(el5.text.encode('utf-8'), '确定参与')
        except:
            self.screencap(self.driver, name='8test_0002')
            self.assertEqual(el5.text.encode('utf-8'), '确定参与')
    def test_0003(self):
        u'''0购记录'''
        el = self.driver.find_element_by_name('金币云购').click()
        el2 = self.driver.find_element_by_name('0购记录').click()
        el3 =self.driver.find_element_by_id('com.iexbuy.ihg:id/radio_button1')
        try:
            self.assertEqual(el3.text.encode('utf-8'), '所有0购')
        except:
            self.screencap(self.driver, name='8test_0003')
            self.assertEqual(el3.text.encode('utf-8'), '所有0购')
    def test_0004(self):
        u'''幸运中奖'''
        el = self.driver.find_element_by_name('金币云购').click()
        el2 = self.driver.find_element_by_name('幸运中奖').click()
        el3 =self.driver.find_element_by_id('com.iexbuy.ihg:id/radio_button2')
        try:
            self.assertEqual(el3.text.encode('utf-8'), '揭晓的0购')
        except:
            self.screencap(self.driver, name='8test_0004')
            self.assertEqual(el3.text.encode('utf-8'), '揭晓的0购')
    def test_0005(self):
        u'''公益慈善'''
        el = self.driver.find_element_by_name('金币云购').click()
        el2 = self.driver.find_element_by_name('公益慈善').click()
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/yungouImg')
        try:
            self.assertIsNotNone(el3[0])
        except:
            self.screencap(self.driver, name='8test_0005')
            self.assertIsNotNone(el3[0])
    def test_0006(self):
        u'''抢金币'''
        el = self.driver.find_element_by_name('金币云购').click()
        el2 = self.driver.find_element_by_name('抢金币').click()
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/yungouImg')
        try:
            self.assertIsNotNone(el3[0])
        except:
            self.screencap(self.driver, name='8test_0006')
            self.assertIsNotNone(el3[0])
    def test_0007(self):
        u'''进入充值金币'''
        el = self.driver.find_element_by_name('金币云购').click()
        el3 = self.driver.find_element_by_name('充值金币').click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/aliyPay')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '支付宝支付')
        except:
            self.screencap(self.driver, name='8test_0007')
            self.assertEqual(el4.text.encode('utf-8'), '支付宝支付')
    def test_0008(self):
        u'''幸运殿堂--查看更多'''
        el = self.driver.find_element_by_name('金币云购').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/lackyLayout').click()
        while(True):
            try:
                el3 = self.driver.find_element_by_name('3流剑客').click()
                break
            except:
                self.up_swipe(self.driver)
        el4 = self.driver.find_element_by_name('以往期数')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '以往期数')
        except:
            self.screencap(self.driver, name='8test_0008')
            self.assertEqual(el4.text.encode('utf-8'), '以往期数')
    def test_0009(self):
        u'''进入banner图'''
        el = self.driver.find_element_by_name('金币云购').click()
        sleep(3)
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/view_pager').click()
        el3 = self.driver.find_element_by_name('以往期数')
        try:
            self.assertEqual(el3.text.encode('utf-8'), '以往期数')
        except:
            self.screencap(self.driver, name='8test_0009')
            self.assertEqual(el3.text.encode('utf-8'), '以往期数')
    def test_0010(self):
        u'''参与0购'''
        el = self.driver.find_element_by_name('金币云购').click()
        while(True):
            try:
                el = self.driver.find_elements_by_id('com.iexbuy.ihg:id/yungouImg')
                el[1].click()
                self.up_swipe(self.driver)
                break
            except:
                self.up_swipe(self.driver)
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/submitYunguoBtn').click() #立即参与
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/submitPayBtn').click() #确认参与
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/cancle').click() #确认
        el5 =self.driver.find_element_by_id('com.iexbuy.ihg:id/shareCircleBtn')
        try:
            self.assertEqual(el5.text.encode('utf-8'), '分享到朋友圈')
        except:
            self.screencap(self.driver, name='8test_0010')
            self.assertEqual(el5.text.encode('utf-8'), '分享到朋友圈')