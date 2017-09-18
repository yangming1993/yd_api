#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/15
'''
from common import gen_req, gen_sign
import requests

dic = {
	"source":"1",
	"version":"2.0",
	"identity_id":"CMV10999723",
	"data":{
		"virtualCodes":[
			{
				"vcodePass":"CMV10999725_12345678",
				"vcode":"CMV10999725_12345678"
			}
		],
		"itemId":"X17011900041638-01",
		"orderId":"V17091518452654"
	}
}

dic2 = {
	"version":"2.0",
	"identity_id":"CMV12345678",
	"source":"1",
	"data":{
		"virtualCodes":[
			{
				"vcodePass":"CMV12345678_XXXXXXXX",
				"vcode":"CMV12345678_XXXXXXXX"
			}
		],
		"itemId":"X16110300000000-01",
		"orderId":"V16110114687522"
	}
}

dic3 = {
	"version":"2.0",
	"identity_id":"CMV10999723",
	"source":"1",
	"data":
	{
		"orderId":"V17091518452654",
		"memo":"不买了",
		"userPhone":"18710070484"
	}
}


sign = gen_sign(dic3)

req = gen_req(sign, dic3)
print(req)
ret = requests.post('http://222.35.5.7/vapi/service/cancelOrder', data={'req':req})
print(ret.content.decode())
