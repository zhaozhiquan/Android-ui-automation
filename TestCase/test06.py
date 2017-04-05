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
	u'''账号安全--更改密码'''
	def setUp(self):
		#self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.xuanyi.mbzj.appgame','com.xuanyi.mbzj.SplashActivity'))
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.zhankaigame.destiny.appgame', 'com.zhankaigame.destiny.RenWanTangSplashActivity'))
		#智能等待
		self.driver.implicitly_wait(10)
		self.ele = self.get_col(6,6) #元素列
		self.exp = self.get_col(6,7) #预期结果列
		self.case_id = self.get_col(6,0) #case id 列
		self.preset = self.get_col(6,2) #预置条件列
		self.using = self.get_col(6, 5)  # 查找元素方式列
		#self.by_id(self.driver, 'com.zhankaigame.destiny.appgame:id/button_1').click()
		#悬浮标 坐标
		self.suspend = (float(self.ele[2]), float(self.exp[2]))
		# ele[n] 为width,exp[n] 为height
	def tearDown(self):
		self.driver.quit()
	def test_6001(self):
		u'''更改密码，原密码输入空，密码输入6位数字，确认密码与密码一致'''
		self.element(self.driver, 'id','iv_other_account').click()  # 记住列表账号按钮
		list1 = self.elements(self.driver,'id', 'tv_account_name')
		list1[2].click()  # 选择列表第三个账号
		input1 = self.element(self.driver, 'id','editTextPassWord')  # 密码输入框
		input1.clear()
		input1.send_keys('qwerty123')  #选择回玩家号注册的账号
		self.element(self.driver,'name', '登  录').click()  # 登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[4], self.ele[4]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[5], self.ele[5]).click()  # 更改登录密码
		#el =self.by_id(self.driver,self.ele[6])      #原密码
		el2 = self.element(self.driver,self.using[7],self.ele[7])     #新密码
		el2.clear()
		el2.send_keys(self.preset[7].encode('utf-8').decode("utf-8"))
		el3 = self.element(self.driver,self.using[8], self.ele[8])    # 确认密码
		el3.clear()
		el3.send_keys(self.preset[8].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[9],self.ele[9]).click()
		el4 = self.element(self.driver,self.using[10],self.ele[10])     #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[4])
		self.dy(self.driver, unicode(el4.text), self.exp[1], self.case_id[1])
	def test_6002(self):
		u'''更改密码，输入正确原密码，密码输入为空，确认密码为非空'''
		self.element(self.driver,self.using[11], self.ele[11]).click()  # 登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[14], self.ele[14]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[15], self.ele[15]).click()  # 更改登录密码
		el =self.element(self.driver,self.using[16],self.ele[16])      #原密码
		el.clear()
		el.send_keys(self.preset[16].encode('utf-8').decode("utf-8"))
		#el2 = self.by_id(self.driver,self.ele[17])     #新密码
		#el2.clear()
		#el2.send_keys(self.preset[17].encode('utf-8').decode("utf-8"))
		el3 = self.element(self.driver,self.using[18], self.ele[18])    # 确认密码
		el3.clear()
		el3.send_keys(self.preset[18].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[19],self.ele[19]).click()
		el4 = self.element(self.driver,self.using[20],self.ele[20])     #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[11])
		self.dy(self.driver, unicode(el4.text), self.exp[11], self.case_id[11])
	def test_6003(self):
		u'''更改密码，输入正确原密码，密码输入11位字母，确认密码为空'''
		self.element(self.driver,self.using[21], self.ele[21]).click()  # 登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[24], self.ele[24]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[25], self.ele[25]).click()  # 更改登录密码
		el =self.element(self.driver,self.using[26],self.ele[26])      #原密码
		el.clear()
		el.send_keys(self.preset[26].encode('utf-8').decode("utf-8"))
		el2 = self.element(self.driver,self.using[27],self.ele[27])     #新密码
		el2.clear()
		el2.send_keys(self.preset[27].encode('utf-8').decode("utf-8"))
		#el3 = self.by_id(self.driver, self.ele[28])    # 确认密码
		#el3.clear()
		#el3.send_keys(self.preset[28].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[29],self.ele[29]).click()
		el4 = self.element(self.driver,self.using[30],self.ele[30])     #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[21])
		self.dy(self.driver, unicode(el4.text), self.exp[21], self.case_id[21])
	def test_6004(self):
		u'''更改密码，输入错误原密码，密码输入6位字母+数字，确认密码与密码一致'''
		self.element(self.driver,self.using[31], self.ele[31]).click()  # 登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver, self.using[34],self.ele[34]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver, self.using[35],self.ele[35]).click()  # 更改登录密码
		el =self.element(self.driver,self.using[36],self.ele[36])      #原密码
		el.clear()
		el.send_keys(self.preset[36].encode('utf-8').decode("utf-8"))
		el2 = self.element(self.driver,self.using[37],self.ele[37])     #新密码
		el2.clear()
		el2.send_keys(self.preset[37].encode('utf-8').decode("utf-8"))
		el3 = self.element(self.driver,self.using[38], self.ele[38])    # 确认密码
		el3.clear()
		el3.send_keys(self.preset[38].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[39],self.ele[39]).click()
		el4 = self.element(self.driver,self.using[40],self.ele[40])     #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[31])
		self.dy(self.driver, unicode(el4.text), self.exp[31], self.case_id[31])
	def test_6005(self):
		u'''更改密码，输入正确原密码，密码输入5位字母+数字，确认密码与密码一致'''
		self.element(self.driver,self.using[41], self.ele[41]).click()  # 登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[44], self.ele[44]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[45], self.ele[45]).click()  # 更改登录密码
		el =self.element(self.driver,self.using[46],self.ele[46])      #原密码
		el.clear()
		el.send_keys(self.preset[46].encode('utf-8').decode("utf-8"))
		el2 = self.element(self.driver,self.using[47],self.ele[47])     #新密码
		el2.clear()
		el2.send_keys(self.preset[47].encode('utf-8').decode("utf-8"))
		el3 = self.element(self.driver,self.using[48], self.ele[48])    # 确认密码
		el3.clear()
		el3.send_keys(self.preset[48].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[49],self.ele[49]).click()
		el4 = self.element(self.driver,self.using[50],self.ele[50])     #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[41])
		self.dy(self.driver, unicode(el4.text), self.exp[41], self.case_id[41])
	def test_6006(self):
		u'''更改密码，输入正确原密码，密码输入8位字母+数字+符号，确认密码与密码不一致'''
		self.element(self.driver, self.using[51],self.ele[51]).click()  # 登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[54], self.ele[54]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[55], self.ele[55]).click()  # 更改登录密码
		el =self.element(self.driver,self.using[56],self.ele[56])      #原密码
		el.clear()
		el.send_keys(self.preset[56].encode('utf-8').decode("utf-8"))
		el2 = self.element(self.driver,self.using[57],self.ele[57])     #新密码
		el2.clear()
		el2.send_keys(self.preset[57].encode('utf-8').decode("utf-8"))
		el3 = self.element(self.driver,self.using[58], self.ele[58])    # 确认密码
		el3.clear()
		el3.send_keys(self.preset[58].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[59],self.ele[59]).click()
		el4 = self.element(self.driver,self.using[60],self.ele[60])     #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[51])
		self.dy(self.driver, unicode(el4.text), self.exp[51], self.case_id[51])
	def test_6007(self):
		u'''更改密码，输入正确原密码，密码输入10位字母+数字，确认密码与密码一致'''
		self.element(self.driver,self.using[61], self.ele[61]).click()  # 登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[64], self.ele[64]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[65], self.ele[65]).click()  # 更改登录密码
		el =self.element(self.driver,self.using[66],self.ele[66])      #原密码
		el.clear()
		el.send_keys(self.preset[66].encode('utf-8').decode("utf-8"))
		el2 = self.element(self.driver,self.using[67],self.ele[67])     #新密码
		el2.clear()
		el2.send_keys(self.preset[67].encode('utf-8').decode("utf-8"))
		el3 = self.element(self.driver,self.using[68], self.ele[68])    # 确认密码
		el3.clear()
		el3.send_keys(self.preset[68].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[69],self.ele[69]).click()
		el4 = self.elements(self.driver,self.using[70],self.ele[70])     #提示语
		print unicode('测试结果: %s' % el4[1].text)
		print unicode('预期结果: %s' % self.exp[61])
		self.dy(self.driver, unicode(el4[1].text), self.exp[61], self.case_id[61])
	def test_6008(self):
		u'''修改密码后登录'''
		el = self.element(self.driver,self.using[71],self.ele[71])      #密码输入框
		el.click()
		for i in range(10):
			self.driver.keyevent(123)
			self.driver.keyevent(67)

		el.send_keys(self.preset[71].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[72],self.ele[72]).click()  #登录按钮

		LOGIN_BUTTON = self.element_or_none(self.driver,self.using[73], self.ele[73])
		print unicode('测试结果: %s' % LOGIN_BUTTON)
		print unicode('预期结果: 元素不为空')
		self.dy_IsNone(self.driver,LOGIN_BUTTON,self.case_id[71])
	def test_6009(self):
		u'''查看消费记录'''
		self.element(self.driver, self.using[74],self.ele[74]).click()  # 登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[77], self.ele[77]).click()  # 消费记录
				break
			except:
				pass
		el = self.element(self.driver,self.using[78],self.ele[78])      #记录信息
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[74].encode('utf-8'))
		self.dy(self.driver, unicode(el.text), self.exp[74], self.case_id[74])