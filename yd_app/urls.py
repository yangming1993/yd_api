#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/15
'''

from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^notifyOrder$', views.notifyOrder),
]