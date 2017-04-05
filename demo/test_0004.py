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
        u'''优惠活动1'''
        el3 = self.driver.find_element_by_name('购物导航').click()
        self.up_swipe(self.driver)
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/adOne').click()
        self.up_swipe(self.driver)
        self.down_swipe(self.driver)
        back = self.driver.find_element_by_name('返回').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/radio_button1')
        try:
            self.assertEqual(el2.text.encode('utf-8'), '购物导航')
        except:
            self.screencap(self.driver, name='4test_0001')
            self.assertEqual(el2.text.encode('utf-8'), '购物导航')

    def test_0002(self):
        u'''优惠活动2'''
        el3 = self.driver.find_element_by_name('购物导航').click()
        self.up_swipe(self.driver)
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/adTwo').click()
        self.up_swipe(self.driver)
        self.down_swipe(self.driver)
        back = self.driver.find_element_by_name('返回').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/radio_button1')
        try:
            self.assertEqual(el2.text.encode('utf-8'), '购物导航')
        except:
            self.screencap(self.driver, name='4test_0002')
            self.assertEqual(el2.text.encode('utf-8'), '购物导航')

    def test_0003(self):
        u'''优惠活动3'''
        el3 = self.driver.find_element_by_name('购物导航').click()
        self.up_swipe(self.driver)
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/adThree').click()
        self.up_swipe(self.driver)
        self.down_swipe(self.driver)
        back = self.driver.find_element_by_name('返回').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/radio_button1')
        try:
            self.assertEqual(el2.text.encode('utf-8'), '购物导航')
        except:
            self.screencap(self.driver, name='4test_0003')
            self.assertEqual(el2.text.encode('utf-8'), '购物导航')
    def test_0004(self):
        u'''购物-换购切换'''
        el = self.driver.find_element_by_name('购物导航').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/radio_button2').click()
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/txtTitle')
        try:
            self.assertEqual(el3.text.encode('utf-8'), '特卖商城')
        except:
            self.screencap(self.driver, name='4test_0004')
            self.assertEqual(el3.text.encode('utf-8'), '特卖商城')
    def test_0005(self):
        u'''购物-0购切换'''
        el = self.driver.find_element_by_name('购物导航').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/radio_button3').click()
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/txtTitle')
        try:
            self.assertEqual(el3.text.encode('utf-8'), '金币云购')
        except:
            self.screencap(self.driver, name='4test_0005')
            self.assertEqual(el3.text.encode('utf-8'), '金币云购')
    def test_0006(self):
        u'''购物-个人中心切换'''
        el = self.driver.find_element_by_name('购物导航').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/radio_button4').click()
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/txtTitle')
        try:
            self.assertEqual(el3.text.encode('utf-8'), '个人中心')
        except:
            self.screencap(self.driver, name='4test_0006')
            self.assertEqual(el3.text.encode('utf-8'), '个人中心')

    def test_0007(self):
        u'''进入购物中心--导航'''
        el = self.driver.find_element_by_name('购物导航').click()
        self.up_swipe(self.driver)
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/shopCenterIcon').click()
        e = self.driver.find_element_by_id('com.iexbuy.ihg:id/shopCenterAdrMap').click()  # 查看
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/navigation').click()
        el4 = self.driver.find_element_by_id('top').click()
        el5 = self.driver.find_element_by_id('com.baidu.BaiduMap:id/radioButton0')  # 百度
        try:
            self.assertEqual(el5.text.encode('utf-8'), '最短时间')
        except:
            self.screencap(self.driver, name='4test_0007')
            self.assertEqual(el5.text.encode('utf-8'), '最短时间')

    def test_0008(self):
        u'''所有店铺'''
        el = self.driver.find_element_by_name('购物导航').click()
        while (True):
            try:
                el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/shopCenterIcon').click()
                break
            except:
                self.up_swipe(self.driver)
        self.up_swipe(self.driver)
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/shopListLayout').click()
        a = ['全部类别', '美食广场', '购物天地']
        for i in a:
            el5 = self.driver.find_element_by_id('com.iexbuy.ihg:id/categorySelectLayout').click()
            el4 = self.driver.find_element_by_name(i).click()
            el6 = self.driver.find_element_by_name(i)
            try:
                self.assertEqual(el6.text.encode('utf-8'), i)
            except:
                self.screencap(self.driver, name='4test_0008')
                self.assertEqual(el6.text.encode('utf-8'), i)

    def test_0009(self):
        u'''进入品牌商家'''
        el = self.driver.find_element_by_name('购物导航').click()
        self.up_swipe(self.driver)
        while (True):
            try:
                el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/view_pager').click()
                break
            except:
                self.up_swipe(self.driver)
        try:
            self.up_swipe(self.driver)
            self.down_swipe(self.driver)
        finally:
            back = self.driver.find_element_by_id('com.iexbuy.ihg:id/btnBack').click() #返回按钮
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/radio_button1')  #购物导航
        try:
            self.assertEqual(el3.text.encode('utf-8'), '购物导航')
        except:
            self.screencap(self.driver, name='4test_0009')
            self.assertEqual(el3.text.encode('utf-8'), '购物导航')

    def test_0010(self):
        u'''周边商家'''
        el = self.driver.find_element_by_name('购物导航').click()
        while (True):
            try:
                el2 = self.driver.find_element_by_name('周边商家')
                break
            except:
                self.up_swipe(self.driver)
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listTitle')
        el3[0].click()
        try:
            self.up_swipe(self.driver)
            self.down_swipe(self.driver)
        finally:
            back = self.driver.find_element_by_id('com.iexbuy.ihg:id/btnBack').click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/radio_button1')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '购物导航')
        except:
            self.screencap(self.driver, name='4test_0010')
            self.assertEqual(el4.text.encode('utf-8'), '购物导航')
if __name__ == '__main__':
    unittest.main()