#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'



from pageobjects.app_login_page import LoginPage
from pageobjects.app_home_page import HomePage


class APPLogin():

    def login(self, driver):
        phone = '17000000001'
        pwd = 'cyj123456'
        homepage = HomePage(driver)
        homepage.my_click()
        loginpage = LoginPage(driver)
        loginpage.login_app(phone, pwd)
        # LoginPage(self.driver).login_app(phone, pwd)
        loginpage.sleep(3)
        # userName = loginpage.get_user_name()

