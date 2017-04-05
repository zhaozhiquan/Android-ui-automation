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
	u'''账号安全--绑定手机号、绑定邮箱'''
	def setUp(self):
		#self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.xuanyi.mbzj.appgame','com.xuanyi.mbzj.SplashActivity'))
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.zhankaigame.destiny.appgame', 'com.zhankaigame.destiny.RenWanTangSplashActivity'))
		#智能等待
		self.driver.implicitly_wait(10)
		self.driver.implicitly_wait(10)
		self.ele = self.get_col(5,6) #元素列
		self.exp = self.get_col(5,7) #预期结果列
		self.case_id = self.get_col(5,0) #case id 列
		self.preset = self.get_col(5,2) #预置条件列
		self.using = self.get_col(5, 5)  # 查找元素方式列
		#self.by_id(self.driver,'com.zhankaigame.destiny.appgame:id/button_1').click()
		#悬浮标 坐标
		self.suspend =(float(self.ele[2]), float(self.exp[2]))
		# ele[n] 为width,exp[n] 为height
	def tearDown(self):
		self.driver.quit()
	def test_5001(self):
		u'''切换账号'''
		self.element(self.driver,self.using[1],self.ele[1]).click()  #登录按钮
		sleep(5)
		while(True):
			try :
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[4], self.ele[4]).click()  # 切换账号
				break
			except:
				pass
		self.element(self.driver,self.using[5],self.ele[5]).click()  #登录

		LOGIN_BUTTON = self.element_or_none(self.driver,self.using[6], self.ele[6])
		print unicode('测试结果: %s' % LOGIN_BUTTON)
		print unicode('预期结果: 元素不为空')
		self.dy_IsNone(self.driver,LOGIN_BUTTON,self.case_id[1])
	def test_5002(self):
		u'''账号安全，绑定手机号，输入为空'''
		self.element(self.driver,self.using[7],self.ele[7]).click()  #登录按钮
		sleep(5)
		while(True):
			try :
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[10],self.ele[10]).click() #账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[11],self.ele[11]).click() #绑定手机
		self.element(self.driver,self.using[12],self.ele[12]).click() #提交
		el = self.element(self.driver,self.using[13],self.ele[13])   #提示语
		print unicode('测试结果: %s' % el.text)
		print unicode('预期结果: %s' % self.exp[7])
		self.dy(self.driver, unicode(el.text), self.exp[7], self.case_id[7])
	def test_5003(self):
		u'''账号安全，绑定手机号，输入10位数字'''
		self.element(self.driver,self.using[14],self.ele[14]).click()  #登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver, self.using[17],self.ele[17]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[18], self.ele[18]).click()  # 绑定手机
		el = self.element(self.driver,self.using[19],self.ele[19])      #手机号输入框
		for i in range(10):
			el.clear()
			el.send_keys(self.preset[19].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[19]:
				break
		self.element(self.driver,self.using[20],self.ele[20]).click()  #提交
		el2 = self.element(self.driver,self.using[21],self.ele[21])
		print unicode('测试结果: %s' % el2.text)
		print unicode('预期结果: %s' % self.exp[14])
		self.dy(self.driver, unicode(el2.text), self.exp[14], self.case_id[14])

	def test_5004(self):
		u'''账号安全，绑定手机号，输入12位数字'''
		self.element(self.driver,self.using[22],self.ele[22]).click()  #登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[25], self.ele[25]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[26], self.ele[26]).click()  # 绑定手机
		el = self.element(self.driver,self.using[27],self.ele[27])      #手机号输入框
		for i in range(10):
			el.clear()
			el.send_keys(self.preset[27].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[27]:
				break
		self.element(self.driver,self.using[28],self.ele[28]).click()  #提交
		el2 = self.element(self.driver,self.using[29],self.ele[29])
		print unicode('测试结果: %s' % el2.text)
		print unicode('预期结果: %s' % self.exp[22])
		self.dy(self.driver, unicode(el2.text), self.exp[22], self.case_id[22])
	def test_5005(self):
		u'''账号安全，绑定手机号，输入已绑定手机'''
		self.element(self.driver,self.using[30],self.ele[30]).click()  #登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[33], self.ele[33]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[34], self.ele[34]).click()  # 绑定手机
		el = self.element(self.driver,self.using[35],self.ele[35])      #手机号输入框
		for i in range(10):
			el.clear()
			el.send_keys(self.preset[35].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[35]:
				break
		self.element(self.driver,self.using[36],self.ele[36]).click()  #提交
		el2 = self.element(self.driver,self.using[37],self.ele[37])
		print unicode('测试结果: %s' % el2.text)
		print unicode('预期结果: %s' % self.exp[30])
		self.dy(self.driver, unicode(el2.text), self.exp[30], self.case_id[30])
	def test_5006(self):
		u'''账号安全，绑定手机号，11位数字，验证为空'''
		self.element(self.driver,self.using[38],self.ele[38]).click()  #登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[41], self.ele[41]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[42], self.ele[42]).click()  # 绑定手机
		el = self.element(self.driver,self.using[43],self.ele[43])      #手机号输入框
		for i in range(10):
			el.clear()
			el.send_keys(self.preset[43].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[43]:
				break
		for i  in  range(2):
			self.element(self.driver,self.using[44],self.ele[44]).click()  #提交
			sleep(3)
		el2 = self.element(self.driver,self.using[45],self.ele[45])
		print unicode('测试结果: %s' % el2.text)
		print unicode('预期结果: %s' % self.exp[38])
		self.dy(self.driver, unicode(el2.text), self.exp[38], self.case_id[38])
	def test_5007(self):
		u'''账号安全，绑定手机号，11位数字，错误验证'''
		self.element(self.driver,self.using[46],self.ele[46]).click()  #登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver, self.using[49],self.ele[49]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[50], self.ele[50]).click()  # 绑定手机
		el = self.element(self.driver,self.using[51],self.ele[51])      #手机号输入框
		for i in range(10):
			el.clear()
			el.send_keys(self.preset[51].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[51]:
				break
		self.element(self.driver,self.using[52],self.ele[52]).click()  #提交
		el2 = self.element(self.driver,self.using[53],self.ele[53])    #验证码输入框
		for i in range(10):
			el2.clear()
			el2.send_keys(self.preset[53].encode('utf-8').decode("utf-8"))
			if unicode(el2.text) == self.preset[53]:
				break
		self.element(self.driver,self.using[52], self.ele[52]).click()  # 提交  使用上面提及的数据
		el3 = self.element(self.driver,self.using[54],self.ele[54])
		print unicode('测试结果: %s' % el3.text)
		print unicode('预期结果: %s' % self.exp[46])
		self.dy(self.driver, unicode(el3.text), self.exp[46], self.case_id[46])
	def test_5008(self):
		u'''账号安全，绑定邮箱，输入为空'''
		self.element(self.driver,self.using[55],self.ele[55]).click()  #登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[58], self.ele[58]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[59], self.ele[59]).click()  # 绑定邮箱
		self.element(self.driver,self.using[60], self.ele[60]).click()  # 提交
		el = self.element(self.driver,self.using[61],self.ele[61])      #提示语
		print unicode('测试结果: %s' % el.text)
		print unicode('预期结果: %s' % self.exp[55])
		self.dy(self.driver, unicode(el.text), self.exp[55], self.case_id[55])
	def test_5009(self):
		u'''输入错误的邮箱'''
		self.element(self.driver,self.using[62], self.ele[62]).click()  # 登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[65], self.ele[65]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[66], self.ele[66]).click()  # 绑定邮箱
		el = self.element(self.driver,self.using[67],self.ele[67])     #输入框
		for i  in range(10):
			el.clear()
			el.send_keys(self.preset[67].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[67]:
				break
		self.element(self.driver,self.using[68], self.ele[68]).click()  # 提交
		el2 = self.element(self.driver,self.using[69], self.ele[69])  # 提示语
		print unicode('测试结果: %s' % el2.text)
		print unicode('预期结果: %s' % self.exp[62])
		self.dy(self.driver, unicode(el2.text), self.exp[62], self.case_id[62])
	def test_5010(self):
		u'''输入正确的邮箱'''
		self.element(self.driver,self.using[70], self.ele[70]).click()  # 登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[73], self.ele[73]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[74], self.ele[74]).click()  # 绑定邮箱
		el = self.element(self.driver,self.using[75],self.ele[75])     #输入框
		for i  in range(10):
			el.clear()
			el.send_keys(self.preset[75].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[75]:
				break
		self.element(self.driver,self.using[76], self.ele[76]).click()  # 提交
		el2 = self.element(self.driver,self.using[77], self.ele[77])  # 提示语
		print unicode('测试结果: %s' % el2.text)
		print unicode('预期结果: %s' % self.exp[70])
		self.dy(self.driver, unicode(el2.text), self.exp[70], self.case_id[70])
	def test_5011(self):
		u'''输入已绑定的邮箱'''
		self.element(self.driver,self.using[78], self.ele[78]).click()  # 登录按钮
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[81], self.ele[81]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[82], self.ele[82]).click()  # 绑定邮箱
		el = self.element(self.driver,self.using[83],self.ele[83])     #输入框
		for i  in range(10):
			el.clear()
			el.send_keys(self.preset[83].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[83]:
				break
		self.element(self.driver,self.using[84], self.ele[84]).click()  # 提交
		el2 = self.element(self.driver,self.using[85], self.ele[85])  # 提示语
		print unicode('测试结果: %s' % el2.text)
		print unicode('预期结果: %s' % self.exp[78])
		self.dy(self.driver, unicode(el2.text), self.exp[78], self.case_id[78])

	def test_5012(self):
		u'''查看已绑定手机'''
		for i in range(10):
			el = self.element(self.driver,self.using[86],self.ele[86])     #账号输入框
			el.clear()
			el.send_keys(self.preset[86].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[86]:
				break
		el2 =self.element(self.driver,self.using[87],self.ele[87])    #密码输入框
		for i in range(3):
			el2.clear()
		el2.send_keys(self.preset[87].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[88],self.ele[88]).click()  #登录
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver, self.using[91],self.ele[91]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[92],self.ele[92]).click()  #解绑手机
		el3 = self.element(self.driver,self.using[93],self.ele[93])    #绑定手机号
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[86].encode('utf-8'))
		self.dy(self.driver, unicode(el3.text), self.exp[86], self.case_id[86])
	def test_5013(self):
		u'''过期验证码'''
		self.element(self.driver,self.using[94], self.ele[94]).click()  # 登录
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[97], self.ele[97]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[98], self.ele[98]).click()  # 解绑手机
		for i in range(10):
			el = self.element(self.driver,self.using[99],self.ele[99])     #验证码输入框
			el.clear()
			el.send_keys(self.preset[99].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[99]:
				break
		self.element(self.driver,self.using[100], self.ele[100]).click()   #解绑手机
		el2 = self.element(self.driver,self.using[101], self.ele[101])     #提示语
		print unicode('测试结果: %s' % el2.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[94].encode('utf-8'))
		self.dy(self.driver, unicode(el2.text), self.exp[94], self.case_id[94])
	def test_5014(self):
		u'''点击发送验证码'''
		for i in range(10):
			el = self.element(self.driver,self.using[102],self.ele[102])     #账号输入框
			el.clear()
			el.send_keys(self.preset[102].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[102]:
				break
		el2 =self.element(self.driver,self.using[103],self.ele[103])    #密码输入框
		for i in range(3):
			el2.clear()
		el2.send_keys(self.preset[103].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[104], self.ele[104]).click()  # 登录
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[107], self.ele[107]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[108], self.ele[108]).click()  # 解绑手机
		self.element(self.driver,self.using[109], self.ele[109]).click()  # 点击验证码
		el = self.element(self.driver,self.using[110], self.ele[110])
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[102].encode('utf-8'))
		self.dy(self.driver, unicode(el.text), self.exp[102], self.case_id[102])
	def test_5015(self):
		u'''空验证码'''
		self.element(self.driver,self.using[111], self.ele[111]).click()  # 登录
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[114], self.ele[114]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[115], self.ele[115]).click()  # 解绑手机
		self.element(self.driver, self.using[116],self.ele[116]).click()   #点击解绑手机
		el= self.element(self.driver,self.using[117], self.ele[117])     #提示语
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[111].encode('utf-8'))
		self.dy(self.driver, unicode(el.text), self.exp[111], self.case_id[111])

	def test_5016(self):
		u'''错误验证吗'''
		self.element(self.driver,self.using[118], self.ele[118]).click()  # 登录
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[121], self.ele[121]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[122], self.ele[122]).click()  # 解绑手机
		for i in range(10):
			el = self.element(self.driver,self.using[123],self.ele[123])     #验证码输入框
			el.clear()
			el.send_keys(self.preset[123].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[123]:
				break
		self.element(self.driver,self.using[124], self.ele[124]).click() #点击解绑手机
		el2 = self.element(self.driver,self.using[125], self.ele[125])
		print unicode('测试结果: %s' % el2.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[118].encode('utf-8'))
		self.dy(self.driver, unicode(el2.text), self.exp[118], self.case_id[118])

	def test_5017(self):
		u'''解绑手机'''
		self.element(self.driver,self.using[126],self.ele[126]).click()  #登录
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[129], self.ele[129]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[130],self.ele[130]).click()  #解绑手机
		for i in range(10):
			el3 = self.element(self.driver,self.using[131],self.ele[131])     #验证码输入框
			el3.clear()
			el3.send_keys(self.preset[131].encode('utf-8').decode("utf-8"))
			if unicode(el3.text) == self.preset[131]:
				break
		self.element(self.driver,self.using[132], self.ele[132]).click() #点击解绑手机
		el4 = self.element(self.driver,self.using[133], self.ele[133])  # 个人中心
		print unicode('测试结果: %s' % el4.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[126].encode('utf-8'))
		self.dy(self.driver, unicode(el4.text), self.exp[126], self.case_id[126])
	def test_5018(self):
		u'''绑定手机'''
		self.element(self.driver,self.using[134],self.ele[134]).click()  #登录
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver, self.using[137],self.ele[137]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[138],self.ele[138]).click()  #绑定手机
		for i in range(10):
			el = self.element(self.driver,self.using[139],self.ele[139])     #手机号输入框
			el.clear()
			el.send_keys(self.preset[139].encode('utf-8').decode("utf-8"))
			if unicode(el.text) == self.preset[139]:
				break
		self.element(self.driver,self.using[140], self.ele[140]).click() #提交
		for i in range(10):
			el2 = self.element(self.driver,self.using[141],self.ele[141])     #验证码输入框
			el2.clear()
			el2.send_keys(self.preset[141].encode('utf-8').decode("utf-8"))
			if unicode(el2.text) == self.preset[141]:
				break
		self.element(self.driver,self.using[142], self.ele[142]).click() #提交
		el3 = self.element(self.driver,self.using[143],self.ele[143])
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[134].encode('utf-8'))
		self.dy(self.driver, unicode(el3.text), self.exp[134], self.case_id[134])

	def test_5019(self):
		self.element(self.driver,self.using[126], self.ele[126]).click()  # 登录
		sleep(5)
		while (True):
			try:
				for i in range(2):
					self.tap(self.driver, self.suspend)  # 点击悬浮标
				sleep(2)
				self.element(self.driver,self.using[129], self.ele[129]).click()  # 账号安全
				break
			except:
				pass
		self.element(self.driver,self.using[130], self.ele[130]).click()  # 解绑手机
		for i in range(10):
			el3 = self.element(self.driver, self.using[131],self.ele[131])  # 验证码输入框
			el3.clear()
			el3.send_keys(self.preset[131].encode('utf-8').decode("utf-8"))
			if unicode(el3.text) == self.preset[131]:
				break
		self.element(self.driver,self.using[132], self.ele[132]).click()  # 点击解绑手机
		el4 = self.element(self.driver,self.using[132], self.ele[133])  # 个人中心
		print unicode('测试结果: %s' % el4.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[126].encode('utf-8'))