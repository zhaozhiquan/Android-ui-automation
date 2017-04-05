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
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()
    def test_0001(self):
        u'''进入banner图2'''
        el = self.driver.find_element_by_name('金币云购').click()
        while(True):
            try:
                el = self.driver.find_element_by_id('com.iexbuy.ihg:id/yungouCateBtn')
                break
            except:
                self.up_swipe(self.driver)
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/view_pager').click() #进入banner图2
        el3 = self.driver.find_element_by_name('以往期数')
        try:
            self.assertEqual(el3.text.encode('utf-8'), '以往期数')
        except:
            self.screencap(self.driver, name='9test_0001')
            self.assertEqual(el3.text.encode('utf-8'), '以往期数')
    def test_0002(self):
        u'''推荐--0元中手机'''
        el = self.driver.find_element_by_name('金币云购').click()
        while (True):
            try:
                el = self.driver.find_element_by_id('com.iexbuy.ihg:id/yungouCateBtn').click()
                break
            except:
                self.up_swipe(self.driver)
        el2 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/yungouImg')
        try:
            self.assertIsNotNone(el2[0])
        except:
            self.screencap(self.driver, name='9test_0002')
            self.assertIsNotNone(el2[0])
    def test_0003(self):
        u'''推荐-0元生活购'''
        el = self.driver.find_element_by_name('金币云购').click()
        while (True):
            try:
                el = self.driver.find_element_by_id('com.iexbuy.ihg:id/yungouSkinBtn').click()
                break
            except:
                self.up_swipe(self.driver)
        el2 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/yungouImg')
        try:
            self.assertIsNotNone(el2[0])
        except:
            self.screencap(self.driver, name='9test_0003')
            self.assertIsNotNone(el2[0])
    def test_0004(self):
        u'''推荐-0元夺金'''
        el = self.driver.find_element_by_name('金币云购').click()
        while (True):
            try:
                el = self.driver.find_element_by_id('com.iexbuy.ihg:id/yungousuppliesBtn').click()
                break
            except:
                self.up_swipe(self.driver)
        el2 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/yungouImg')
        try:
            self.assertIsNotNone(el2[0])
        except:
            self.screencap(self.driver, name='9test_0004')
            self.assertIsNotNone(el2[0])
    def test_0005(self):
        u'''推荐-0元抢家电'''
        el = self.driver.find_element_by_name('金币云购').click()
        while (True):
            try:
                el = self.driver.find_element_by_id('com.iexbuy.ihg:id/yungouApplianceBtn').click()
                break
            except:
                self.up_swipe(self.driver)
        el2 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/yungouImg')
        try:
            self.assertIsNotNone(el2[0])
        except:
            self.screencap(self.driver, name='9test_0005')
            self.assertIsNotNone(el2[0])
    def test_0006(self):
        u'''推荐-0元中宝马'''
        el = self.driver.find_element_by_name('金币云购').click()
        while (True):
            try:
                el = self.driver.find_element_by_id('com.iexbuy.ihg:id/yungouButton').click()
                break
            except:
                self.up_swipe(self.driver)
        el2 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/yungouImg')
        try:
            self.assertIsNotNone(el2[0])
        except:
            self.screencap(self.driver, name='9test_0006')
            self.assertIsNotNone(el2[0])
    def test_0007(self):
        u'''热拍榜'''
        el = self.driver.find_element_by_name('金币云购').click()
        while (True):
            try:
                el = self.driver.find_element_by_id('com.iexbuy.ihg:id/hotLayout').click()
                break
            except:
                self.up_swipe(self.driver)
        el2 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/yungouImg')
        try:
            self.assertIsNotNone(el2[0])
        except:
            self.screencap(self.driver, name='9test_0007')
            self.assertIsNotNone(el2[0])
    def test_0008(self):
        u'''热拍商品'''
        el = self.driver.find_element_by_name('金币云购').click()
        while (True):
            try:
                el = self.driver.find_element_by_id('com.iexbuy.ihg:id/hotLayout')
                break
            except:
                self.up_swipe(self.driver)
        el2 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/yungouImg')
        el2[0].click()
        el3 = self.driver.find_element_by_name('以往期数')
        try:
            self.assertEqual(el3.text.encode('utf-8'), '以往期数')
        except:
            self.screencap(self.driver, name='9test_0008')
            self.assertEqual(el3.text.encode('utf-8'), '以往期数')
    def test_0009(self):
        u'''TOP键'''
        el = self.driver.find_element_by_name('金币云购').click()
        while (True):
            try:
                el = self.driver.find_element_by_id('com.iexbuy.ihg:id/toTopBtn').click()
                break
            except:
                self.up_swipe(self.driver)
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyCoinBtn')
        try:
            self.assertEqual(el2.text.encode('utf-8'), '充值金币')
        except:
            self.screencap(self.driver, name='9test_0009')
            self.assertEqual(el2.text.encode('utf-8'), '充值金币')