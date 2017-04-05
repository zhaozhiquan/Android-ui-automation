#!/usr/bin/env python
# coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep
import public.methods as t
import random
class Test_Case(unittest.TestCase,t.Methods):
    u'''个人中心'''
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps())
        #智能等待
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
    def test_0001(self):
        u'''退出登录'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 =self.driver.find_element_by_id('com.iexbuy.ihg:id/btnSetting').click() #设置按钮
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/exit').click()  #退出登录
        el4 = self.driver.find_element_by_name('确定').click()
        el5 = self.driver.find_element_by_id('com.iexbuy.ihg:id/loginBtn')
        try:
            self.assertEqual(el5.text.encode('utf-8'), '登录')
        except:
            self.screencap(self.driver, name='10test_0001')
            self.assertEqual(el5.text.encode('utf-8'), '登录')
    def test_0002(self):
        '''关于我们'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/btnSetting').click()  # 设置按钮
        el3= self.driver.find_element_by_id('com.iexbuy.ihg:id/aboutMeLayout').click() #关于我们
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/txtTitle')
        try:
            self.assertEqual(el4.text.encode('utf-8'), '关于爱换购')
        except:
            self.screencap(self.driver, name='10test_0002')
            self.assertEqual(el4.text.encode('utf-8'), '关于爱换购')
    def test_0003(self):
        u'''发送验证码'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_name('登录').click()
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/jumpForgetPasswordBtn').click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/mobileNo')
        el4.send_keys('13711477453'.decode("utf-8"))
        el5 =self.driver.find_element_by_id('com.iexbuy.ihg:id/getValidateCodeBtn')
        el5.click() #发送验证码
        sleep(5)
        try:
            self.assertNotEqual(el5.text.encode('utf-8'), '发送验证码')
        except:
            self.screencap(self.driver, name='10test_0003')
            self.assertNotEqual(el5.text.encode('utf-8'), '发送验证码')
    def test_0004(self):
        u'''登录'''
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
            self.screencap(self.driver, name='10test_0004')
            self.assertEqual(el6.text.encode('utf-8'), 'test')
    def test_0005(self):
        u'''更改用户名'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_name('个人信息管理').click()
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/userName').click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/userName')
        el4.clear()
        a = [0,1,2,3]
        b = str(random.choice(a))
        c ='test账号'+b
        el4.send_keys(c.decode("utf-8"))
        el5 =self.driver.find_element_by_id('com.iexbuy.ihg:id/btnRight').click()
        el6 = self.driver.find_element_by_id('com.iexbuy.ihg:id/userName')
        try:
            self.assertEqual(el6.text.encode('utf-8'), c)
        except:
            self.screencap(self.driver, name='10test_0005')
            self.assertEqual(el6.text.encode('utf-8'), c)
    def test_0006(self):
        u'''新增收货地址'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_name('个人信息管理').click()
        el3 =self.driver.find_element_by_id('com.iexbuy.ihg:id/addressLayout').click()
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/addAddressBtn').click()
        el5 =self.driver.find_element_by_id('com.iexbuy.ihg:id/name').send_keys('test姓名1'.decode("utf-8"))
        el6 = self.driver.find_element_by_id('com.iexbuy.ihg:id/mobileNo').send_keys('13711477453'.decode("utf-8"))
        el7= self.driver.find_element_by_id('com.iexbuy.ihg:id/areaNo').send_keys('test区号1'.decode("utf-8"))
        el8 = self.driver.find_element_by_id('com.iexbuy.ihg:id/address').send_keys('test地址1'.decode("utf-8"))
        el1 = self.driver.find_element_by_id('com.iexbuy.ihg:id/saveAddress').click() #保存
        el9 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/mobileNo')
        a = int(len(el9))-1
        try:
            self.assertEqual(el9[a].text.encode('utf-8'), '13711477453')
        except:
            self.screencap(self.driver, name='10test_0006')
            self.assertEqual(el9[a].text.encode('utf-8'), '13711477453')
    def test_0007(self):
        u'''编辑收货地址'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_name('个人信息管理').click()
        el3 =self.driver.find_element_by_id('com.iexbuy.ihg:id/addressLayout').click()
        el4 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/editAddressLayout')
        b = int(len(el4))-1#编辑
        el4[b].click()
        el5= self.driver.find_element_by_id('com.iexbuy.ihg:id/mobileNo')
        el5.clear()
        el5.send_keys('13711477455'.decode("utf-8"))
        el11 = self.driver.find_element_by_id('com.iexbuy.ihg:id/toggleButton').click() #默认地址
        el1 = self.driver.find_element_by_id('com.iexbuy.ihg:id/saveAddress').click()  # 保存
        el9 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/mobileNo')
        a = int(len(el9))-1
        try:
            self.assertEqual(el9[a].text.encode('utf-8'), '13711477455')
        except:
            self.screencap(self.driver, name='10test_0006')
            self.assertEqual(el9[a].text.encode('utf-8'), '13711477455')
    '''def test_0008(self):
        u''''''
        el = self.driver.find_element_by_name('特卖商城').click()
        while (True):
            try:
                el2 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/listIcon')
                el2[0].click()
                break
            except:
                self.up_swipe(self.driver)
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/buyBtn').click() #立即换购
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/submitPayBtn').click() #确定参与
        el5 = self.driver.find_element_by_id('com.iexbuy.ihg:id/cancle').click() #确认
        el6 =self.driver.find_element_by_id('com.iexbuy.ihg:id/shareCircleBtn') #分享
        try:
            self.assertEqual(el6.text.encode('utf-8'), '分享')
        except:
            self.screencap(self.driver, name='10test_0008')
            self.assertEqual(el4.text.encode('utf-8'), '分享')'''

    def test_0009(self):
        u'''删除收货地址'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_name('个人信息管理').click()
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/addressLayout').click()
        el6 =self.driver.find_elements_by_id('com.iexbuy.ihg:id/mobileNo')
        a = int(len(el6))
        el4 = self.driver.find_element_by_id('com.iexbuy.ihg:id/deleteAddressLayout').click()  # 删除
        el5 = self.driver.find_element_by_id('com.iexbuy.ihg:id/cancle').click() #确定
        el7 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/mobileNo')
        b =int(len(el7))
        try:
            self.assertEqual(a,b+1)
            print u'删除成功'
        except:
            self.screencap(self.driver,name='10test_0009')
            self.assertEqual(a, b + 1)
    def test_0010(self):
        u'''待支付取消订单'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_name('消费订单').click()
        el3 =self.driver.find_elements_by_id('com.iexbuy.ihg:id/itemTime')
        b = el3[0].text.encode('utf-8')
        el3[0].click()
        el4 =self.driver.find_element_by_id('com.iexbuy.ihg:id/cancelOrderBtn').click() #取消订单
        el5 =self.driver.find_element_by_name('确定').click()
        el6 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/itemTime')
        try:
            self.assertNotEquals(el6[0].text.encode('utf-8'), b)
        except:
            self.screencap(self.driver, name='10test_0010')
            self.assertNotEquals(el6[0].text.encode('utf-8'), b)
    def test_0011(self):
        u'''待支付订单，支付宝支付'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_name('消费订单').click()
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/itemImage')
        el3[0].click()
        el4 =self.driver.find_element_by_id('com.iexbuy.ihg:id/continuePayBtn').click() #继续支付
        el5 =self.driver.find_element_by_id('com.iexbuy.ihg:id/aliyPay').click()  #选择支付宝
        el6 =self.driver.find_element_by_id('com.iexbuy.ihg:id/submitPayBtn').click() #确认支付
        el7 =self.driver.find_element_by_name('支付宝账号')
        try:
            self.assertEqual(el7.text.encode('utf-8'), '支付宝账号')
        except:
            self.screencap(self.driver, name='10test_0011')
            self.assertEqual(el7.text.encode('utf-8'), '支付宝账号')
    def test_0012(self):
        u'''待支付订单，微信支付'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_name('消费订单').click()
        el3 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/itemImage')
        el3[0].click()
        el4 =self.driver.find_element_by_id('com.iexbuy.ihg:id/continuePayBtn').click() #继续支付
        el5 =self.driver.find_element_by_id('com.iexbuy.ihg:id/weixingPay').click()  #选择微信
        el6 =self.driver.find_element_by_id('com.iexbuy.ihg:id/submitPayBtn').click() #确认支付
        el7 =self.driver.find_element_by_id('android:id/text2')
        try:
            self.assertEqual(el7.text.encode('utf-8'), '微信安全支付')
        except:
            self.screencap(self.driver, name='10test_0012')
            self.assertEqual(el7.text.encode('utf-8'), '微信安全支付')
