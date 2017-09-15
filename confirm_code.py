#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/15
'''
from common import gen_req, gen_sign
import requests
import copy
dit = {
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

sign = gen_sign(dit)

req = gen_req(sign, dit)
print req
ret = requests.post('http://222.35.5.7/vapi/service/setVirtualCode', data={'req':req})
print ret.content
dic