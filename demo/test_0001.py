#!/usr/bin/env python
# coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep
import public.methods as t
class Test_Case(unittest.TestCase,t.Methods):
    u'''购物导航-商家界面遍历、支付'''
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps())
        #智能等待
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
    def t001(self):
        u'''进入商家'''
        el5 = self.driver.find_element_by_name('购物导航').click()
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/mSearchBtn').click() #搜索
        el1 = self.driver.find_element_by_id('com.iexbuy.ihg:id/mSearchText').send_keys('Pull'.decode('utf-8'))
        sousuo = self.driver.find_element_by_id('com.iexbuy.ihg:id/searchBtn').click()  #搜索按钮
        el2 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')  #选择第一个logo
        el2[0].click()
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/shopTitle')
        try:
            self.assertEqual(el3.text.encode('utf-8'), 'Pull')
        except:
            self.screencap(self.driver, name='0test_t001')
            self.assertEqual(el3.text.encode('utf-8'), 'Pull')

    def test_0001(self):
        u'''划动导航页，进入app首页'''
        try:
            btn_allow = self.driver.find_element_by_name('允许').click() #弹出gps权限，点击允许
        except:pass
        sleep(2)
        for i in range(3):
            self.left_swipe(self.driver)
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/loginBtn').click()
        el2 = self.driver.find_element_by_name('购物导航')
        try:
            self.assertEqual(el2.text.encode('utf-8'), '购物导航')
        except:
            self.screencap(self.driver, name='0test_0001')
            self.assertEqual(el2.text.encode('utf-8'), '购物导航')
    def test_0002(self):
        u'''登陆'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/loginBtn').click()
        while (True):
            el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/userName')
            el4.clear()
            el4.send_keys('test'.decode("utf-8"))
            if el4.text.encode('utf-8') == 'test':
                break
        el5 = self.driver.find_element_by_id('com.iexbuy.ihg:id/password')
        el5.clear()
        el5.send_keys('445566'.decode("utf-8"))
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/loginBtn').click()
        el6 = self.driver.find_element_by_id('com.iexbuy.ihg:id/userMobile')
        try:
            self.assertEqual(el6.text.encode('utf-8'), 'test')
        except:
            self.screencap(self.driver, name='0test_0002')
            self.assertEqual(el6.text.encode('utf-8'), 'test')

    def test_0003(self):
        u'''商家导航'''
        self.t001()
        sleep(2)
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/ico_address').click()
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/navigation').click()
        el4 = self.driver.find_element_by_id('top').click()
        el5 = self.driver.find_element_by_id('com.baidu.BaiduMap:id/radioButton0')  # 百度
        try:
            self.assertEqual(el5.text.encode('utf-8'), '最短时间')
        except:
            self.screencap(self.driver, name='0test_0003')
            self.assertEqual(el5.text.encode('utf-8'), '最短时间')
    def test_0004(self):
        u'''进入优惠券'''
        self.t001()
        sleep(2)
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/shopCouponLayout').click()  #更多
        el3 = self.driver.find_element_by_name('返回').click()  #返回
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/shopTitle')
        try:
            self.assertEqual(el2.text.encode('utf-8'), 'Pull')
        except:
            self.screencap(self.driver, name='0test_0004')
            self.assertEqual(el2.text.encode('utf-8'), 'Pull')
    def test_0005(self):
        u'''图文-评论切换'''
        self.t001()
        sleep(2)
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/radio_button2').click()
        try:
            self.up_swipe(self.driver)
        except:
            pass
        el2 = self.driver.find_elements_by_xpath('//android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout')
        try:
            self.assertIsNotNone(el2[int(len(el2)) - 1])
        except:
            self.screencap(self.driver, name='0test_0005')
            self.assertIsNotNone(el2[int(len(el2)) - 1])
    def test_0006(self):
        u'''拨号'''
        self.t001()
        sleep(2)
        el  = self.driver.find_element_by_id('com.iexbuy.ihg:id/ico_phone').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/cancle').click()
        try:
            el3 = self.driver.find_element_by_id('com.huawei.systemmanager:id/btn_allow').click()
        except:pass
        el4 = self.driver.find_element_by_id('com.android.incallui:id/callStateLabel')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '正在拨号')
        except:
            self.screencap(self.driver, name='0test_0006')
            self.assertEqual(el4.text.encode('utf-8'), '正在拨号')
        el5 = self.driver.find_element_by_id('com.android.incallui:id/endButton').click()
    def test_0007(self):
        u'''特卖商品'''
        self.t001()
        sleep(2)
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/radio_button1').click() #推荐
        try:
            self.up_swipe(self.driver)
        except:
            self.up_swipe(self.driver)
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/listIcon').click()
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/shopTitle')
        try:
            self.assertEqual(el3.text.encode('utf-8'), '花纹雪纺衬衫')
        except:
            self.screencap(self.driver, name='0test_0007')
            self.assertEqual(el3.text.encode('utf-8'), '花纹雪纺衬衫')
    def test_0008(self):
        u'''面对面支付，金币支付'''
        self.t001()
        sleep(2)
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/directBuyBtn').click() #立即买单
        while(True):
            el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/price')  #买单价
            el2.send_keys('0.1'.decode("utf-8"))
            if el2.text.encode('utf-8') == '0.1':
                break
        while(True):
            el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/coin') # 金币抵扣
            el3.send_keys('1'.decode("utf-8"))
            if el3.text.encode('utf-8') == '1':
                break
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/submitOrderBtn').click() #确认买单
        el5 = self.driver.find_element_by_id('com.iexbuy.ihg:id/cancle').click()   #确认
        el6 = self.driver.find_element_by_id('com.iexbuy.ihg:id/orderStatus')   #支付状态
        try:
            self.assertEqual(el6.text.encode('utf-8'), '(已支付)')
        except:
            self.screencap(self.driver, name='0test_0008')
            self.assertEqual(el6.text.encode('utf-8'), '(已支付)')
    def test_0009(self):
        u'''面对面支付，支付宝支付'''
        self.t001()
        sleep(2)
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/directBuyBtn').click()  #立即买单
        while (True):
            el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/price')  #买单价
            el2.send_keys('0.1'.decode("utf-8"))
            if el2.text.encode('utf-8') == '0.1':
                break
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/submitOrderBtn').click() #确认买单
        el6 = self.driver.find_element_by_id('com.iexbuy.ihg:id/aliyPay').click()  # 选择支付宝
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/submitPayBtn').click() #确认支付
        el5 = self.driver.find_element_by_name('支付宝账号')
        try:
            self.assertEqual(el5.text.encode('utf-8'), '支付宝账号')
        except:
            self.screencap(self.driver, name='0test_0009')
            self.assertEqual(el5.text.encode('utf-8'), '支付宝账号')
    def test_0010(self):
        u'''面对面支付，微信支付'''
        self.t001()
        sleep(2)
        el = self.driver.find_element_by_id('com.iexbuy.ihg:id/directBuyBtn').click()  # 立即买单
        while (True):
            el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/price')  # 买单价
            el2.send_keys('0.1'.decode("utf-8"))
            if el2.text.encode('utf-8') == '0.1':
                break
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/submitOrderBtn').click()  # 确认买单
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/weixingPay').click() #选择微信支付
        el5 = self.driver.find_element_by_id('com.iexbuy.ihg:id/submitPayBtn').click()  # 确认支付
        el6 = self.driver.find_element_by_id('android:id/text2')
        try:
            self.assertEqual(el6.text.encode('utf-8'), '微信安全支付')
        except:
            self.screencap(self.driver, name='0test_0010')
            self.assertEqual(el6.text.encode('utf-8'), '微信安全支付')
if __name__ == '__main__':
    unittest.main()





