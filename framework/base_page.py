#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

import time
from selenium.common.exceptions import NoSuchElementException
import os
from framework.logger import Logger
from appium.webdriver.common.touch_action import TouchAction

# 创建一个logger实例
logger = Logger(logger="BasePage").getLog()


class BasePage(object):
    '''
    定义一个页面基类，让所有页面都继承这个类，封闭一些常用的页面操作方法到这个类
    找到了一些关于按键的keycode，如下：
    KEYCODE_CALL 拨号键 5
    KEYCODE_ENDCALL 挂机键 6
    KEYCODE_HOME 按键Home 3
    KEYCODE_MENU 菜单键 82
    KEYCODE_BACK 返回键 4
    KEYCODE_SEARCH 搜索键 84
    KEYCODE_CAMERA 拍照键 27
    KEYCODE_FOCUS 拍照对焦键 80
    KEYCODE_POWER 电源键 26
    KEYCODE_NOTIFICATION 通知键 83
    KEYCODE_MUTE 话筒静音键 91
    KEYCODE_VOLUME_MUTE 扬声器静音键 164
    KEYCODE_VOLUME_UP 音量增加键 24
    KEYCODE_VOLUME_DOWN 音量减小键 25
    Tips：后面的数字为  keycode
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

    def get_img(self, str=u'默认'):
        '''
        保存图片
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹\Screenshots下
        :param str: 步骤名称
        :return:
        '''
        now = time.strftime('%Y%m%d', time.localtime(time.time()))
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/%s/' % now
        if not os.path.exists(file_path):
            logger.info('创建%s文件夹' % file_path)
            os.mkdir(file_path)
        # rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # screen_name = file_path + str + '_' + rq + '.jpg'
        screen_name = file_path + '%s.png' % str
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('成功保存【%s.png】截图至screenhosts/%s目录下' % (str, now))
        except NameError as e:
            logger.error('保存图片失败，错误信息:%s' % e)
            self.get_img(str)

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
        # print(selector_value)

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

    def get_text(self, selector):
        '''
        获取元素文本
        :param selector:
        :return:
        '''
        print(selector)
        el = self.find_element(selector)
        try:
            text = el.text
            logger.info('成功获取元素文本:%s' % el.text)
            return text
        except NameError as e:
            logger.error('获取元素文本失败:%s' % e)

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
            self.get_img()


    def action_tap(self, el, x, y):
        '''
        坐标点击
        :param coo: 坐标
        :param sec: 毫秒
        :return:
        '''
        logger.info('===点击坐标:%s,%s===' % (x, y))
        TouchAction(self.driver).tap(el, x, y).perform()

    def tap(self, coo, sec=100):
        '''
        坐标点击
        :param coo: 坐标
        :param sec: 毫秒
        :return:
        '''
        logger.info('===点击坐标:%s===' % (coo))
        self.sleep(3)
        self.driver.tap(coo, sec)


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

    def move_to(self, selector):
        '''
        移动到某个位置
        :param selector:
        :return:
        '''
        el = self.find_element(selector)

    def key_back(self):
        '''
        返回键
        :return:
        '''
        logger.info('===点击返回键===')
        self.sleep(3)
        self.driver.press_keycode(4)

    def key_home(self):
        '''
        Home键
        :return:
        '''
        logger.info('===点击Home键===')
        self.sleep(3)
        self.driver.press_keycode(3)


    def refresh(self):
        '''
        刷新界面
        :return:
        '''
        logger.info('===刷新界面===')
        self.sleep(3)
        self.driver.refresh()

    def launch(self):
        '''
        启动已安装好的APP
        :return:
        '''
        logger.info('===启动APP===')
        self.sleep(3)
        self.driver.launch_app()
