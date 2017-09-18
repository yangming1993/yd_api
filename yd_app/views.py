# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from yd_app.models import Order
import json
from common import *
# Create your views here.
def index(request):

	return HttpResponse('a')

@csrf_exempt
def notifyOrder(request):
	dic = req_to_dir(request.META['QUERY_STRING'])['data']
	print(dic)
	if Order.objects.filter(orderId=dic['orderId']):
		return HttpResponse(json.dumps({"code": "1009", "msg": "重复订单"},ensure_ascii=False))
	Order.objects.create(orderId=dic['orderId'],
						 phone=dic['phone'],
						 itemId=dic['itemId'],
						 title=dic['title'],
						 price=dic['price'],
						 quantity=dic['quantity'],
						 finalFee=dic['finalFee'],
						 )
	return HttpResponse(json.dumps({"code": "0", "msg": "下单成功"},ensure_ascii=False))

@csrf_exempt
def resendVirtualCode(request):
	dic = req_to_dir(request.META['QUERY_STRING'])['data']
	if Order.objects.filter(orderId=dic['orderId']):
		#向用户发送对应的虚拟码
		return HttpResponse(json.dumps({"code": "0", "msg": "重发成功"},ensure_ascii=False))
	return HttpResponse(json.dumps({"code": "1009", "msg": "未找到订单"}, ensure_ascii=False))

@csrf_exempt
def setCodeInvalid(request):
	dic = req_to_dir(request.META['QUERY_STRING'])['data']
	if Order.objects.filter(orderId=dic['orderId']):
		#在数据库中设计isInvalid, 设置isInvalid为True
		return HttpResponse(json.dumps({"code": "0", "msg": "设置失效成功"},ensure_ascii=False))
	return HttpResponse(json.dumps({"code": "1009", "msg": "失败原因"}, ensure_ascii=False))

