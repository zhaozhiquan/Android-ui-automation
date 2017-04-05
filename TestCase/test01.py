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
	u'''玩+账号注册'''
	def setUp(self):
		#self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.xuanyi.mbzj.appgame','com.xuanyi.mbzj.SplashActivity'))
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.zhankaigame.destiny.appgame', 'com.zhankaigame.destiny.RenWanTangSplashActivity'))
		#智能等待
		self.driver.implicitly_wait(10)
		self.ele = self.get_col(1,6) #元素列
		self.exp = self.get_col(1,7) #预期结果列
		self.case_id = self.get_col(1,0) #case id 列
		self.preset = self.get_col(1,2) #预置条件列
		self.using = self.get_col(1, 5)  # 查找元素方式列
		#self.by_id(self.driver,'com.zhankaigame.destiny.appgame:id/button_1').click()

	def tearDown(self):
		self.driver.quit()
	def test_1001(self):
		u'''玩+账号注册，输入为空'''

		self.element(self.driver,self.using[1],self.ele[1]).click() #登录界面注册
		self.element(self.driver,self.using[2],self.ele[2]).click() #注册按钮

		el3 = self.element(self.driver,self.using[3],self.ele[3])    #提示语
		print unicode('测试结果: %s' % el3.text)
		print unicode('预期结果: %s' % self.exp[1])
		self.dy(self.driver,unicode(el3.text),self.exp[1],self.case_id[1]) #断言+截图

	def test_1002(self):
		u'''玩+账号，输入3位中文，密码5位数字，确认密码与密码一致'''
		self.element(self.driver,self.using[4],self.ele[4]).click() #登录界面注册
		for i in range(10):
			el2 = self.element(self.driver,self.using[5],self.ele[5])    #账号输入框
			el2.clear()
			el2.send_keys(self.preset[5].encode('utf-8').decode("utf-8"))
			if unicode(el2.text) == self.preset[5]:
				break
		el3 = self.element(self.driver,self.using[6],self.ele[6])  #密码输入框
		el3.clear()
		el3.send_keys(self.preset[6].decode("utf-8"))
		el4 = self.element(self.driver,self.using[7],self.ele[7])  #确认密码输入框
		el4.clear()
		el4.send_keys(self.preset[7].decode("utf-8"))
		self.element(self.driver,self.using[8],self.ele[8]).click()  #注册按钮
		el6 = self.element(self.driver,self.using[9],self.ele[9])  #提示语
		print unicode('测试结果: %s' % el6.text)
		print unicode('预期结果: %s' % self.exp[4])
		self.dy(self.driver,unicode(el6.text),self.exp[4],self.case_id[4]) #断言+截图
	def test_1003(self):
		u'''玩+账号，输入4位数字，密码6位字母，确认密码与密码一致'''
		self.element(self.driver,self.using[10],self.ele[10]).click() #登录界面注册
		for i in range(10):
			el2 = self.element(self.driver,self.using[11],self.ele[11])    #账号输入框
			el2.clear()
			el2.send_keys(self.preset[11].decode("utf-8"))
			if unicode(el2.text) == self.preset[11]:
				break
		el3 = self.element(self.driver,self.using[12],self.ele[12])  #密码输入框
		el3.clear()
		el3.send_keys(self.preset[12].decode("utf-8"))
		el4 = self.element(self.driver,self.using[13],self.ele[13])  #确认密码输入框
		el4.clear()
		el4.send_keys(self.preset[13].decode("utf-8"))
		self.element(self.driver,self.using[14],self.ele[14]).click()  #注册按钮
		el6 = self.element(self.driver,self.using[15],self.ele[15])  #提示语
		print unicode('测试结果: %s' % el6.text)
		print unicode('预期结果: %s' % self.exp[10])
		self.dy(self.driver,unicode(el6.text),self.exp[10],self.case_id[10]) #断言+截图
	def test_1004(self):
		u'''玩+账号，输入9位字母，密码为空，确认密码与密码不一致'''
		self.element(self.driver,self.using[16],self.ele[16]).click() #登录界面注册
		for i in range(10):
			el2 = self.element(self.driver,self.using[17],self.ele[17])    #账号输入框
			el2.clear()
			el2.send_keys(self.preset[17].decode("utf-8"))
			if unicode(el2.text) == self.preset[17]:
				break

		el4 = self.element(self.driver,self.using[19],self.ele[19])  #确认密码输入框
		el4.clear()
		el4.send_keys(self.preset[19].decode("utf-8"))
		self.element(self.driver,self.using[20],self.ele[20]).click()  #注册按钮
		el6 = self.element(self.driver,self.using[21],self.ele[21])  #提示语
		print unicode('测试结果: %s' % el6.text)
		print unicode('预期结果: %s' % self.exp[16])
		self.dy(self.driver,unicode(el6.text),self.exp[16],self.case_id[16]) #断言+截图
	def test_1005(self):
		u'''玩+账号，输入14位（中英数），密码7位（英数），确认密码为空'''
		self.element(self.driver,self.using[22],self.ele[22]).click() #登录界面注册
		for i in range(10):
			el2 = self.element(self.driver,self.using[23],self.ele[23])    #账号输入框
			el2.clear()
			el2.send_keys(self.preset[23].decode("utf-8"))
			if unicode(el2.text) == self.preset[23]:
				break
		el3 = self.element(self.driver,self.using[24],self.ele[24])  #密码输入框
		el3.clear()
		el3.send_keys(self.preset[24].decode("utf-8"))
		el4 = self.element(self.driver,self.using[25],self.ele[25])  #确认密码输入框
		el4.clear()
		el4.send_keys(self.preset[25].decode("utf-8"))
		self.element(self.driver,self.using[26],self.ele[26]).click()  #注册按钮
		el6 = self.element(self.driver,self.using[27],self.ele[27])  #提示语
		print unicode('测试结果: %s' % el6.text)
		print unicode('预期结果: %s' % self.exp[22])
		self.dy(self.driver,unicode(el6.text),self.exp[22],self.case_id[22]) #断言+截图
	def test_1006(self):
		u'''玩+账号，输入15位（中英数符），密码11位（中英数），确认密码与密码一致'''
		self.element(self.driver,self.using[28],self.ele[28]).click() #登录界面注册
		for i in range(10):
			el2 = self.element(self.driver,self.using[29],self.ele[29])    #账号输入框
			el2.clear()
			el2.send_keys(self.preset[29].encode('utf-8').decode("utf-8"))
			if unicode(el2.text) == self.preset[29]:
				break
		el3 = self.element(self.driver,self.using[30],self.ele[30])  #密码输入框
		el3.clear()
		el3.send_keys(self.preset[30].encode('utf-8').decode("utf-8"))
		el4 = self.element(self.driver,self.using[31],self.ele[31])  #确认密码输入框
		el4.clear()
		el4.send_keys(self.preset[31].encode('utf-8').decode("utf-8"))
		el5 = self.element(self.driver,self.using[32],self.ele[32]).click()  #注册按钮
		el6 = self.element(self.driver,self.using[33],self.ele[33])  #提示语
		print unicode('测试结果: %s' % el6.text)
		print unicode('预期结果: %s' % self.exp[28])
		self.dy(self.driver,unicode(el6.text),self.exp[28],self.case_id[28]) #断言+截图
	def test_1007(self):
		u'''玩+账号，输入空格'''
		self.element(self.driver,self.using[34],self.ele[34]).click() #登录界面注册
		for i in range(10):
			el2 = self.element(self.driver,self.using[35],self.ele[35])    #账号输入框
			el2.clear()
			el2.send_keys(self.preset[35].encode('utf-8').decode("utf-8"))
			if unicode(el2.text) == self.preset[35]:
				break
		el3 = self.element(self.driver,self.using[36],self.ele[36])  #密码输入框
		el3.clear()
		el3.send_keys(self.preset[36].encode('utf-8').decode("utf-8"))
		el4 = self.element(self.driver,self.using[37],self.ele[37])  #确认密码输入框
		el4.clear()
		el4.send_keys(self.preset[37].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[38],self.ele[38]).click()  #注册按钮
		el6 = self.element(self.driver,self.using[39],self.ele[39])  #提示语
		print unicode('测试结果: %s' % el6.text)
		print unicode('预期结果: %s' % self.exp[34])
		self.dy(self.driver,unicode(el6.text),self.exp[34],self.case_id[34]) #断言+截图
	def test_1008(self):
		u'''玩+账号，输入16位（中英数），密码21位（英数），确认密码与密码一致'''
		self.element(self.driver,self.using[40],self.ele[40]).click() #登录界面注册
		for i in range(10):
			el2 = self.element(self.driver,self.using[41],self.ele[41])    #账号输入框
			el2.clear()
			el2.send_keys(self.preset[41].encode('utf-8').decode("utf-8"))
			if unicode(el2.text) == self.preset[41]:
				break
		el3 = self.element(self.driver,self.using[42],self.ele[42])  #密码输入框
		el3.clear()
		el3.send_keys(self.preset[42].encode('utf-8').decode("utf-8"))
		el4 = self.element(self.driver,self.using[43],self.ele[43])  #确认密码输入框
		el4.clear()
		el4.send_keys(self.preset[43].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[44],self.ele[44]).click()  #注册按钮
		el6 = self.element(self.driver,self.using[45],self.ele[45])  #提示语
		print unicode('测试结果: %s' % el6.text)
		print unicode('预期结果: %s' % self.exp[40])
		self.dy(self.driver,unicode(el6.text),self.exp[40],self.case_id[40]) #断言+截图
	def test_1009(self):
		u'''注册成功后，点击进入游戏登录'''
		self.element(self.driver,self.using[46],self.ele[46]).click() #登录界面注册
		################
		# 随机账号
		a = xrange(10000000000000)
		b = random.choice(a)
		d = ['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m']
		e = random.choice(d)
		f = random.choice(d)
		c = e+f+str(b)
		####################
		for i in range(10):
			el2 = self.element(self.driver,self.using[47],self.ele[47])    #账号输入框
			el2.clear()
			el2.send_keys(c)
			if unicode(el2.text) == unicode(c):
				break
		el3 = self.element(self.driver,self.using[48],self.ele[48])  #密码输入框
		el3.clear()
		el3.send_keys(self.preset[48].encode('utf-8').decode("utf-8"))
		el4 = self.element(self.driver,self.using[49],self.ele[49])  #确认密码输入框
		el4.clear()
		el4.send_keys(self.preset[49].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[50],self.ele[50]).click()  #注册按钮
		self.element(self.driver,self.using[51],self.ele[51]).click() #进入游戏按钮

		LOGIN_BUTTON = self.element_or_none(self.driver,self.using[52], self.ele[52])
		print unicode('测试结果: %s' % LOGIN_BUTTON)
		print unicode('预期结果: 元素不为空')
		self.dy_IsNone(self.driver,LOGIN_BUTTON,self.case_id[46])
	def test_1010(self):
		u'''玩+账号，输入完成 ，点击右上角返回按钮'''
		self.element(self.driver,self.using[53],self.ele[53]).click() #登录界面注册
		for i in range(10):
			el2 = self.element(self.driver,self.using[54],self.ele[54])    #账号输入框
			el2.clear()
			el2.send_keys(self.preset[54].encode('utf-8').decode("utf-8"))
			if unicode(el2.text) == self.preset[54]:
				break
		el3 = self.element(self.driver,self.using[55],self.ele[55])  #密码输入框
		el3.clear()
		el3.send_keys(self.preset[55].encode('utf-8').decode("utf-8"))
		el4 = self.element(self.driver,self.using[56],self.ele[56])  #确认密码输入框
		el4.clear()
		el4.send_keys(self.preset[56].encode('utf-8').decode("utf-8"))
		self.element(self.driver,self.using[57],self.ele[57]).click()  #返回按钮
		el6 = self.element(self.driver,self.using[58],self.ele[58]) #登录界面 登录按钮
		print unicode('测试结果: %s' % el6.text)
		print unicode('预期结果: %s' % self.exp[53])
		self.dy(self.driver,unicode(el6.text),self.exp[53],self.case_id[53]) #断言+截图
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(AndroidSDK)
	unittest.TextTestRunner(verbosity=2).run(suite)
	'''now_time = strftime("%Y-%m-%d %H_%M_%S")
	filename = 'D:/test_result/'+now_time+"-result.html"
	fp = open(filename, 'wb')
	case_shuo_ming = u'测试情况'
	HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=case_shuo_ming).run(suite)
	fp.close()'''
