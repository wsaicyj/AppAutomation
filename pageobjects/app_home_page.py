#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

from framework.base_page import BasePage


class HomePage(BasePage):
    '''
    首页界面
    '''

    my = "xpath=>//android.widget.TextView[@text='我的']"  # 我的模块
    health = "xpath=>//android.widget.TextView[@text='健康']"  # 健康模块
    bianmin = "xpath=>//android.widget.TextView[@text='便民']"  # 便民模块
    yiuyi = "xpath=>//android.widget.TextView[@text='就医']"  # 便民模块

    def my_click(self):
        '''
        点击首页界面【我的】模块
        :return:
        '''
        self.sleep(3)
        self.click(self.my)

    def yiuyi_click(self):
        '''
        点击首页界面【就医】模块
        :return:
        '''
        self.sleep(3)
        self.click(self.yiuyi)

    def health_click(self):
        '''
        点击首页界面【健康】模块
        :return:
        '''
        self.sleep(3)
        self.click(self.health)

    def bianmin_click(self):
        '''
        点击首页界面【便民】模块
        :return:
        '''
        self.sleep(3)
        self.click(self.bianmin)

