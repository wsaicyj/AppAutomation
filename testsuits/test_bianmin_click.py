#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

import unittest
from framework.app_engine import APPEngine
from pageobjects.app_home_page import HomePage


class BianminClick(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        app = APPEngine(cls)
        cls.driver = app.open_app(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_bianmin_click(self):
        homepage = HomePage(self.driver)
        homepage.bianmin_click()
        homepage.sleep(3)
        homepage.get_img()