#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


import unittest
from framework.app_engine import APPEngine
from pageobjects.app_login_page import LoginPage
from pageobjects.app_home_page import HomePage
from parameterized import parameterized
from framework.logger import Logger
from appium.webdriver.common.touch_action import TouchAction

logger = Logger(logger='APPLogin').getLog()

class APPLogin(unittest.TestCase):



    # def setUp(self):
    #     '''
    #     测试固件setUp的代码，主要是测试的前提准备工作
    #     :return:
    #     '''
    #     app = APPEngine(self)
    #     self.driver = app.open_app(self)
    #
    #
    # def tearDown(self):
    #     '''
    #     测试结束后的操作,这里基本是关闭操作
    #     :return:
    #     '''
    #
    #     self.driver.quit()


    @classmethod
    def setUpClass(cls):
        '''
        测试固件setUp的代码，主要是测试的前提准备工作
        :return:
        '''
        app = APPEngine(cls)
        cls.driver = app.open_app(cls)
        cls.hp = HomePage(cls.driver)
        cls.loginpage = LoginPage(cls.driver)
        # cls.driver = app.open_apps(cls)


    @classmethod
    def tearDownClass(cls):
        '''
        测试结束后的操作,这里基本是关闭操作
        :return:
        '''
        # pass
        cls.driver.quit()

    @parameterized.expand([
        ('17010000001', 'cyj123456'),
        # ('17000000001', 'cyj123456', '福泉洛'),
        # ('17000000005', 'cyj123456', '余妊截'),
    ])
    def test_login(self, phone, pwd, username):
        # HomePage(self.driver).my_click()
        self.hp.my_click()
        # loginpage = LoginPage(self.driver)
        self.loginpage.no_login_click()   #点击【未登录】按钮
        self.loginpage.type_phone(phone)  # 输入手机号
        self.loginpage.type_pwd(pwd)  # 输入密码
        self.loginpage.submit_btn_click()  # 点击登录按钮
        self.loginpage.sleep(3)
        self.hp.yiuyi_tap()   #通过坐标点击就医模块
        self.hp.my_tap()     #通过坐标点击我的模块
        self.loginpage.sleep(5)
        un = self.loginpage.get_user_name()   #获取登录后的用户名
        print('un:', un, type(un))
        print('username:', username, type(username))
        # if self.assertEqual(username, un):
        if username == un:
            logger.info('%s登录成功' % un)
            self.loginpage.get_img(phone)  # 截图
        else:
            logger.info('登录失败')
            self.loginpage.get_img('登录失败')

        self.loginpage.setting_btn_click()
        self.loginpage.exit_btn_click()



    # def test_logout(self):
    #     self.loginpage.setting_btn_click()
    #     self.loginpage.exit_btn_click()

    '''
    def test_get_username(self):
        loginpage = LoginPage(self.driver)
        # loginpage.key_home()
        # loginpage.launch()
        HomePage(self.driver).my_click()  # 点击【我的】模块
        HomePage(self.driver).yiuyi_tap()  # 点击【就医】模块
        # loginpage.sleep(10)
        # un = loginpage.get_user_name()
        # print(un)
        '''



if __name__ == '__main__':
    unittest.main(verbosity=2)
    # unittest.main()

