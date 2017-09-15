# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from common import *
# Create your views here.
def index(request):
	post = request.POST
	print post
	print 'from index'
	return render()

@csrf_exempt
def notifyOrder(request):
	print 'from notifyOrder'
	post = request.POST
	path = request.path
	print request.method
	print request.body
	print request.META
	print 'from notifyOrder'
	context = {"source": "1",
			   "version": "2.0",
			   "identity_id": "CMV10999725", "data": {"code": "0", "msg": "下单成功"}}
	# sign = gen_sign(context)
	req = 'ODE0ZmMxNjM2NTE5MmY1ZGQ0MDI5YzRjMGRkNjc1ZGV7ImRhdGEiOiB7ImNvZGUiOiAiMCIsICJtc2ciOiAi5LiL5Y2V5oiQ5YqfIn0sICJpZGVudGl0eV9pZCI6ICJDTVYxMDk5OTcyNSIsICJzb3VyY2UiOiAiMSIsICJ2ZXJzaW9uIjogIjIuMCJ9'
	return HttpResponse(json.dumps({"code": "0", "msg": "下单成功"},ensure_ascii=False))