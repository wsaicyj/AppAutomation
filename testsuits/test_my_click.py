#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

import unittest
from framework.app_engine import APPEngine
from pageobjects.app_home_page import HomePage


class MyClick(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app = APPEngine(cls)
        cls.driver = app.open_app(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_my_click(self):
        str = u'点击【我的】模块'
        homepage = HomePage(self.driver)
        homepage.my_click()
        homepage.sleep(3)
        # homepage.get_img(str)
        homepage.get_img()