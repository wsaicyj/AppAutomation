#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


# my = "xpath=>//android.widget.TextView[@text='我的']"
my = "id=>com.xky.app.patient:id/tv_personal_userName"

print(my.split('=>')[0])
print(my.split('=>')[1])