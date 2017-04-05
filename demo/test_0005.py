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
        u'''全部分类遍历'''
        el = self.driver.find_element_by_name('特卖商城').click()
        el2 = self.driver.find_element_by_name('全部分类').click()
        a = ['护肤彩妆','手机数码','家居家纺','食品饮料','办公家电','服饰配件','鞋帽箱包','日用百货','运动户外','母婴亲子','家具建材']
        for i in a :
            el3 = self.driver.find_element_by_name(i).click()
            el5 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
            el5[0].click()
            el6 =self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
            try:
                self.assertEqual(el6.text.encode('utf-8'), '立即换购')
            except:
                self.screencap(self.driver, name='6test_0001-'+i.decode('utf-8'))
                self.assertEqual(el6.text.encode('utf-8'), '立即换购')
            finally:
                back = self.driver.find_element_by_id('com.iexbuy.ihg:id/btnBack').click()
    def test_0002(self):
        u'''手机数码'''
        el = self.driver.find_element_by_name('特卖商城').click()
        for i in range(3):
            try:
                el2 = self.driver.find_element_by_name('手机数码').click()
                break
            except:
                self.left_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
        el3[0].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='6test_0002')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')

    def test_0003(self):
        u'''办公家电'''
        el = self.driver.find_element_by_name('特卖商城').click()
        for i in range(3):
            try:
                el2 = self.driver.find_element_by_name('办公家电').click()
                break
            except:
                self.left_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
        el3[0].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='6test_0003')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')

    def test_0004(self):
        u'''护肤彩妆'''
        el = self.driver.find_element_by_name('特卖商城').click()
        for i in range(3):
            try:
                el2 = self.driver.find_element_by_name('护肤彩妆').click()
                break
            except:
                self.left_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
        el3[0].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='6test_0004')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')

    def test_0005(self):
        u'''日用百货'''
        el = self.driver.find_element_by_name('特卖商城').click()
        for i in range(3):
            try:
                el2 = self.driver.find_element_by_name('日用百货').click()
                break
            except:
                self.left_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
        el3[0].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='6test_0005')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')

    def test_0006(self):
        u'''食品饮料'''
        el = self.driver.find_element_by_name('特卖商城').click()
        for i in range(3):
            try:
                el2 = self.driver.find_element_by_name('食品饮料').click()
                break
            except:
                self.left_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
        el3[0].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='6test_0006')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
    def test_0007(self):
        u'''家居家纺'''
        el = self.driver.find_element_by_name('特卖商城').click()
        for i in range(3):
            try:
                el2 = self.driver.find_element_by_name('家居家纺').click()
                break
            except:
                self.left_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
        el3[0].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='6test_0007')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
    def test_0008(self):
        u'''服饰配件'''
        el = self.driver.find_element_by_name('特卖商城').click()
        for i in range(3):
            try:
                el2 = self.driver.find_element_by_name('服饰配件').click()
                break
            except:
                self.left_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
        el3[0].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='6test_0008')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
    def test_0009(self):
        u'''鞋帽箱包'''
        el = self.driver.find_element_by_name('特卖商城').click()
        for i in range(3):
            try:
                el2 = self.driver.find_element_by_name('鞋帽箱包').click()
                break
            except:
                self.left_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
        el3[0].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='6test_0009')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')

    def test_0010(self):
        u'''运动户外'''
        el = self.driver.find_element_by_name('特卖商城').click()
        for i in range(3):
            try:
                el2 = self.driver.find_element_by_name('运动户外').click()
                break
            except:
                self.left_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
        el3[0].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='6test_0010')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
    def test_0011(self):
        u'''母婴亲子'''
        el = self.driver.find_element_by_name('特卖商城').click()
        for i in range(3):
            try:
                el2 = self.driver.find_element_by_name('母婴亲子').click()
                break
            except:
                self.left_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
        el3[0].click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')
        except:
            self.screencap(self.driver, name='6test_0011')
            self.assertEqual(el4.text.encode('utf-8'), '立即换购')



if __name__ == '__main__':
    unittest.main()