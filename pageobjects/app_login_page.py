#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

from framework.base_page import BasePage
from framework.logger import Logger

logger = Logger(logger='LoginPage').getLog()

class LoginPage(BasePage):
    '''
    首页界面、登录界面
    '''

    # no_login = "id=>com.xky.app.patient:id/tv_personal_userName" #未登录按钮
    regis_login_btn = "id=>com.xky.app.patient:id/tv_register_or_login" #未登录按钮
    phone_btn = "id=>com.xky.app.patient:id/edtTxt_login_userPhoneNumber"  #手机号输入框
    pwd_btn = "id=>com.xky.app.patient:id/edtTxt_login_userPassword" #密码输入框
    submit_btn = "id=>com.xky.app.patient:id/btn_login" #确认按钮
    un_btn = "id=>com.xky.app.patient:id/tv_personal_userName"   #登录后的用户名
    setting_btn = "id=>com.xky.app.patient:id/mImg_personal_setting"   #设置按钮
    exit_btn = "id=>com.xky.app.patient:id/btn_setting_exitToLand"    #退出登录按钮



    def login_app(self, phone, pwd):
        '''
        登录APP
        :param phone: 手机号
        :param pwd: 密码
        :return:
        '''
        # fun_name = u'登录APP'
        self.no_login_click()
        self.type_phone(phone) #输入手机号
        self.type_pwd(pwd) #输入密码
        self.submit_btn_click() #点击登录按钮
        self.sleep(10)


    def logoun_app(self):
        '''
        退出APP
        :return:
        '''
        self.setting_btn_click()  #点击设置按钮
        self.exit_btn_click()     #点击退出按钮


    def regi_login_click(self):
        '''
        点击注册/登录按钮
        :return:
        '''
        logger.info('===点击【未登录】按钮===')
        self.sleep(3)
        self.click(self.regi_login_btn)


    def type_phone(self, phone):
        '''
        输入手机号
        :return:
        '''
        logger.info('===输入手机号===')
        self.sleep(3)
        self.type(self.phone_btn, phone)


    def type_pwd(self, pwd):
        '''
        输入密码
        :param text:
        :return:
        '''
        logger.info('===输入密码===')
        self.sleep(3)
        self.type(self.pwd_btn, pwd)


    def submit_btn_click(self):
        '''
        点击确认按钮
        :return:
        '''
        logger.info('===点击【确认】按钮===')
        self.sleep(3)
        self.click(self.submit_btn)


    def get_user_name(self):
        '''
        获取登录后的用户名
        :return:
        '''
        logger.info('===获取登录后的用户名===')
        self.sleep(3)
        return self.get_text(self.un_btn)
        # return un


    def setting_btn_click(self):
        '''
        点击设置按钮
        :return:
        '''
        logger.info('===点击【设置】按钮===')
        self.sleep(3)
        self.click(self.setting_btn)

    def exit_btn_click(self):
        '''
        点击退出登录按钮
        :return:
        '''
        logger.info('===点击【退出登录】按钮===')
        self.sleep(3)
        self.click(self.exit_btn)


