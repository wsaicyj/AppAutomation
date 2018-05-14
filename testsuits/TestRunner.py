#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'



import unittest, time
import os
import HTMLTestRunner
import testsuits
from testsuits.test_bianmin_click import BianminClick
from testsuits.test_health_click import HealthClick
from testsuits.test_my_click import MyClick


#设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/testreport/'
#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

#设置报告名称格式
htmlFile = report_path + now + 'HTMLtemplate.html'


suite = unittest.TestSuite()
# suite.addTest(BianminClick('test_bianmin_click'))
# suite.addTest(HealthClick('test_health_click'))
# suite.addTest(MyClick('test_my_click'))
test_dir = os.path.abspath('.')
# suite = unittest.TestLoader.discover(start_dir=test_dir, pattern="test_*.py", top_level_dir=None)
suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern="test_*.py", top_level_dir=None)

# print(test_dir)



if __name__ == '__main__':

    #执行用例
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    with open(htmlFile, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='健康深圳APP测试报告', description=u'测试结果:')
        runner.run(suite)