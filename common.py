#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/14
'''

import json
import base64
import hashlib
import uuid

#测试的
secretKey = 'kjkhZ4TAxYFWXBMMhFevWFRc3uB5XXCvu4LfwTGc52iRx9Ta1eQCspPfb9Jzr2QVShjcXaLdcCOzEbUnx9zuPTWMdcWAdC1YhpNBtz51gs1n9i7rTxuVkgzUk59zK208'
#示例的
# secretKey = 'RMSMs44C4YRA25w27nRjN399VTUVVBY2eGy6E2v'
identity_id = 'CMV10999723'


def gen_sign(dic):
	"""
	生成签名
	:param dir: 传入所有信息字典
	:return: 签名
	"""
	json_dir = json.dumps(dic, ensure_ascii=False)
	json_sort_dir = sorted(json_dir)

	json_sort_dir = ''.join(json_sort_dir).strip()
	sign = hashlib.md5(bytes((secretKey + json_sort_dir),encoding='utf-8')).hexdigest().lower()

	return sign

def gen_req(sign, dic):
	'''
	:param sign: 签名
	:param dir: 传入所有信息字典
	:return: 请求req
	'''
	js = json.dumps(dic, ensure_ascii=False)
	st = sign + js
	print(st)
	req = base64.b64encode(st.encode())

	return req

def req_to_dir(req):
	'''
	将从request.META['QUERY_STRING']获取的数据转化为可操作的字典
	:param req: 形如'req=abc'的字符串
	:return: 字典， 签名不正确时返回False
	'''
	st = base64.b64decode(req.partition('=')[2]).decode()
	sign, a, json_dic = st.partition('{')
	json_dic = a + json_dic
	dic = json.loads(json_dic)  #loads后为unicode格式
	cf_sign = gen_sign(dic)
	if sign == cf_sign:
		return dic
	return False

def gen_vcode():
	return '{0}_{1}'.format(identity_id, uuid.uuid1()), '{0}_{1}'.format(identity_id, uuid.uuid4())


