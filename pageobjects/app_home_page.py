#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

from framework.base_page import BasePage
from framework.logger import Logger

logger = Logger(logger='HomePage').getLog()

class HomePage(BasePage):
    '''
    首页界面
    '''

    my = "xpath=>//android.widget.TextView[@text='我的']"  # 我的模块
    health = "xpath=>//android.widget.TextView[@text='健康']"  # 健康模块
    bianmin = "xpath=>//android.widget.TextView[@text='便民']"  # 便民模块
    yiuyi = "xpath=>//android.widget.TextView[@text='就医']"  # 就医模块
    coo_yiuyi = [(116, 1655), (188, 1727)]   #就医模块--坐标
    coo_my = [(891, 1655), (963, 1727)]

    def my_click(self):
        '''
        点击首页界面【我的】模块
        :return:
        '''
        logger.info('===点击首页界面【我的】模块===')
        self.sleep(3)
        self.click(self.my)

    def my_tap(self):
        '''
        通过坐标点击首页界面【我的】模块
        :return:
        '''
        logger.info('===点击【我的】模块-坐标===')
        self.sleep(3)
        self.tap(self.coo_my)

    def yiuyi_click(self):
        '''
        点击首页界面【就医】模块
        :return:
        '''
        logger.info('===点击首页界面【就医】模块===')
        self.sleep(3)
        self.click(self.yiuyi)

    def yiuyi_tap(self):
        '''
        点击【就医】模块-坐标
        :return:
        '''
        logger.info('===点击【就医】模块-坐标===')
        self.sleep(3)
        self.tap(self.coo_yiuyi)

    def health_click(self):
        '''
        点击首页界面【健康】模块
        :return:
        '''
        logger.info('===点击首页界面【健康】模块===')
        self.sleep(3)
        self.click(self.health)

    def bianmin_click(self):
        '''
        点击首页界面【便民】模块
        :return:
        '''
        logger.info('===点击首页界面【便民】模块===')
        self.sleep(3)
        self.click(self.bianmin)

