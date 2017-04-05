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
	u'''快速注册'''
	def setUp(self):
		#self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.xuanyi.mbzj.appgame','com.xuanyi.mbzj.SplashActivity'))
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps('com.zhankaigame.destiny.appgame', 'com.zhankaigame.destiny.RenWanTangSplashActivity'))
		#智能等待
		self.driver.implicitly_wait(10)
		self.ele = self.get_col(0,6) #元素列
		self.exp = self.get_col(0,7) #预期结果列
		self.case_id = self.get_col(0,0) #case id 列
		self.preset = self.get_col(0,2) #预置条件列
		self.using = self.get_col(0, 5)  # 查找元素方式列
		#self.by_id(self.driver,'com.zhankaigame.destiny.appgame:id/button_1').click()

	def tearDown(self):
		self.driver.quit()

	def test_0001(self):
		u'''快速注册，输入空密码'''
		self.element(self.driver,self.using[1],self.ele[1]).click() #快速注册
		self.element(self.driver,self.using[3],self.ele[3]).click() #注册
		el3 = self.element(self.driver,self.using[4],self.ele[4]) #提示语
		print unicode('测试结果: %s' % el3.text)
		print unicode('预期结果: %s' % self.exp[1])
		self.dy(self.driver,unicode(el3.text),self.exp[1],self.case_id[1]) #断言+截图
	def test_0002(self):
		u'''快速注册，输入5个数字密码'''
		self.element(self.driver,self.using[5],self.ele[5]).click() #快速注册
		for i in range(10):
			el2 = self.element(self.driver,self.using[6],self.ele[6]) #输入框
			el2.clear()
			el2.send_keys(str(int(self.preset[6])))   #输入整形字符串 12345
			if unicode(el2.text) == str(int(self.preset[6])):
				break
		self.element(self.driver,self.using[7],self.ele[7]).click() #注册
		el4 =self.element(self.driver,self.using[8],self.ele[8]) #提示语
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[5])
		self.dy(self.driver, unicode(el4.text), self.exp[5], self.case_id[5])  # 断言+截图
	def test_0003(self):
		u'''快速注册，输入6个英文密码'''
		self.element(self.driver,self.using[9],self.ele[9]).click() #快速注册
		for i in range(10):
			el2 =self.element(self.driver,self.using[10],self.ele[10])  #输入框
			el2.clear()
			el2.send_keys(self.preset[10].decode("utf-8")) #输入6个英文密码
			if unicode(el2.text) == self.preset[10]:
				break
		self.element(self.driver,self.using[11],self.ele[11]).click() #注册
		el4 = self.element(self.driver,self.using[12],self.ele[12])  #进入游戏按钮
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[9])
		self.dy(self.driver,unicode(el4.text),self.exp[9],self.case_id[9]) # 断言+截图
	def test_0004(self):
		u'''快速注册，输入7个英数密码'''
		self.element(self.driver,self.using[13],self.ele[13]).click() #快速注册
		for i in range(10):
			el2 = self.element(self.driver,self.using[14],self.ele[14]) #输入框
			el2.clear()
			el2.send_keys(self.preset[14].decode("utf-8")) #输入7个（英数密码
			if unicode(el2.text) == self.preset[14]:
				break
		self.element(self.driver,self.using[15],self.ele[15]).click() #注册
		el4 = self.element(self.driver,self.using[16],self.ele[16]) #进入游戏按钮
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[13])
		self.dy(self.driver,unicode(el4.text),self.exp[13],self.case_id[13]) # 断言+截图
	def test_0005(self):
		u'''快速注册，输入特殊符号和中文'''
		self.element(self.driver,self.using[17],self.ele[17]).click() #快速注册
		el2 = self.element(self.driver,self.using[18],self.ele[18]) #输入框
		el2.clear()
		el2.send_keys(self.preset[18].encode('utf-8').decode("utf-8")) #输入特殊符号和中文
		el3 =self.element(self.driver,self.using[19],self.ele[19])  #输入框为空
		print unicode('测试结果: %s' % el3.text)
		print unicode('预期结果: %s' % self.exp[17])
		self.dy(self.driver,unicode(el3.text),self.exp[17],self.case_id[17])
	def test_0006(self):
		u'''快速注册，密码输入完成 ，点击右上角返回按钮'''
		self.element(self.driver,self.using[20],self.ele[20]).click() #快速注册
		for i in range(10):
			el2 = self.element(self.driver,self.using[21],self.ele[21]) #输入框
			el2.clear()
			el2.send_keys(self.preset[21].decode("utf-8")) #输入qwerty
			if unicode(el2.text) == self.preset[21]:
				break
		self.element(self.driver,self.using[22],self.ele[22]).click() #返回按钮
		el4 = self.element(self.driver,self.using[23],self.ele[23])  #登录界面 快速注册按钮
		print unicode('测试结果: %s' % el4.text)
		print unicode('预期结果: %s' % self.exp[20])
		self.dy(self.driver,unicode(el4.text),self.exp[20],self.case_id[20])
	def test_0007(self):
		u'''注册成功后，点击进入游戏'''
		self.element(self.driver,self.using[24],self.ele[24]).click() #快速注册
		for i in range(10):
			el2 =self.element(self.driver,self.using[25],self.ele[25]) #输入框
			el2.clear()
			el2.send_keys(self.preset[25].decode("utf-8")) #输入qwerty
			if unicode(el2.text) == self.preset[25]:
				break
		self.element(self.driver,self.using[26],self.ele[26]).click() #注册
		self.element(self.driver,self.using[27],self.ele[27]).click() #进入游戏按钮

		LOGIN_BUTTON = self.element_or_none(self.driver,self.using[28], self.ele[28])
		print unicode('测试结果: %s' % LOGIN_BUTTON)
		print unicode('预期结果: 元素不为空')
		self.dy_IsNone(self.driver,LOGIN_BUTTON,self.case_id[24])
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(AndroidSDK)
	unittest.TextTestRunner(verbosity=2).run(suite)
	'''now_time = strftime("%Y-%m-%d %H_%M_%S")
	filename = 'D:/test_result/'+now_time+"-result.html"
	fp = open(filename, 'wb')
	case_shuo_ming = u'测试情况'
	HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=case_shuo_ming).run(suite)
	fp.close()'''