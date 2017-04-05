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
	u'''手机号注册'''
	def setUp(self):
		#self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.xuanyi.mbzj.appgame','com.xuanyi.mbzj.SplashActivity'))
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.zhankaigame.destiny.appgame', 'com.zhankaigame.destiny.RenWanTangSplashActivity'))
		#智能等待
		self.driver.implicitly_wait(10)
		self.ele = self.get_col(2,6) #元素列
		self.exp = self.get_col(2,7) #预期结果列
		self.case_id = self.get_col(2,0) #case id 列
		self.preset = self.get_col(2,2) #预置条件列
		self.using = self.get_col(2, 5)  # 查找元素方式列
		#self.by_id(self.driver,'com.zhankaigame.destiny.appgame:id/button_1').click()

	def tearDown(self):
		self.driver.quit()
	def test_2001(self):
		u'''手机号注册，输入为空'''
		self.element(self.driver,self.using[1],self.ele[1]).click()  #登录界面注册按钮
		self.element(self.driver,self.using[2],self.ele[2]).click()  #手机号注册
		#el3 = self.by_name(self.driver, self.ele[89])   手机号输入框
		self.element(self.driver,self.using[4],self.ele[4]).click()   #发送短信
		el5 =self.element(self.driver,self.using[5],self.ele[5])            #提示语
		print unicode('测试结果: %s' % el5.text)
		print unicode('预期结果: %s' % self.exp[1])
		self.dy(self.driver,unicode(el5.text),self.exp[1],self.case_id[1]) #断言+截图
	def test_2002(self):
		u'''手机号注册，输入为空格'''
		self.element(self.driver,self.using[6],self.ele[6]).click()  #登录界面注册按钮
		self.element(self.driver,self.using[7],self.ele[7]).click()  #手机号注册
		for i in range(10):
			el3 =self.element(self.driver,self.using[8],self.ele[8])        #手机号输入框
			el3.clear()
			el3.send_keys(self.preset[8].encode('utf-8').decode("utf-8"))
			if unicode(el3.text) == self.preset[8]:
				break
		self.element(self.driver,self.using[9],self.ele[9]).click()   #发送短信
		el5 =self.element(self.driver,self.using[10],self.ele[10])            #提示语
		print unicode('测试结果: %s' % el5.text)
		print unicode('预期结果: %s' % self.exp[6])
		self.dy(self.driver,unicode(el5.text),self.exp[6],self.case_id[6]) #断言+截图
	def test_2003(self):
		u'''手机号注册，输入10位数'''
		self.element(self.driver,self.using[11],self.ele[11]).click()  #登录界面注册按钮
		self.element(self.driver,self.using[12],self.ele[12]).click()  #手机号注册
		for i in range(10):
			el3 =self.element(self.driver,self.using[13],self.ele[13])        #手机号输入框
			el3.clear()
			el3.send_keys(self.preset[13].encode('utf-8').decode("utf-8"))
			if unicode(el3.text) == self.preset[13]:
				break
		self.element(self.driver,self.using[14],self.ele[14]).click()   #发送短信
		el5 =self.element(self.driver,self.using[15],self.ele[15])            #提示语
		print unicode('测试结果: %s' % el5.text)
		print unicode('预期结果: %s' % self.exp[11])
		self.dy(self.driver,unicode(el5.text),self.exp[11],self.case_id[11]) #断言+截图
	def test_2004(self):
		u'''手机号注册，输入11位数'''
		self.element(self.driver,self.using[16],self.ele[16]).click()  #登录界面注册按钮
		self.element(self.driver,self.using[17],self.ele[17]).click()  #手机号注册
		for i in range(10):
			el3 =self.element(self.driver,self.using[18],self.ele[18])        #手机号输入框
			el3.clear()
			el3.send_keys(self.preset[18].encode('utf-8').decode("utf-8"))
			if unicode(el3.text) == self.preset[18]:
				break
		self.element(self.driver,self.using[19],self.ele[19]).click()   #发送短信
		el5 =self.element(self.driver,self.using[20],self.ele[20])            #提示语
		print unicode('测试结果: %s' % el5.text)
		print unicode('预期结果: %s' % self.exp[16])
		self.dy(self.driver,unicode(el5.text),self.exp[16],self.case_id[16]) #断言+截图
	def test_2005(self):
		u'''手机号注册，输入12位数'''
		self.element(self.driver,self.using[21],self.ele[21]).click()  #登录界面注册按钮
		self.element(self.driver,self.using[22],self.ele[22]).click()  #手机号注册
		for i in range(10):
			el3 =self.element(self.driver,self.using[23],self.ele[23])        #手机号输入框
			el3.clear()
			el3.send_keys(self.preset[23].encode('utf-8').decode("utf-8"))
			if unicode(el3.text) == self.preset[23]:
				break
		self.element(self.driver,self.using[24],self.ele[24]).click()   #发送短信
		el5 =self.element(self.driver,self.using[25],self.ele[25])            #提示语
		print unicode('测试结果: %s' % el5.text)
		print unicode('预期结果: %s' % self.exp[21])
		self.dy(self.driver,unicode(el5.text),self.exp[21],self.case_id[21]) #断言+截图
	def test_2006(self):
		u'''手机号注册，输入已注册手机号'''
		self.element(self.driver,self.using[26],self.ele[26]).click()  #登录界面注册按钮
		self.element(self.driver,self.using[26],self.ele[27]).click()  #手机号注册
		for i in range(10):
			el3 =self.element(self.driver,self.using[28],self.ele[28])        #手机号输入框
			el3.clear()
			el3.send_keys(self.preset[28].encode('utf-8').decode("utf-8"))
			if unicode(el3.text) == self.preset[28]:
				break
		self.element(self.driver,self.using[29],self.ele[29]).click()   #发送短信
		el5 =self.element(self.driver,self.using[30],self.ele[30])            #提示语
		print unicode('测试结果: %s' % el5.text)
		print unicode('预期结果: %s' % self.exp[26])
		self.dy(self.driver,unicode(el5.text),self.exp[26],self.case_id[26]) #断言+截图
	def test_2007(self):
		u'''手机号注册，正确手机号，验证码为空'''
		self.element(self.driver,self.using[31],self.ele[31]).click()  #登录界面注册按钮
		self.element(self.driver,self.using[22],self.ele[32]).click()  #手机号注册
		for i in range(10):
			el3 =self.element(self.driver,self.using[33],self.ele[33])        #手机号输入框
			el3.clear()
			el3.send_keys(self.preset[33].encode('utf-8').decode("utf-8"))
			if unicode(el3.text) == self.preset[33]:
				break
		#el4 = self.by_id(self.driver,self.ele[120])         验证码输入
		self.element(self.driver,self.using[35],self.ele[35]).click()   #注册按钮
		el6= self.element(self.driver,self.using[36],self.ele[36])              #提示语
		print unicode('测试结果: %s' % el6.text)
		print unicode('预期结果: %s' % self.exp[31])
		self.dy(self.driver,unicode(el6.text),self.exp[31],self.case_id[31]) #断言+截图
	def test_2008(self):
		u'''手机号注册，正确手机号，错误验证码'''
		self.element(self.driver,self.using[37],self.ele[37]).click()  #登录界面注册按钮
		self.element(self.driver,self.using[38],self.ele[38]).click()  #手机号注册
		for i in range(10):
			el3 =self.element(self.driver,self.using[39],self.ele[39])        #手机号输入框
			el3.clear()
			el3.send_keys(self.preset[39].encode('utf-8').decode("utf-8"))
			if unicode(el3.text) == self.preset[39]:
				break
		for i in range(10):
			el4 = self.element(self.driver,self.using[40],self.ele[40])         #验证码输入
			el4.clear()
			el4.send_keys(self.preset[40].encode('utf-8').decode("utf-8"))
			if unicode(el4.text) == self.preset[40]:
				break
		self.element(self.driver,self.using[41],self.ele[41]).click()   #注册按钮
		el6= self.element(self.driver,self.using[42],self.ele[42])              #提示语
		print unicode('测试结果: %s' % el6.text)
		print unicode('预期结果: %s' % self.exp[37])
		self.dy(self.driver,unicode(el6.text),self.exp[37],self.case_id[37]) #断言+截图
	def test_2009(self):
		u'''手机号注册，输入完成 ，点击右上角返回按钮'''
		self.element(self.driver,self.using[43],self.ele[43]).click()  #登录界面注册按钮
		self.element(self.driver,self.using[44],self.ele[44]).click()  #手机号注册
		for i in range(10):
			el3 =self.element(self.driver,self.using[45],self.ele[45])        #手机号输入框
			el3.clear()
			el3.send_keys(self.preset[45].encode('utf-8').decode("utf-8"))
			if unicode(el3.text) == self.preset[45]:
				break
		for i in range(10):
			el4 = self.element(self.driver,self.using[46],self.ele[46])         #验证码输入
			el4.clear()
			el4.send_keys(self.preset[46].encode('utf-8').decode("utf-8"))
			if unicode(el4.text) == self.preset[46]:
				break
		self.element(self.driver,self.using[47],self.ele[47]).click()   #返回按钮
		el6= self.element(self.driver,self.using[48],self.ele[48])              #登录界面 登录按钮
		print unicode('测试结果: %s' % el6.text)
		print unicode('预期结果: %s' % self.exp[43])
		self.dy(self.driver,unicode(el6.text),self.exp[43],self.case_id[43]) #断言+截图

#####################################################################################
	def phone_registration(self):
		# 手机号注册验证吗公用模块
		self.element(self.driver, self.using[49],self.ele[49]).click()  # 登录界面注册按钮
		self.element(self.driver, self.using[50],self.ele[50]).click()  # 手机号注册
		for i in range(10):
			el3 = self.element(self.driver,self.using[51], self.ele[51])  # 手机号输入框
			el3.clear()
			el3.send_keys(self.preset[51].encode('utf-8').decode("utf-8"))
			if unicode(el3.text) == self.preset[51]:
				break
		self.element(self.driver,self.using[52], self.ele[52]).click()  # 发送验证码
		for i in range(10):
			el4 = self.element(self.driver,self.using[53], self.ele[53])  # 验证码输入
			el4.clear()
			el4.send_keys(self.preset[53].encode('utf-8').decode("utf-8"))
			if unicode(el4.text) == self.preset[53]:
				break
		self.element(self.driver,self.using[54], self.ele[54]).click()  # 注册按钮
######################################################################################
	def test_2010(self):
		u'''手机号注册，正确手机号，正确验证码'''
		self.phone_registration()
		el= self.element(self.driver,self.using[55],self.ele[55])              #提示语
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[49].encode('utf-8'))
		self.dy(self.driver,unicode(el.text),self.exp[49],self.case_id[49]) #断言+截图

	def test_2011(self):
		u'''设置密码为空'''
		self.phone_registration()
		self.element(self.driver, self.using[57],self.ele[57]).click()  #设置密码按钮
		el = self.element(self.driver,self.using[58], self.ele[58])  # 提示语
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[56].encode('utf-8'))
		self.dy(self.driver,unicode(el.text),self.exp[56],self.case_id[56]) #断言+截图

	def test_2012(self):
		u'''设置密码和确认密码为少6位'''
		self.phone_registration()
		el3 = self.element(self.driver,self.using[60], self.ele[60])  # 密码输入框
		el3.clear()
		el3.send_keys(self.preset[60].encode('utf-8').decode("utf-8"))

		el4 = self.element(self.driver,self.using[61], self.ele[61])  # 确定密码输入框
		el4.clear()
		el4.send_keys(self.preset[61].encode('utf-8').decode("utf-8"))

		self.element(self.driver,self.using[62], self.ele[62]).click()  #设置密码按钮
		el = self.element(self.driver,self.using[63], self.ele[63])  # 提示语
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[59].encode('utf-8'))
		self.dy(self.driver,unicode(el.text),self.exp[59],self.case_id[59]) #断言+截图

	def test_2013(self):
		u'''设置密码和确认密码不一致'''
		self.phone_registration()
		el3 = self.element(self.driver, self.using[65],self.ele[65])  # 密码输入框
		el3.clear()
		el3.send_keys(self.preset[65].encode('utf-8').decode("utf-8"))

		el4 = self.element(self.driver,self.using[66], self.ele[66])  # 确定密码输入框
		el4.clear()
		el4.send_keys(self.preset[66].encode('utf-8').decode("utf-8"))

		self.element(self.driver,self.using[67], self.ele[67]).click()  #设置密码按钮
		el = self.element(self.driver,self.using[68], self.ele[68])  # 提示语
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[64].encode('utf-8'))
		self.dy(self.driver,unicode(el.text),self.exp[64],self.case_id[64]) #断言+截图

	def test_2014(self):
		u'''设置6位数密码'''
		self.phone_registration()
		el3 = self.element(self.driver,self.using[70], self.ele[70])  # 密码输入框
		el3.clear()
		el3.send_keys(self.preset[70].encode('utf-8').decode("utf-8"))

		el4 = self.element(self.driver,self.using[71], self.ele[71])  # 确定密码输入框
		el4.clear()
		el4.send_keys(self.preset[71].encode('utf-8').decode("utf-8"))

		self.element(self.driver, self.using[72],self.ele[72]).click()  #设置密码按钮

		LOGIN_BUTTON = self.element_or_none(self.driver, self.using[73],self.ele[73])
		print unicode('测试结果: %s' % LOGIN_BUTTON)
		print unicode('预期结果: 元素不为空')
		self.dy_IsNone(self.driver,LOGIN_BUTTON,self.case_id[69])

