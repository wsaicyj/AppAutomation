#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

from framework.base_page import BasePage
from appium.webdriver.common.touch_action import TouchAction
from framework.logger import Logger

logger = Logger(logger='YuYuePage').getLog()
class YuYuePage(BasePage):

    yuyue_btn = "id=>com.xky.app.patient:id/mTv_appointment_registration"    #就医-预约挂号按钮
    area_btn = "xpath=>//android.widget.TextView[@text='%s']"     #市区
    hos_btn = "xpath=>//android.widget.TextView[@text='%s']"      #医院
    depcls_btn = "xpath=>//android.widget.TextView[@text='%s']"      #科室类别
    dep_btn = "xpath=>//android.widget.TextView[@text='%s']"      #科室
    doc_btn = "xpath=>//android.widget.TextView[@text='%s']"      #医生
    sch_btn = "xpath=>//android.widget.TextView[@text='预约']"     #排班
    sou_btn = "xpath=>//android.widget.TextView[@text='%s']"     #号源
    sub_btn = "id=>com.xky.app.patient:id/mBtn_order_confirm"    #确认按钮
    sub2_btn = "id=>com.xky.app.patient:id/mTv_positive_text"    #确认下单
    res_btn = "id=>com.xky.app.patient:id/tv_appoint_result_confirm_btn"  #查看订单



    def __init__(self, driver):
        self.driver = driver


    def yuyue_click(self):
        '''
        点击预约挂号模块
        :return:
        '''
        self.sleep(3)
        self.click(self.yuyue_btn)


    def select_area(self, area):
        '''
        选择市区
        :return:
        '''
        self.sleep(3)
        self.click(self.area_btn % area)
        logger.info('选择%s' % area)


    def select_hospital(self, hos):
        '''
        选择医院
        :return:
        '''
        self.sleep(3)
        self.click(self.hos_btn % hos)
        logger.info('选择医院:%s' % hos)

    def select_depcls(self, depcls):
        '''
        选择科室类别
        :param dep:
        :return:
        '''
        self.sleep(3)
        self.click(self.depcls_btn)
        logger.info('选择科室:%s' % depcls)

    def select_deptment(self, dep):
        '''
        选择科室
        :param dep:
        :return:
        '''
        self.sleep(3)
        self.click(self.dep_btn)
        logger.info('选择科室:%s' % dep)

    def select_doctor(self, doc):
        '''
        选择医生
        :param doc:
        :return:
        '''
        self.sleep(3)
        self.click(self.doc_btn)
        logger.info('选择医生:%s' % doc)

    def select_schedule(self):
        '''
        选择排班
        :return:
        '''
        self.sleep(3)
        self.click(self.sch_btn)
        logger.info('选择排班')

    def select_source(self, sou):
        '''
        选择号源
        :return:
        '''
        self.sleep(3)
        self.click(self.sou_btn % sou)
        logger.info("选择号源时间段:%s" % sou)


    def submit_btn(self):
        '''
        点击确认按钮,提交预约信息
        :return:
        '''
        self.sleep(3)
        self.click(self.sub_btn)
        self.sleep(3)
        self.click(self.sub2_btn)
        logger.info('提交预约信息')


    def result_btn(self):
        '''
        查看订单
        :return:
        '''
        self.sleep(3)
        self.click(self.res_btn)
        logger.info('查看订单')




    def scroll_up(self,hos1, hos2):
        '''
        向上拖动
        :return:
        '''
        el1 = self.find_element(self.hos_btn % hos1)
        el2 = self.find_element(self.hos_btn % hos2)
        actions = TouchAction(self.driver)
        actions.press(el=el1).move_to(el=el2).release().perform()
        logger.info('向上拖动')






