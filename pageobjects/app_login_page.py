#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

from framework.base_page import BasePage


class LoginPage(BasePage):
    '''
    首页界面、登录界面
    '''

    no_login = "id=>com.xky.app.patient:id/tv_personal_userName" #未登录按钮
    phone = "id=>com.xky.app.patient:id/edtTxt_login_userPhoneNumber"  #手机号输入框
    pwd = "id=>com.xky.app.patient:id/edtTxt_login_userPassword" #密码输入框
    submit_btn = "id=>com.xky.app.patient:id/btn_login" #确认按钮



    def no_login_click(self):
        '''
        点击未登录按钮
        :return:
        '''
        self.sleep(3)
        self.click(self.no_login)


    def type_phone(self, text):
        '''
        输入手机号
        :return:
        '''
        self.sleep(3)
        self.type(self.phone, text)


    def type_pwd(self, text):
        '''
        输入密码
        :param text:
        :return:
        '''
        self.sleep(3)
        self.type(self.pwd, text)


    def submit_btn_click(self):
        '''
        点击确认按钮
        :return:
        '''
        self.click(self.submit_btn)





