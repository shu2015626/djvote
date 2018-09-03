# -*- coding: utf-8 -*-
'''
请写模块说明
'''
__author__ = "sunsn"
__date__ = '2018/9/3 22:15'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
