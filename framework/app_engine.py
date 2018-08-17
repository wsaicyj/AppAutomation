#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

import os
from appium import webdriver
from framework.logger import Logger
from configparser import ConfigParser
# from testsuits.app_login import APPLogin
# import threading
# from multiprocessing import Process

logger = Logger(logger="APPEngine").getLog()

class APPEngine(object):
    '''
    Appium Desired Capabilities配置信息
    '''

    config = ConfigParser()
    file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
    config.read(file_path)

    # dir = os.path.dirname(os.path.abspath('.'))

    def __init__(self, driver):
        self.driver = driver


    def open_app(self, driver):
        '''
        读取配置文件并获取对应字段单个信息
        :param driver:
        :return:
        '''
        # config = ConfigParser()
        # file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        # config.read(file_path)

        deviceName = self.config.get("desiredCap", "deviceName")
        # deviceName = self.config.get("desiredCap", "deviceName")
        logger.info('设备名称:%s' % deviceName)
        platformName = self.config.get("desiredCap", "platformName")
        logger.info('平台系统:%s' % platformName)
        platformVersion = self.config.get("desiredCap", "platformVersion")
        logger.info('系统版本:%s' % platformVersion)
        noReset = self.config.get("desiredCap", "noReset")
        logger.info('是否重新安装APK:%s' % noReset)
        noSign = self.config.get("desiredCap", "noSign")
        logger.info('跳过检查和签名:%s' % noSign)
        appPackage = self.config.get("desiredCap", "appPackage")
        logger.info('APK包名称:%s' % appPackage)
        appActivity = self.config.get("desiredCap", "appActivity")
        logger.info('启动页面:%s' % appActivity)
        url = self.config.get("testServer", "url")
        logger.info('远程地址:%s' % url)

        desired_caps = {}
        desired_caps['deviceName'] = deviceName
        desired_caps['platformName'] = platformName
        desired_caps['platformVersion'] = platformVersion
        desired_caps['noReset'] = noReset
        desired_caps['noSign'] = noSign
        desired_caps["appPackage"] = appPackage
        desired_caps["appActivity"] = appActivity

        driver = webdriver.Remote(url, desired_caps)
        driver.implicitly_wait(3)

        return driver

    def open_apps(self,driver, i):
        '''
        读取配置文件并获取对应字段多个信息
        :param driver:
        :return:
        '''

        deviceName = self.config.get("desiredCaps", "deviceName")
        platformName = self.config.get("desiredCaps", "platformName")
        platformVersion = self.config.get("desiredCaps", "platformVersion")
        noReset = self.config.get("desiredCaps", "noReset")
        appPackage = self.config.get("desiredCaps", "appPackage")
        appActivity = self.config.get("desiredCaps", "appActivity")
        url = self.config.get("testServers", "url")

        deviceNames = deviceName.split(',')
        print(deviceNames[0],deviceNames[1])
        platformVersions = platformVersion.split(',')
        print(platformVersions[0],platformVersions[1])
        urls = url.split(',')
        print(urls[0], urls[1])

        desired_caps = {}
        desired_caps['deviceName'] = deviceNames[i]
        logger.info('设备名称:%s' % deviceNames[i])
        desired_caps['platformName'] = platformName
        logger.info('平台系统:%s' % platformName)
        desired_caps['platformVersion'] = platformVersions[i]
        logger.info('系统版本:%s' % platformVersions[i])
        desired_caps['noReset'] = noReset
        logger.info('是否重新安装APK:%s' % noReset)
        desired_caps["appPackage"] = appPackage
        logger.info('APK包名称:%s' % appPackage)
        desired_caps["appActivity"] = appActivity
        logger.info('启动页面:%s' % appActivity)

        logger.info('远程地址:%s' % urls[i])

        driver = webdriver.Remote(urls[i], desired_caps)
        driver.implicitly_wait(3)
        # func
        # APPLogin().login(driver)
        # lg.login(driver)
        # driver.quit()
        return driver

        '''
        for i in range(len(deviceName)):

            desired_caps = {}
            desired_caps['deviceName'] = deviceNames[i]
            logger.info('设备名称:%s' % deviceNames[i])
            desired_caps['platformName'] = platformName
            logger.info('平台系统:%s' % platformName)
            desired_caps['platformVersion'] = platformVersions[i]
            logger.info('系统版本:%s' % platformVersions[i])
            desired_caps['noReset'] = noReset
            logger.info('是否重新安装APK:%s' % noReset)
            desired_caps["appPackage"] = appPackage
            logger.info('APK包名称:%s' % appPackage)
            desired_caps["appActivity"] = appActivity
            logger.info('启动页面:%s' % appActivity)

            logger.info('远程地址:%s' % urls[i])

            driver = webdriver.Remote(urls[i], desired_caps)
            driver.implicitly_wait(3)
            lg = APPLogin()
            lg.login(driver)
            # threading.Thread(target=lg.login(driver)).start()

            # return driver
            '''



    def quit_app(self):
        logger.info('退出并关闭APP')
        self.driver.quit()



'''
if __name__ == '__main__':
    # app = APPEngine()
    # p1 = Process(target=APPEngine().open_apps, args=(1,))
    # p2 = Process(target=APPEngine().open_apps, args=(0,))
    # p1.start()
    # p2.start()
    # print('多进程')


    # driver = app.open_apps()
    for i in range(2):
        threading.Thread(target=APPEngine().open_apps, args=(i,)).start()
    # th1 = threading.Thread(target=APPEngine().open_apps, args=(0,))
    # th2 = threading.Thread(target=APPEngine().open_apps, args=(1,))
    # th1.start()
    # th2.start()
    print('多线程')
'''