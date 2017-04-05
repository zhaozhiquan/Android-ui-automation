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
	u'''登录'''
	def setUp(self):
		#self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.xuanyi.mbzj.appgame','com.xuanyi.mbzj.SplashActivity'))
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.zhankaigame.destiny.appgame', 'com.zhankaigame.destiny.RenWanTangSplashActivity'))
		#智能等待
		self.driver.implicitly_wait(10)
		self.driver.implicitly_wait(10)
		self.ele = self.get_col(4,6) #元素列
		self.exp = self.get_col(4,7) #预期结果列
		self.case_id = self.get_col(4,0) #case id 列
		self.preset = self.get_col(4,2) #预置条件列
		self.using = self.get_col(4, 5)  # 查找元素方式列
		#self.by_id(self.driver,'com.zhankaigame.destiny.appgame:id/button_1').click()

	def tearDown(self):
		self.driver.quit()
	def test_4001(self):
		u'''账号输入为空'''
		el = self.element(self.driver,self.using[1], self.ele[1])  # 账号输入框
		el2 = self.element(self.driver,self.using[2], self.ele[2])  # 密码输入框
		for i in range(10):
			el.clear()
		for i  in  range(10):
			el2.clear()
		self.element(self.driver,self.using[3],self.ele[3]).click()  #登录按钮
		el4 = self.element(self.driver,self.using[4],self.ele[4])    #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[1])
		self.dy(self.driver, unicode(el4.text), self.exp[1], self.case_id[1])  # 断言+截图
	def test_4002(self):
		u'''账号输入不为空，密码为空'''
		for i in range(10):
			el = self.element(self.driver,self.using[5],self.ele[5])   #账号输入框
			el.clear()
			el.send_keys(self.preset[5].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[5]:
				break
		el2 = self.element(self.driver, self.using[6],self.ele[6])  # 密码输入框
		for i  in  range(5):
			el2.clear()
		self.element(self.driver,self.using[7],self.ele[7]).click()  #登录按钮
		el4 = self.element(self.driver,self.using[8],self.ele[8])    #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[5])
		self.dy(self.driver, unicode(el4.text), self.exp[5], self.case_id[5])  # 断言+截图
	def test_4003(self):
		u'''正确账号，错误密码'''

		for i in range(10):
			el = self.element(self.driver,self.using[9], self.ele[9])  # 账号输入框
			el.clear()
			el.send_keys(self.preset[9].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[9]:
				break
		el2 = self.element(self.driver,self.using[10],self.ele[10])  #密码输入框
		for i in range(5):
			el2.clear()
		el2.send_keys(self.preset[10].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[11],self.ele[11]).click()  #登录按钮
		el4 = self.element(self.driver,self.using[12],self.ele[12])    #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[9])
		self.dy(self.driver, unicode(el4.text), self.exp[9], self.case_id[9])  # 断言+截图
	def test_4004(self):
		u'''错误账号，正确密码'''
		for i in range(10):
			el = self.element(self.driver,self.using[13],self.ele[13])   #账号输入框
			el.clear()
			el.send_keys(self.preset[13].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[13]:
				break
		el2 = self.element(self.driver,self.using[14],self.ele[14])  #密码输入框
		for i in range(6):
			el2.clear()
		el2.send_keys(self.preset[14].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[15],self.ele[15]).click()  #登录按钮
		el4 = self.element(self.driver,self.using[16],self.ele[16])    #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[13])
		self.dy(self.driver, unicode(el4.text), self.exp[13], self.case_id[13])  # 断言+截图
	def test_4005(self):
		u'''错误账号，错误密码'''
		for i in range(10):
			el = self.element(self.driver,self.using[17],self.ele[17])   #账号输入框
			el.clear()
			el.send_keys(self.preset[17].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[17]:
				break
		el2 = self.element(self.driver,self.using[18],self.ele[18])  #密码输入框
		for i in range(5):
			el2.clear()
		el2.send_keys(self.preset[18].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[19],self.ele[19]).click()  #登录按钮
		el4 = self.element(self.driver,self.using[20],self.ele[20])    #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[17])
		self.dy(self.driver, unicode(el4.text), self.exp[17], self.case_id[17])  # 断言+截图
	def test_4006(self):
		u'''正确账号，密码少于6位'''
		for i in range(10):
			el = self.element(self.driver,self.using[21],self.ele[21])   #账号输入框
			el.clear()
			el.send_keys(self.preset[21].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[21]:
				break
		el2 = self.element(self.driver,self.using[22],self.ele[22])  #密码输入框
		for i in range(6):
			el2.clear()
		el2.send_keys(self.preset[22].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[23],self.ele[23]).click()  #登录按钮
		el4 = self.element(self.driver,self.using[24],self.ele[24])    #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[21])
		self.dy(self.driver, unicode(el4.text), self.exp[21], self.case_id[21])  # 断言+截图
	def test_4007(self):
		u'''正确账号，正确密码'''
		for i in range(10):
			el = self.element(self.driver,self.using[25],self.ele[25])   #账号输入框
			el.clear()
			el.send_keys(self.preset[25].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[25]:
				break
		el2 = self.element(self.driver,self.using[26],self.ele[26])  #密码输入框
		for i in range(5):
			el2.clear()
		el2.send_keys(self.preset[26].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[27],self.ele[27]).click()  #登录按钮

		LOGIN_BUTTON = self.element_or_none(self.driver,self.using[28], self.ele[28])
		print unicode('测试结果: %s' % LOGIN_BUTTON)
		print unicode('预期结果: 元素不为空')
		self.dy_IsNone(self.driver,LOGIN_BUTTON,self.case_id[25])

	def test_4008(self):
		u'''登录界面，输入完成 ，点击右上角X按钮'''
		for i in range(10):
			el = self.element(self.driver,self.using[29],self.ele[29])   #账号输入框
			el.clear()
			el.send_keys(self.preset[29].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[29]:
				break

		el2 = self.element(self.driver,self.using[30],self.ele[30])  #密码输入框
		for i in range(5):
			el2.clear()
		el2.send_keys(self.preset[30].encode('utf-8').decode("utf-8"))

		self.element(self.driver,self.using[31],self.ele[31]).click()  #返回按钮

		LOGIN_BUTTON = self.element_or_none(self.driver,self.using[32], self.ele[32])
		print unicode('测试结果: %s' % LOGIN_BUTTON)
		print unicode('预期结果: 元素不为空')
		self.dy_IsNone(self.driver,LOGIN_BUTTON,self.case_id[29])
	def test_4009(self):
		u'''登录多个账号，查看记住账号'''
		self.element(self.driver,self.using[33],self.ele[33]).click()   #记住列表账号按钮
		el2 = self.elements(self.driver,self.using[34],self.ele[34])
		a = len(el2)
		print unicode('测试结果: %s' % a)
		print unicode('预期结果: %s' % int(self.exp[33]))
		self.dy(self.driver,a,int(self.exp[33]),self.case_id[33])
	def test_4010(self):
		u'''选择列表中的账号登录'''
		self.element(self.driver,self.using[35], self.ele[35]).click()  # 记住列表账号按钮
		el2 = self.elements(self.driver, self.using[36],self.ele[36])
		el2[1].click()                                       #选择列表第二个账号

		el3 = self.element(self.driver,self.using[37],self.ele[37])          #密码输入框
		el3.clear()
		el3.send_keys(self.preset[37].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[38],self.ele[38]).click() #登录按钮

		LOGIN_BUTTON = self.element_or_none(self.driver,self.using[39], self.ele[39])
		print unicode('测试结果: %s' % LOGIN_BUTTON)
		print unicode('预期结果: 元素不为空')
		self.dy_IsNone(self.driver,LOGIN_BUTTON,self.case_id[35])

