#!/usr/bin/env python
# coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep, strftime
import HTMLTestRunner
import random
import shutil
import public.methods as t
import public.case_xls as xl
class AndroidSDK(unittest.TestCase,t.Methods,xl.Case_xls):
	u'''第三方登录'''
	def setUp(self):
		# self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.xuanyi.mbzj.appgame','com.xuanyi.mbzj.SplashActivity'))
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.zhankaigame.destiny.appgame', 'com.zhankaigame.destiny.RenWanTangSplashActivity'))
		# 智能等待
		self.driver.implicitly_wait(10)
		self.driver.implicitly_wait(10)
		self.ele = self.get_col(7, 6)  # 元素列
		self.exp = self.get_col(7, 7)  # 预期结果列
		self.case_id = self.get_col(7, 0)  # case id 列
		self.preset = self.get_col(7, 2)  # 预置条件列
		self.using = self.get_col(7, 5)  # 查找元素方式列
	def tearDown(self):
		self.driver.quit()

	def test_7001(self):
		u'''微信登录--取消'''
		self.element(self.driver,self.using[1], self.ele[1]).click()  #其他登录
		self.element(self.driver,self.using[2],self.ele[2]).click()     #微信
		sleep(5)
		self.tap(self.driver, (float(self.ele[3]), float(self.exp[3])))      #取消
		el1 =  self.element(self.driver,self.using[4], self.ele[4])
		print unicode('测试结果: %s' % el1.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[1].encode('utf-8'))
		self.dy(self.driver, unicode(el1.text), self.exp[1], self.case_id[1])

	def test_7002(self):
		u'''微博登录--取消'''
		self.element(self.driver, self.using[5],self.ele[5]).click()  #其他登录
		self.element(self.driver,self.using[6],self.ele[6]).click()     #微博
		self.element(self.driver,self.using[7],self.ele[7]).click()       #取消
		el1 =  self.element(self.driver,self.using[8], self.ele[8])
		print unicode('测试结果: %s' % el1.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[5].encode('utf-8'))
		self.dy(self.driver, unicode(el1.text), self.exp[5], self.case_id[5])

	def test_7003(self):
		u'''QQ登录--取消'''
		self.element(self.driver,self.using[9], self.ele[9]).click()  #其他登录
		self.element(self.driver,self.using[10],self.ele[10]).click()     #QQ
		self.element(self.driver,self.using[11],self.ele[11]).click()       #返回
		el1 =  self.element(self.driver,self.using[12], self.ele[12])
		print unicode('测试结果: %s' % el1.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[9].encode('utf-8'))
		self.dy(self.driver, unicode(el1.text), self.exp[9], self.case_id[9])

	def test_7004(self):
		u'''微信登录'''
		self.element(self.driver, self.using[13],self.ele[13]).click()  #其他登录
		self.element(self.driver,self.using[14],self.ele[14]).click()     #微信
		sleep(5)
		self.tap(self.driver,(float(self.ele[15]),float(self.exp[15])))  #授权登录

		LOGIN_BUTTON = self.element_or_none(self.driver,self.using[16], self.ele[16])
		print unicode('测试结果: %s' % LOGIN_BUTTON)
		print unicode('预期结果: 元素为空')
		self.dy_IsNone(self.driver,LOGIN_BUTTON,self.case_id[13])

	def test_7005(self):
		u'''微博登录'''
		self.element(self.driver,self.using[17], self.ele[17]).click()  #其他登录
		self.element(self.driver,self.using[18],self.ele[18]).click()     #微博
		self.element(self.driver, self.using[19],self.ele[19]).click()    # 授权登录

		LOGIN_BUTTON = self.element_or_none(self.driver,self.using[20], self.ele[20])
		print unicode('测试结果: %s' % LOGIN_BUTTON)
		print unicode('预期结果: 元素为空')
		self.dy_IsNone(self.driver,LOGIN_BUTTON,self.case_id[17])

	def test_7006(self):
		u'''QQ登录'''
		self.element(self.driver,self.using[21], self.ele[21]).click()  #其他登录
		self.element(self.driver,self.using[22],self.ele[22]).click()     #微博
		self.element(self.driver,self.using[23], self.ele[23]).click()    # 授权登录

		LOGIN_BUTTON = self.element_or_none(self.driver,self.using[24], self.ele[24])
		print unicode('测试结果: %s' % LOGIN_BUTTON)
		print unicode('预期结果: 元素为空')
		self.dy_IsNone(self.driver,LOGIN_BUTTON,self.case_id[21])

	def test_7007(self):
		u'''选择第三方界面，点击 X 按钮'''
		self.element(self.driver, self.using[25],self.ele[25]).click()  #其他登录
		self.element(self.driver,self.using[26],self.ele[26]).click()     #点击X
		LOGIN_BUTTON = self.element_or_none(self.driver,self.using[27], self.ele[27])
		print unicode('测试结果: %s' % LOGIN_BUTTON)
		print unicode('预期结果: 元素为空')
		self.dy_IsNone(self.driver,LOGIN_BUTTON,self.case_id[25])

	def test_7008(self):
		u'''选择第三方界面，点击账号登录'''
		self.element(self.driver,self.using[28], self.ele[28]).click()     #其他登录
		self.element(self.driver,self.using[29],self.ele[29]).click()     #账号登录
		el1 = self.element(self.driver,self.using[30],self.ele[30])        #查找登录按钮
		print unicode('测试结果: %s' % el1.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[28].encode('utf-8'))
		self.dy(self.driver, unicode(el1.text), self.exp[28], self.case_id[28])