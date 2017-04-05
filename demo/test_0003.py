#!/usr/bin/env python
# coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep
import public.methods as t
class Test_Case(unittest.TestCase,t.Methods):
    u'''购物导航'''
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps())
        #智能等待
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_0001(self):
        u'''美食广场'''
        el = self.driver.find_element_by_name('购物导航').click()
        el2 = self.driver.find_element_by_name('美食广场').click()
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listTitle')
        el3[0].click()
        try:
            self.up_swipe(self.driver)
            self.down_swipe(self.driver)
        finally:
            self.driver.back()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/categoryBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '美食广场')
        except:
            self.screencap(self.driver, name='3test_0001')
            self.assertEqual(el4.text.encode('utf-8'), '美食广场')

    def test_0002(self):
        u'''休闲娱乐'''
        el = self.driver.find_element_by_name('购物导航').click()
        el2 = self.driver.find_element_by_name('休闲娱乐').click()
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listTitle')
        el3[0].click()
        try:
            self.up_swipe(self.driver)
            self.down_swipe(self.driver)
        finally:
            self.driver.back()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/categoryBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '休闲娱乐')
        except:
            self.screencap(self.driver, name='3test_0002')
            self.assertEqual(el4.text.encode('utf-8'), '休闲娱乐')

    def test_0003(self):
        u'''酒店住宿'''
        el = self.driver.find_element_by_name('购物导航').click()
        el2 = self.driver.find_element_by_name('酒店住宿').click()
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listTitle')
        el3[0].click()
        try:
            self.up_swipe(self.driver)
            self.down_swipe(self.driver)
        finally:
            self.driver.back()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/categoryBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '酒店住宿')
        except:
            self.screencap(self.driver, name='3test_0003')
            self.assertEqual(el4.text.encode('utf-8'), '酒店住宿')

    def test_0004(self):
        u'''时尚丽人'''
        el = self.driver.find_element_by_name('购物导航').click()
        el2 = self.driver.find_element_by_name('时尚丽人').click()
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listTitle')
        el3[0].click()
        try:
            self.up_swipe(self.driver)
            self.down_swipe(self.driver)
        finally:
            self.driver.back()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/categoryBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '时尚丽人')
        except:
            self.screencap(self.driver, name='3test_0004')
            self.assertEqual(el4.text.encode('utf-8'), '时尚丽人')

    def test_0005(self):
        u'''购物天地'''
        el = self.driver.find_element_by_name('购物导航').click()
        el2 = self.driver.find_element_by_name('购物天地').click()
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listTitle')
        el3[0].click()
        try:
            self.up_swipe(self.driver)
            self.down_swipe(self.driver)
        finally:
            self.driver.back()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/categoryBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '购物天地')
        except:
            self.screencap(self.driver, name='3test_0005')
            self.assertEqual(el4.text.encode('utf-8'), '购物天地')

    def test_0006(self):
        u'''生活服务'''
        el = self.driver.find_element_by_name('购物导航').click()
        el2 = self.driver.find_element_by_name('生活服务').click()
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listTitle')
        el3[0].click()
        try:
            self.up_swipe(self.driver)
            self.down_swipe(self.driver)
        finally:
            self.driver.back()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/categoryBtn')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '生活服务')
        except:
            self.screencap(self.driver, name='3test_0006')
            self.assertEqual(el4.text.encode('utf-8'), '生活服务')
if __name__ == '__main__':
    unittest.main()