#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/15
'''

from django.conf.urls import url
from yd_app import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^notifyOrder$', views.notifyOrder),
	url(r'^resendVirtualCode$', views.resendVirtualCode),
	url(r'^setCodeInvalid$', views.setCodeInvalid),

]