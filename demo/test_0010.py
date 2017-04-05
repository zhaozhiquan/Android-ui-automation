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
        u'''查看已支付订单'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_name('消费订单').click()
        el3 = self.driver.find_element_by_name('已支付').click()
        el4 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/itemImage')
        el4[0].click()
        el5 =self.driver.find_element_by_id('com.iexbuy.ihg:id/goHuiguoBtn').click()
        el6 =self.driver.find_element_by_id('com.iexbuy.ihg:id/buyCoinBtn')
        try:
            self.assertEqual(el6.text.encode('utf-8'), '充值金币')
        except:
            self.screencap(self.driver, name='11test_0001')
            self.assertEqual(el6.text.encode('utf-8'), '充值金币')
    def test_0002(self):
        u'''评价'''
        l = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_name('消费订单').click()
        el3 = self.driver.find_element_by_name('待评价').click()
        el4 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/itemTime')
        b = el4[0].text.encode('utf-8')
        el4[0].click()
        el5 = self.driver.find_element_by_id('com.iexbuy.ihg:id/ratingBar').click() # 选择星级
        el6 =self.driver.find_element_by_id('com.iexbuy.ihg:id/commentText').send_keys('好漂亮，好喜欢'.decode('utf-8'))
        el7 =self.driver.find_element_by_id('com.iexbuy.ihg:id/btnRight').click()  #保存
        el8 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/itemTime')
        try:
            self.assertNotEquals(el8[0].text.encode('utf-8'), b)
        except:
            self.screencap(self.driver, name='11test_0002')
            self.assertNotEquals(el8[0].text.encode('utf-8'), b)
    def test_0003(self):
        u'''换购待发货订单'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_name('换购订单').click()
        el3 = self.driver.find_element_by_name('待发货').click()
        el4 =self.driver.find_elements_by_id('com.iexbuy.ihg:id/itemImage')
        el4[0].click()
        el5 =self.driver.find_element_by_id('com.iexbuy.ihg:id/orderStatus')
        try:
            self.assertEquals(el5.text.encode('utf-8'),'(已支付)')
        except:
            self.screencap(self.driver, name='11test_0003')
            self.assertEquals(el5.text.encode('utf-8'), '(已支付)')
    def test_0004(self):
        u'''换购待发货订单'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_name('换购订单').click()
        el3 = self.driver.find_element_by_name('已完成').click()
        el4 =self.driver.find_elements_by_id('com.iexbuy.ihg:id/itemImage')
        el4[0].click()
        el5 =self.driver.find_element_by_id('com.iexbuy.ihg:id/orderStatus')
        try:
            self.assertEquals(el5.text.encode('utf-8'),'(已完成)')
        except:
            self.screencap(self.driver, name='11test_0004')
            self.assertEquals(el5.text.encode('utf-8'), '(已完成)')
    def test_0005(self):
        u'''钱包--规则'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 =self.driver.find_element_by_id('com.iexbuy.ihg:id/wallet_layout').click() #钱包
        el3 =self.driver.find_element_by_id('com.iexbuy.ihg:id/walletRule').click() #规则
        el4 =self.driver.find_element_by_id('com.iexbuy.ihg:id/finishTx')
        try:
            self.assertEquals(el4.text.encode('utf-8'), '规则')
        except:
            self.screencap(self.driver, name='11test_0005')
            elf.assertEquals(el4.text.encode('utf-8'), '规则')
    def test_0006(self):
        u'''钱包--充值'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 =self.driver.find_element_by_id('com.iexbuy.ihg:id/wallet_layout').click() #钱包
        el3 =self.driver.find_element_by_id('com.iexbuy.ihg:id/rechargeLayout').click() #充值
        el4 =self.driver.find_element_by_id('com.iexbuy.ihg:id/userMobile')
        try:
            self.assertEquals(el4.text.encode('utf-8'), 'tes********')
        except:
            self.screencap(self.driver, name='11test_0006')
            elf.assertEquals(el4.text.encode('utf-8'), 'tes********')
    def test_0007(self):
        u'''我的优惠券'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/couponLayout').click() #优惠券
        el3 =self.driver.find_element_by_id('com.iexbuy.ihg:id/txtTitle')
        try:
            self.assertEquals(el3.text.encode('utf-8'), '我的优惠券')
        except:
            self.screencap(self.driver, name='11test_0007')
            self.assertEquals(el3.text.encode('utf-8'), '我的优惠券')
    def test_0008(self):
        u'''邀请码'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/invi_layout').click() #邀请码
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/detailTx')
        try:
            self.assertEquals(el3.text.encode('utf-8'), 'cs14315')
        except:
            self.screencap(self.driver, name='11test_0008')
            self.assertEquals(el3.text.encode('utf-8'), 'cs14315')
    def test_0009(self):
        u'''下级会员'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/lower_layout').click() #下级会员
        el3 =self.driver.find_element_by_id('com.iexbuy.ihg:id/txtTitle')
        try:
            self.assertEquals(el3.text.encode('utf-8'), '下级会员')
        except:
            self.screencap(self.driver, name='11test_0009')
            self.assertEquals(el3.text.encode('utf-8'), '下级会员')
    def test_0010(self):
        u'''常见问题'''
        el = self.driver.find_element_by_name('个人中心').click()
        el2 =self.driver.find_element_by_id('com.iexbuy.ihg:id/questionLayout').click() #常见问题
        a = ['其他问题','消费问题', '换购问题','0购问题', '联系客服']
        el5 = self.driver.find_elements_by_id('com.iexbuy.ihg:id/itemTitle')
        for i in range(int(len(el5))):
            el5[i].click()
            el6 =self.driver.find_element_by_id('com.iexbuy.ihg:id/btnBack').click()
            try:
                self.assertEquals(el5[i].text.encode('utf-8'),a[i])
            except:
                self.screencap(self.driver, name='11test_0010-'+str(i))
                self.assertEquals(el5[i].text.encode('utf-8'), a[i])
    def test_0011(self):
        u'''服务与反馈'''
        a = ['其他问题', '消费问题', '换购问题', '0购问题', '联系客服']
        b =random.choice(a)
        el = self.driver.find_element_by_name('个人中心').click()
        el2 =self.driver.find_element_by_id('com.iexbuy.ihg:id/feebackLayout').click() #服务与反馈
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/radioButton1').click()
        el4 =self.driver.find_element_by_id('com.iexbuy.ihg:id/commentText').send_keys(b.decode('utf-8'))
        el5 = self.driver.find_element_by_id('com.iexbuy.ihg:id/btnRight').click()
        el6 =self.driver.find_elements_by_id('com.iexbuy.ihg:id/itemSubtitle')
        try:
            self.assertEquals(el6[0].text.encode('utf-8'), b)
        except:
            self.screencap(self.driver, name='11test_0011')
            self.assertEquals(el6[0].text.encode('utf-8'), b)
    def test_0012(self):
        u'''我要合作'''
        el = self.driver.find_element_by_name('个人中心').click()
        while(True):
            try:
                el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/cooperationLayout').click() #我要合作
                break
            except:
                self.up_swipe(self.driver)
        el3 = self.driver.find_element_by_id('com.iexbuy.ihg:id/txtTitle')
        try:
            self.assertEquals(el3.text.encode('utf-8'),'我要合作')
        except:
            self.screencap(self.driver, name='11test_0012')
            self.assertEquals(el6[0].text.encode('utf-8'),'我要合作')
    def test_0013(self):
        u'''我是商家-登陆'''
        el = self.driver.find_element_by_name('个人中心').click()
        while(True):
            try:
                el2 = self.driver.find_element_by_id('com.iexbuy.ihg:id/businessLayout').click() #我是商家
                break
            except:
                self.up_swipe(self.driver)
        el3 =self.driver.find_elements_by_xpath('//android.webkit.WebView/android.widget.EditText')
        el3[0].send_keys('哈哈'.decode('utf-8'))
        el3[1].send_keys('chen123456'.decode('utf-8'))
        el4 = self.driver.find_elements_by_xpath('//android.webkit.WebView/android.view.View')
        el4[1].click()
        el5 =self.driver.find_element_by_name('Pull')
        try:
            self.assertEquals(el5.get_attribute('name').encode('utf-8'), 'Pull')
        except:
            self.screencap(self.driver, name='11test_0013')
            self.assertEquals(el5.get_attribute('name').encode('utf-8'), 'Pull')
