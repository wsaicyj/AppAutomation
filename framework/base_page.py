#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


import time
from selenium.common.exceptions import NoSuchElementException
import os
from framework.logger import Logger



#创建一个logger实例
logger = Logger(logger="BasePage").getLog()


class BasePage(object):
    '''
    定义一个页面基类，让所有页面都继承这个类，封闭一些常用的页面操作方法到这个类
    '''

    def __init__(self, driver):
        self.driver = driver


    def quit_app(self):
        '''
        退出APP
        :return:
        '''
        self.driver.quit()


    def wait(self, seconds):
        '''
        隐式等待
        :param seconds:时间单位为秒
        :return:
        '''
        self.driver.implicitly_wait(seconds)
        logger.info('隐式等待%s秒' % seconds)


    def get_img(self):
        '''
        保存图片
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹\Screenshots下
        :return:
        '''
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.jpg'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('成功保存当前步骤截图至screenhosts目录下')
        except NameError as e:
            logger.error('保存图片失败，错误信息:%s' % e)
            self.get_img()


    def find_element(self, selector):
        '''
        定位元素方法
        根据=>来切割字符串，为了防止切割不准确，影响元素定位
        例:submit_btn = "id=>su"
        login_lnk="xpath=>//*[@id='u1]"
        :param selector:
        :return:element
        '''
        element = ''

        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)

        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == 'i' or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info('成功找到%s元素' % selector_value)
            except NoSuchElementException as e:
                logger.error('找不到元素:%s' % e)
                self.get_img()
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info('成功找到%s元素' % selector_value)
            except NoSuchElementException as e:
                logger.error('找不到元素:%s' % e)
                self.get_img()
        else:
            raise NameError('请输入正确的元素')

        return element



    def type(self, selector, text):
        '''
        输入数据
        :param selector:
        :param text:
        :return:
        '''
        el = self.find_element(selector)
        # print(type(el))
        # el.clear()
        try:
            el.send_keys(text)
            logger.info('成功输入数据:%s' % text)
        except NameError as e:
            logger.error('输入数据失败:%s' % e)
            self.get_img()


    def click(self, selector):
        '''
        点击元素
        :param selector:
        :return:
        '''
        el = self.find_element(selector)
        try:
            el.click()
            logger.info('点击按钮成功')
        except NameError as e:
            logger.error('点击按钮失败:%s' % e)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info('等待%d秒' % seconds)


    def clear(self, selector):
        '''
        清除文本框
        :param selector:
        :return:
        '''

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info('输入数据前清除掉输入框里的原有数据')
        except NameError as e:
            logger.error('清除输入框数据失败:%s' % e)
            self.get_img()


