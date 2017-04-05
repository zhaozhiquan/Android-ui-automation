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
	u'''忘记密码'''
	def setUp(self):
		#self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.xuanyi.mbzj.appgame','com.xuanyi.mbzj.SplashActivity'))
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.zhankaigame.destiny.appgame', 'com.zhankaigame.destiny.RenWanTangSplashActivity'))
		#智能等待
		self.driver.implicitly_wait(10)
		self.driver.implicitly_wait(10)
		self.ele = self.get_col(3,6) #元素列
		self.exp = self.get_col(3,7) #预期结果列
		self.case_id = self.get_col(3,0) #case id 列
		self.preset = self.get_col(3,2) #预置条件列
		self.using = self.get_col(3, 5)  # 查找元素方式列
		#self.by_id(self.driver,'com.zhankaigame.destiny.appgame:id/button_1').click()

	def tearDown(self):
		self.driver.quit()
	def test_3001(self):
		u'''忘记密码，输入为空'''
		self.element(self.driver,self.using[1],self.ele[1]).click()  #忘记密码
		#el2 = self.by_id(self.driver,self.ele[136])         #手机号输入框
		self.element(self.driver,self.using[3],self.ele[3]).click()   #发送短信
		el4 =self.element(self.driver,self.using[4],self.ele[4])           #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[1])
		self.dy(self.driver,unicode(el4.text),self.exp[1],self.case_id[1]) #断言+截图
	def test_3002(self):
		u'''忘记密码，输入10位数'''
		self.element(self.driver,self.using[5],self.ele[5]).click()  #忘记密码
		for i  in range(10):
			el2 = self.element(self.driver,self.using[6],self.ele[6])         #手机号输入框
			el2.clear()
			el2.send_keys(self.preset[6].encode('utf-8').decode("utf-8"))
			if unicode(el2.text) == self.preset[6]:
				break
		self.element(self.driver,self.using[7],self.ele[7]).click()   #发送短信
		el4 =self.element(self.driver,self.using[8],self.ele[8])           #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[5])
		self.dy(self.driver,unicode(el4.text),self.exp[5],self.case_id[5]) #断言+截图
	def test_3003(self):
		u'''忘记密码，输入11位数'''
		self.element(self.driver,self.using[9],self.ele[9]).click()  #忘记密码
		for i  in range(10):
			el2 = self.element(self.driver,self.using[10],self.ele[10])         #手机号输入框
			el2.clear()
			el2.send_keys(self.preset[10].encode('utf-8').decode("utf-8"))
			if unicode(el2.text) == self.preset[10]:
				break
		self.element(self.driver,self.using[11],self.ele[11]).click()   #发送短信
		el4 =self.element(self.driver,self.using[12],self.ele[12])           #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[9])
		self.dy(self.driver,unicode(el4.text),self.exp[9],self.case_id[9]) #断言+截图
	def test_3004(self):
		u'''忘记密码，输入12位数'''
		self.element(self.driver,self.using[13],self.ele[13]).click()  #忘记密码
		for i  in range(10):
			el2 = self.element(self.driver,self.using[14],self.ele[14])         #手机号输入框
			el2.clear()
			el2.send_keys(self.preset[14].encode('utf-8').decode("utf-8"))
			if unicode(el2.text) == self.preset[14]:
				break
		self.element(self.driver,self.using[15],self.ele[15]).click()   #发送短信
		el4 =self.element(self.driver,self.using[16],self.ele[16])           #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[13])
		self.dy(self.driver,unicode(el4.text),self.exp[13],self.case_id[13]) #断言+截图
	def test_3005(self):
		u'''忘记密码，正确手机号，验证码为空'''
		self.element(self.driver,self.using[17],self.ele[17]).click()  #忘记密码
		for i  in range(10):
			el2 = self.element(self.driver,self.using[18],self.ele[18])         #手机号输入框
			el2.clear()
			el2.send_keys(self.preset[18].encode('utf-8').decode("utf-8"))
			if unicode(el2.text) == self.preset[18]:
				break
		#el3 =self.by_id(self.driver,self.ele[19])          #验证码
		self.element(self.driver,self.using[20],self.ele[20]).click()        #下一步
		el5 =self.element(self.driver,self.using[21],self.ele[21])             #提示语
		print unicode('测试结果: %s' % el5.text)
		print unicode('预期结果: %s' % self.exp[17])
		self.dy(self.driver,unicode(el5.text),self.exp[17],self.case_id[17]) #断言+截图
	def test_3006(self):
		u'''忘记密码，正确手机号，错误验证码'''
		self.element(self.driver,self.using[22],self.ele[22]).click()  #忘记密码
		for i  in range(10):
			el2 = self.element(self.driver,self.using[23],self.ele[23])         #手机号输入框
			el2.clear()
			el2.send_keys(self.preset[23].encode('utf-8').decode("utf-8"))
			if unicode(el2.text) == self.preset[23]:
				break
		for i in range(10):
			el3 =self.element(self.driver,self.using[24],self.ele[24])          #验证码
			el3.clear()
			el3.send_keys(self.preset[24].encode('utf-8').decode("utf-8"))
			if unicode(el3.text) == self.preset[24]:
				break
		self.element(self.driver,self.using[25],self.ele[25]).click()        #下一步
		el5 =self.element(self.driver,self.using[26],self.ele[26])             #提示语
		print unicode('测试结果: %s' % el5.text)
		print unicode('预期结果: %s' % self.exp[22])
		self.dy(self.driver,unicode(el5.text),self.exp[22],self.case_id[22]) #断言+截图
	def test_3007(self):
		u'''忘记密码，输入未注册手机号'''
		self.element(self.driver,self.using[27],self.ele[27]).click()  #忘记密码
		for i  in range(10):
			el2 = self.element(self.driver,self.using[28],self.ele[28])         #手机号输入框
			el2.clear()
			el2.send_keys(self.preset[28].encode('utf-8').decode("utf-8"))
			if unicode(el2.text) == self.preset[28]:
				break
		self.element(self.driver,self.using[29],self.ele[29]).click()   #发送短信
		el4 =self.element(self.driver,self.using[30],self.ele[30])           #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[27])
		self.dy(self.driver,unicode(el4.text),self.exp[27],self.case_id[27]) #断言+截图
	def test_3008(self):
		u'''忘记密码，正确手机号，错误验证码'''
		self.element(self.driver,self.using[31],self.ele[31]).click()  #忘记密码
		for i  in range(10):
			el2 = self.element(self.driver,self.using[32],self.ele[32])         #手机号输入框
			el2.clear()
			el2.send_keys(self.preset[32].encode('utf-8').decode("utf-8"))
			if unicode(el2.text) == self.preset[32]:
				break
		for i in range(10):
			el3 =self.element(self.driver,self.using[33],self.ele[33])          #验证码
			el3.clear()
			el3.send_keys(self.preset[33].encode('utf-8').decode("utf-8"))
			if unicode(el3.text) == self.preset[33]:
				break
		self.element(self.driver,self.using[34],self.ele[34]).click()        #返回按钮
		el5 =self.element(self.driver,self.using[35],self.ele[35])             #登录界面 登录按钮
		print unicode('测试结果: %s' % el5.text)
		print unicode('预期结果: %s' % self.exp[31])
		self.dy(self.driver,unicode(el5.text),self.exp[31],self.case_id[31]) #断言+截图

		#####################################################################################
	def phone_registration(self):
		# 忘记密码验证码公用模块
		self.element(self.driver, self.using[36],self.ele[36]).click()  # 忘记密码
		for i in range(10):
			el3 = self.element(self.driver,self.using[37], self.ele[37])  # 手机号输入框
			el3.clear()
			el3.send_keys(self.preset[37].encode('utf-8').decode("utf-8"))
			if unicode(el3.text) == self.preset[37]:
				break
		self.element(self.driver,self.using[38], self.ele[38]).click()  # 发送验证码
		for i in range(10):
			el4 = self.element(self.driver,self.using[39], self.ele[39])  # 验证码输入
			el4.clear()
			el4.send_keys(self.preset[39].encode('utf-8').decode("utf-8"))
			if unicode(el4.text) == self.preset[39]:
				break
		self.element(self.driver,self.using[40], self.ele[40]).click()  # 下一步

		######################################################################################
	def test_3009(self):
		u'''忘记密码，正确手机号，正确验证码'''
		self.phone_registration()
		el = self.element(self.driver,self.using[41], self.ele[41])  #提示语
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[36].encode('utf-8'))
		self.dy(self.driver, unicode(el.text), self.exp[36], self.case_id[36])  # 断言+截图

	def test_3010(self):
		u'''新密码，输入为空'''
		self.phone_registration()
		self.element(self.driver,self.using[43], self.ele[43]).click()  #下一步
		el = self.element(self.driver,self.using[44],self.ele[44])        #提示语
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[42].encode('utf-8'))
		self.dy(self.driver, unicode(el.text), self.exp[42], self.case_id[42])  # 断言+截图

	def test_3011(self):
		u'''新密码，密码和确认密码为少6位'''
		self.phone_registration()
		el3 = self.element(self.driver,self.using[46], self.ele[46])  # 密码输入框
		el3.clear()
		el3.send_keys(self.preset[46].encode('utf-8').decode("utf-8"))

		el4 = self.element(self.driver,self.using[47], self.ele[47])  # 确定密码输入框
		el4.clear()
		el4.send_keys(self.preset[47].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[48], self.ele[48]).click()    #下一步
		el = self.self.using[73],(self.driver,self.using[49],self.ele[49])          #提示语
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[45].encode('utf-8'))
		self.dy(self.driver, unicode(el.text), self.exp[45], self.case_id[45])  # 断言+截图

	def test_3012(self):
		u'''新密码，密码和确认密码不一致'''
		self.phone_registration()
		el3 = self.element(self.driver,self.using[51], self.ele[51])  # 密码输入框
		el3.clear()
		el3.send_keys(self.preset[51].encode('utf-8').decode("utf-8"))

		el4 = self.element(self.driver,self.using[52], self.ele[52])  # 确定密码输入框
		el4.clear()
		el4.send_keys(self.preset[52].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[53], self.ele[53]).click()    #下一步
		el = self.element(self.driver,self.using[54],self.ele[54])          #提示语
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[50].encode('utf-8'))
		self.dy(self.driver, unicode(el.text), self.exp[50], self.case_id[50])  # 断言+截图

	def test_3013(self):
		u'''新密码，密码和确认密码6位'''
		self.phone_registration()
		el3 = self.element(self.driver,self.using[56], self.ele[56])  # 密码输入框
		el3.clear()
		el3.send_keys(self.preset[56].encode('utf-8').decode("utf-8"))

		el4 = self.element(self.driver,self.using[57], self.ele[57])  # 确定密码输入框
		el4.clear()
		el4.send_keys(self.preset[57].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[58], self.ele[58]).click()    #下一步
		el = self.element(self.driver,self.using[59],self.ele[59])          #提示语
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[55].encode('utf-8'))
		self.dy(self.driver, unicode(el.text), self.exp[55], self.case_id[55])  # 断言+截图