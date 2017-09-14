#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/14
'''

import json
import base64
import hashlib


secretKey = 'RMSMs44C4YRA25w27nRjN399VTUVVBY2eGy6E2v'
identify_id = 'CMV14223786'


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

	return sign.encode('utf8')

def gen_req(sign, dir):
	'''
	:param sign: 签名
	:param dir: 传入所有信息字典
	:return: 请求req
	'''
	js = json.dumps(dir, ensure_ascii=False, sort_keys=True)
	print js
	st = sign + js
	print st
	req = base64.b64encode(st)

	return req