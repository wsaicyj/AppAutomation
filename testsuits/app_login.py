#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


import unittest
from framework.app_engine import APPEngine
from pageobjects.app_login_page import LoginPage
from pageobjects.app_home_page import HomePage

class APPLogin(unittest.TestCase):


    # def setUp(self):
    #     '''
    #     测试固件setUp的代码，主要是测试的前提准备工作
    #     :return:
    #     '''
    #     app = APPEngine(self)
    #     self.driver = app.open_app(self)
    #
    # def tearDown(self):
    #     '''
    #     测试结束后的操作,这里基本是关闭操作
    #     :return:
    #     '''
    #     self.driver.quit()
    @classmethod
    def setUpClass(cls):
        '''
        测试固件setUp的代码，主要是测试的前提准备工作
        :return:
        '''
        app = APPEngine(cls)
        cls.driver = app.open_app(cls)

    @classmethod
    def tearDownClass(cls):
        '''
        测试结束后的操作,这里基本是关闭操作
        :return:
        '''
        cls.driver.quit()



    def test_login(self):

        phone = '17010000001'
        pwd = 'cyj123456'

        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        #点击首页界面【我的】模块
        homepage.my_click()
        # #点击未登录按钮
        loginpage.no_login_click()
        # #输入手机号
        loginpage.type_phone(phone)
        # #输入密码
        loginpage.type_pwd(pwd)
        # #点击确认按钮
        loginpage.submit_btn_click()
        # #等待3秒
        loginpage.sleep(3)
        #保存登录成功图片
        loginpage.get_img()
        '''
        driver = self.driver
        # 登录APP
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.TextView[@text='我的']").click()
        # driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.TextView').click()
        time.sleep(3)
        driver.find_element_by_id('com.xky.app.patient:id/tv_personal_userName').click()
        time.sleep(3)
        driver.find_element_by_id('com.xky.app.patient:id/edtTxt_login_userPhoneNumber').send_keys(
            '17010000001')  # 输入手机号
        time.sleep(3)
        driver.find_element_by_id('com.xky.app.patient:id/edtTxt_login_userPassword').send_keys('cyj123456')  # 输入密码
        time.sleep(3)
        driver.find_element_by_id('com.xky.app.patient:id/btn_login').click()  # 点击确认按钮
        time.sleep(3)
        driver.get_screenshot_as_file()
        '''

    # def test_health(self):
    #     homepage = HomePage(self.driver)
    #     homepage.health_click()
    #     homepage.sleep(3)
    #     # 保存登录成功图片
    #     homepage.get_img()
    #
    # def test_bianmin(self):
    #     homepage = HomePage(self.driver)
    #     homepage.bianmin_click()
    #     homepage.sleep(3)
    #     # 保存登录成功图片
    #     homepage.get_img()
    #
    # def test_yiuyi(self):
    #     homepage = HomePage(self.driver)
    #     homepage.yiuyi_click()
    #     homepage.sleep(3)
    #     # 保存登录成功图片
    #     homepage.get_img()




if __name__ == '__main__':
    unittest.main()

