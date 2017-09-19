#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/15
'''

'''
提交虚拟码
撤销订单
提交消费记录
'''

from common import gen_req, gen_sign
import requests


dic = {
	"source":"1",
	"version":"2.0",
	"identity_id":"CMV10999708",
	"data":{
		"virtualCodes":[
			{
				"vcodePass":"CMV10999708_12345678",
				"vcode":"CMV10999708_12345678"
			}
		],
		"itemId":"X17011900041638-01",
		"orderId":"V17091910163830"
	}
}



dic2 = {
	"version":"2.0",
	"identity_id":"CMV10999708",
	"source":"1",
	"data":
	{
		"orderId":"V17091910163830",
		"memo":"不买了",
		"userPhone":"18710070484"
	}
}
dic3 = {
	"source":"2",
	"version":"2.0",
	"identity_id":"CMV10999708",
	"data":
		{
			"recordList":[
				{
				"orderId":"V17091910163830",
				"itemId":"X16091900000000-01",
				"useId":"CMV10999708_12345",
				"virtualCode":"CMV10999708_123456",
				"useAmount":"5.00",
				"useDatetime":"2016-11-08 00:09:45",
				"useContent":"消费内容",
				"phone":"13700000000",
				"virtualCodePass":"CMV10999708_3245234"
				},

				]
		}
}


sign = gen_sign(dic)
req = gen_req(sign, dic)
sign2 = gen_sign(dic2)
req2 = gen_req(sign2, dic2)
sign3 = gen_sign(dic3)
req3 = gen_req(sign3, dic3)


ret = requests.post('http://222.35.5.7/vapi/service/setVirtualCode', data={'req':req})
ret2 = requests.post('http://222.35.5.7/vapi/service/cancelOrder', data={'req':req2})
ret3 = requests.post('http://222.35.5.7/vapi/service/setRecord', data={'req':req3})
print(ret.content.decode())
print(ret2.content.decode())
print(ret3.content.decode())


