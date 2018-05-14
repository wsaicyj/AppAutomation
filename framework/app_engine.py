#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

import os
from appium import webdriver
from framework.logger import Logger
from configparser import ConfigParser

logger = Logger(logger="APPEngine").getLog()

class APPEngine(object):
    '''
    Appium Desired Capabilities配置信息
    '''

    # dir = os.path.dirname(os.path.abspath('.'))

    def __init__(self, driver):
        self.driver = driver


    def open_app(self, driver):
        '''
        读取配置文件并获取对应字段信息
        :param driver:
        :return:
        '''
        config = ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        platformName = config.get("desiredCaps", "platformName")
        logger.info('平台系统:%s' % platformName)
        platformVersion = config.get("desiredCaps", "platformVersion")
        logger.info('系统版本:%s' % platformVersion)
        deviceName = config.get("desiredCaps", "deviceName")
        logger.info('设备名称:%s' % deviceName)
        noReset = config.get("desiredCaps", "noReset")
        logger.info('是否重新安装APK:%s' % noReset)
        appPackage = config.get("desiredCaps", "appPackage")
        logger.info('APK包名称:%s' % appPackage)
        appActivity = config.get("desiredCaps", "appActivity")
        logger.info('启动页面:%s' % appActivity)
        url = config.get("testServer", "url")
        logger.info('远程地址:%s' % url)

        desired_caps = {}
        desired_caps['deviceName'] = deviceName
        desired_caps['platformName'] = platformName
        desired_caps['platformVersion'] = platformVersion
        desired_caps['noReset'] = noReset
        desired_caps["appPackage"] = appPackage
        desired_caps["appActivity"] = appActivity

        driver = webdriver.Remote(url, desired_caps)
        driver.implicitly_wait(3)

        return driver


    def quit_app(self):
        logger.info('退出并关闭APP')
        self.driver.quit()



