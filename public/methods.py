#!/usr/bin/env python
#coding=utf-8

from time import sleep, strftime
import os
class Methods(object):
	def public(self,driver):
		self.driver = driver
		sleep(2)
		window = self.driver.get_window_size()
		width = int(window[u'width'])
		height = int(window[u'height'])
		zuobiao = [width,height]
		return  zuobiao
	def left_swipe(self,driver):
		self.driver = driver
		a = self.public(self.driver)
		self.driver.swipe(a[0]*5 / 6, a[1]/2, a[0] *1 / 6, a[1]/2 , 1000)
		sleep(2)
	def right_swipe(self,driver):
		self.driver = driver
		a = self.public(self.driver)
		self.driver.swipe(a[0] * 1 / 6, a[1] / 2, a[0] * 5 / 6, a[1] / 2, 1000)
		sleep(2)
	def up_swipe(self,driver):
		self.driver = driver
		a = self.public(self.driver)
		self.driver.swipe(a[0] /2, a[1] * 5/6, a[0] /2, a[1] * 1/6, 1000)
	def down_swipe(self,driver):
		self.driver = driver
		a = self.public(self.driver)
		self.driver.swipe(a[0] / 2, a[1] * 1 / 6, a[0] / 2, a[1] * 5 / 6, 1000)
		sleep(2)
	def screencap(self,driver,**kwargs):
		dict1 = kwargs
		self.name = dict1['name']
		day = strftime('%Y-%m-%d')
		path = 'result/' + day + '/screencap/'
		self.driver.get_screenshot_as_file(os.getcwd()+os.sep+path + self.name + '.png')
		if os.getcwd()+os.sep =='/Users/zhaozhiquan/automation/AndroidSdk/TestCase/':
			self.driver.save_screenshot(os.getcwd() + os.sep +'../'+ path + self.name + '.png')
		else:
			self.driver.save_screenshot(os.getcwd()+os.sep+path + self.name + '.png')
		sleep(2)
	def desired_caps(self,Package_name,Activity_name):
		desired_caps = {}
		#desired_caps['udid'] = 'CKL6T16B29025193'
		desired_caps['platformName'] = 'Android'
		#desired_caps['platformVersion'] = '5.1'
		desired_caps['deviceName'] = 'GT-I9500'
		desired_caps['appPackage'] = Package_name
		desired_caps['appActivity'] = Activity_name
		desired_caps['unicodeKeyboard'] = 'True'
		desired_caps['appWaitActivity'] = 'com.appgame.lib.sdk.login.AppGameLoginActivity'
		return desired_caps

	def dy(self,driver,value1,value2,screen_name):
		self.driver = driver
		try:
			self.assertEqual(value1, value2)
		except:
			self.screencap(self.driver,name=screen_name)
			self.assertEqual(value1, value2)
	def dy_IsNone(self,driver,obj,screen_name):
		self.driver = driver
		try:
			self.assertIsNone(obj)
		except:
			self.screencap(self.driver,name=screen_name)
			self.assertIsNone(obj)
	def dy_IsNotNone(self,driver,obj,screen_name):
		self.driver = driver
		try:
			self.assertIsNotNone(obj)
		except:
			self.screencap(self.driver,name=screen_name)
			self.assertIsNotNone(obj)

	def tap(self,driver,value,dealy=None):
		#value 是一个元组
		self.driver = driver
		zuobiao = self.public(driver)
		value = (int(value[0]*zuobiao[0]),int(value[1]*zuobiao[1]))
		return self.driver.tap([value],dealy)

	def element(self, driver, methods, value):
		'''
		:param driver:驱动
		:param methods: 方式
		:param value: 值
		:return: 返回对象
		'''
		self.driver = driver
		if methods == 'name':
			return self.driver.find_element_by_name(value)
		elif methods == 'xpath':
			return self.driver.find_element_by_xpath(value)
		elif methods == 'id':
			return self.driver.find_element_by_id(value)
		elif methods == 'class':
			return self.driver.find_element_by_class_name(value)

	def elements(self, driver, methods, value):
		'''
		:param driver:驱动
		:param methods: 方式
		:param value: 值
		:return: 返回对象list
		'''
		self.driver = driver
		if methods == 'name':
			return self.driver.find_elements_by_name(value)
		elif methods == 'xpath':
			return self.driver.find_elements_by_xpath(value)
		elif methods == 'id':
			return self.driver.find_elements_by_id(value)
		elif methods == 'class':
			return self.driver.find_elements_by_class_name(value)

	def element_or_none(self, driver, methods, value):
		'''
		:param driver:驱动
		:param methods:方式
		:param value:知
		:return:元素存在返回元素,不存在,返回None
		'''
		self.driver = driver

		try:
			element = self.element(self.driver, methods, value)
		except:
			element = None
		return element
