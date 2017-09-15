#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/14
'''

import json
import base64
import hashlib

#测试的
secretKey = 'kjkhZ4TAxYFWXBMMhFevWFRc3uB5XXCvu4LfwTGc52iRx9Ta1eQCspPfb9Jzr2QVShjcXaLdcCOzEbUnx9zuPTWMdcWAdC1YhpNBtz51gs1n9i7rTxuVkgzUk59zK208'
#示例的
# secretKey = 'RMSMs44C4YRA25w27nRjN399VTUVVBY2eGy6E2v'
identify_id = 'CMV10999725'


def gen_sign(dir):
	"""
	生成签名
	:param dir: 传入所有信息字典
	:return: 签名
	"""
	json_dir = json.dumps(dir, ensure_ascii=False)
	json_sort_dir = sorted(json_dir.decode('utf8'))

	json_sort_dir = ''.join(json_sort_dir).encode('utf8').strip()
	sign = hashlib.md5(secretKey + json_sort_dir).hexdigest().lower()

	return sign

def gen_req(sign, dir):
	'''
	:param sign: 签名
	:param dir: 传入所有信息字典
	:return: 请求req
	'''
	js = json.dumps(dir, ensure_ascii=False)
	st = sign + js
	print st
	req = base64.b64encode(st)

	return req

def req_to_dir(req):
	st = base64.b64decode(req)
	print st
	return st

