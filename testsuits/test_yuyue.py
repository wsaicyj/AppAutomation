#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

import unittest
from pageobjects.yiuyi.yuyue_page import YuYuePage
from framework.app_engine import APPEngine
from pageobjects.app_home_page import HomePage
from framework.logger import Logger

logger = Logger(logger='YuYue').getLog()

class YuYue(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app = APPEngine(cls)
        cls.driver = app.open_app(cls)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass


    def test_yuyue(self):
        '''
        预约挂号
        :return:
        '''
        area = '福田区'
        up1 = '深圳市妇幼保健院'
        up2 = '香港大学深圳医院'
        hos = '中山大学附属第八医院(福田区人民医院)'
        depcls = '内科'
        dep = '呼吸内科'
        doc = '何海强'
        sou = '08:30-09:00'
        hp = HomePage(self.driver)
        hp.yiuyi_click()  #点击就医模块
        yuyue = YuYuePage(self.driver)
        yuyue.yuyue_click() #点击预约挂号模块
        yuyue.select_area(area) #选择市区
        yuyue.scroll_up(up1, up2)  #向上拖动
        yuyue.select_hospital(hos) #选择医院
        yuyue.select_hospital(depcls) #选择科室类别
        yuyue.select_hospital(dep) #选择科室
        yuyue.select_hospital(doc) #选择医生
        yuyue.select_schedule() #选择排班
        yuyue.select_source(sou)  #选择号源
        yuyue.submit_btn()  #点击确认按钮
        yuyue.result_btn() #查看订单




