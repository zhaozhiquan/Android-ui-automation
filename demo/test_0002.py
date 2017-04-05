#!/usr/bin/env python
# coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep
import public.methods as t
class Test_Case(unittest.TestCase,t.Methods):
    u'''首页'''
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps())
        #智能等待
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
    def test_0001(self):
        u'''切换城市的县级城市'''
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/city').click()
        el2 = self.driver.find_element_by_name('白云区').click()
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/city')
        try:
            self.assertEqual(el3.text.encode('utf-8'), '白云区')
        except:
            self.screencap(self.driver, name='1test_0001')
            self.assertEqual(el2.text.encode('utf-8'), '白云区')
    def test_0002(self):
        u'''切换地级城市'''
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/city').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/changeCityBtn').click()
        while(True):#查找城市，当没找到该城市，划动，直到找到该城市，跳出循环
            try:
                el3 = self.driver.find_element_by_name('潮州市').click()
                break
            except:
                self.up_swipe(self.driver)
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/city')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '潮州市')
        except:
            self.screencap(self.driver, name='1test_0002')
            self.assertEqual(el4.text.encode('utf-8'), '潮州市')
    def test_0003(self):
        u'''点击banner图'''
        try:
            e1 = self.driver.find_element_by_name('切换').click()
        except:
            pass
        el = self.driver.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ImageView').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/btnBack').click()
        el3 = self.driver.find_element_by_name('购物导航')
        try:
            self.assertEqual(el3.text.encode('utf-8'), '购物导航')
        except:
            self.screencap(self.driver, name='1test_0003')
            self.assertEqual(el3.text.encode('utf-8'), '购物导航')

    def test_0004(self):
        u'''点击top'''
        el = self.driver.find_element_by_name('购物导航').click()
        while (True):
            try:
                el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/toTopBtn').click()
                break
            except:
                self.up_swipe(self.driver)
        el3 = self.driver.find_element_by_name('美食广场')
        try:
            self.assertEqual(el3.text.encode('utf-8'), '美食广场')
        except:
            self.screencap(self.driver, name='1test_0004')
            self.assertEqual(el3.text.encode('utf-8'), '美食广场')

    def test_0005(self):
        u'''分享到微信'''
        el = self.driver.find_element_by_name('购物导航').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/btnRight').click()
        el3 = self.driver.find_element_by_name('微信好友').click()
        el4 = self.driver.find_elements_by_id('com.tencent.mm:id/le')  # 选择好友
        el4[0].click()
        el5 = self.driver.find_element_by_name('分享').click()
        el6 = self.driver.find_element_by_name('已发送')
        try:
            self.assertEqual(el6.text.encode('utf-8'), '已发送')
        except:
            self.screencap(self.driver, name='1test_0005')
            self.assertEqual(el3.text.encode('utf-8'), '已发送')

    def test_0006(self):
        u'''分享到朋友圈'''
        el = self.driver.find_element_by_name('购物导航').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/btnRight').click()
        el3 = self.driver.find_element_by_name('微信朋友圈').click()
        el4 = self.driver.find_element_by_id('com.tencent.mm:id/eu').click()
        self.driver.start_activity('com.tencent.mm', 'com.tencent.mm.ui.LauncherUI')  # 运行微信
        el5 = self.driver.find_element_by_name('发现').click()  # 点击发现
        el6 = self.driver.find_element_by_name('朋友圈').click()
        while (True):
            try:
                el7 = self.driver.find_element_by_id('com.tencent.mm:id/cak')
                try:
                    self.assertEqual(el7.text.encode('utf-8'), '爱换购')
                    el8 = self.driver.find_element_by_id('com.tencent.mm:id/cam').click()
                    el9 =self.driver.find_element_by_id('com.tencent.mm:id/bif').click()
                except:
                    self.screencap(self.driver, name='1test_0006')
                    self.assertEqual(el7.text.encode('utf-8'), '爱换购')
                break
            except:
                self.up_swipe(self.driver)


    def test_0007(self):
        u'''分享到QQ'''
        el = self.driver.find_element_by_name('购物导航').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/btnRight').click()
        el3 = self.driver.find_element_by_name('QQ').click()
        el4 = self.driver.find_elements_by_id('com.tencent.mobileqq:id/icon')  # 选择好友
        el4[0].click()
        el5 = self.driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()  # 点击发送
        el6 = self.driver.find_element_by_name('发送成功')
        try:
            self.assertEqual(el6.text.encode('utf-8'), '发送成功')
        except:
            self.screencap(self.driver, name='1test_0007')
            self.assertEqual(el3.text.encode('utf-8'), '发送成功')

    def test_0008(self):
        u'''分享到QQ空间'''
        el = self.driver.find_element_by_name('购物导航').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/btnRight').click()
        el3 = self.driver.find_element_by_name('QQ空间').click()
        el4 = self.driver.find_element_by_id('com.tencent.mobileqq:id/ivTitleBtnRightText').click()  # 点击发送
        el5 = self.driver.find_element_by_id('com.tencent.mobileqq:id/conversation_head')
        # el6 = self.driver.find_element_by_id('com.tencent.mobileqq:id/nickname')
        try:
            self.assertIsNotNone(el5)
        except:
            self.screencap(self.driver, name='1test_0008')
            self.assertIsNotNone(el5)

    def test_0009(self):
        u'''进入更多购物中心列表'''
        el4 = self.driver.find_element_by_name('购物导航').click()
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/moreBtn').click()
        while (True):
            try:
                el2 = self.driver.find_element_by_name('花城汇').click()
                break
            except:
                self.up_swipe(self.driver)
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/txtTitle')
        try:
            self.assertEqual(el3.text.encode('utf-8'), '花城汇')
        except:
            self.screencap(self.driver, name='1test_0009')
            self.assertEqual(el3.text.encode('utf-8'), '花城汇')

    def test_0010(self):
        u'''搜索不同字符的商家'''
        el5 = self.driver.find_element_by_name('购物导航').click()
        a = ['美人渔', '3NMY', '高律kolee']
        for i in a:
            el = self.driver.find_element_by_id('com.iexbuy.ihg:id/mSearchBtn').click()
            el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/mSearchText').send_keys(i.decode("utf-8"))
            el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/searchBtn').click()
            el4 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listTitle')
            try:
                self.assertEqual(el4[0].text.encode('utf-8'), i)
            except:
                self.screencap(self.driver, name='1test_0010-' + i)
                self.assertEqual(el4[0].text.encode('utf-8'), i)
            self.driver.back()
            self.driver.back()
if __name__ == '__main__':
    unittest.main()