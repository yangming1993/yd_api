#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:ym

@time:2017/9/14
'''

import base64
import json
import common
import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')

# s = 'e3aac7a0cff7028865e9d3fb06d75bdd{"source":"1","version":"2.0","identity_id":"CMV12345678","data":{"discount":"","finalFee":"135.0","itemId":"X16000000000000-01","orderId":"V16110114687522","phone":"13700000000","price":"130.0","quantity":"1","title":"测试"}}'
# b64 = base64.b64encode(s)
# strs = base64.b64decode(b64)
# print strs
#
# s2 = '{"source":"1","version":"2.0","idently_id":" CMV14223786","data":{}}'
# s2_sorted = sorted(s2)
# print ''.join(s2_sorted)
#
# d =  {"a":"2"}
# print type(json.dumps(d))
dir = {
"source":"1",
"version":"2.0",
"identity_id":"CMV12345678",
"data":
{
"discount":"",
"finalFee":"135.0",
"itemId":"X16000000000000-01",
"orderId":"V16110114687522",
"phone":"13700000000",
"price":"130.0",
"quantity":"1",
"title":"测试"
}
}

# context = {"source":"1",
# "version":"2.0",
# "identity_id":"CMV10999725","data":{"code": "0", "msg": "下单成功"}}
# json_sort_dir = '"""""""""""""""""""""""""""""""""""""""""""""",,,,,,,,,,-...0000000000000000000000000011111111111112222333344555666677788::::::::::::CFIIMVVX_aaaacccdddddddeeeeeeeeeefhiiiiiiiiiillmnnnnnnoooooppqrrrrrssstttttttttuuuvyy{{}}测试'
sign = common.gen_sign(dir)
print(sign)
# t1 = common.gen_req(sign,dir)
# print t1


# request = [15/Sep/2017 18:42:10] "POST /yd_app/notifyOrder?req=ZjRmZTlhMTVhNzExN2VjM2Y5YzkyMDkyNzM1OGNhNDB7InNvdXJjZSI6IjEiLCJ2ZXJzaW9uIjoiMi4wIiwiaWRlbnRpdHlfaWQiOiJDTVYxMDk5OTcyMyIsImRhdGEiOnsidGl0bGUiOiLmtYvor5XllYblk4EiLCJwaG9uZSI6IjE4NzEwMDcwNDg0IiwicHJpY2UiOiIxMC4wIiwiY2hhbm5lbFN1Yk9yZGVySWQiOiIyMDE3MDkxNTE4NDUyNjEyMDQzMSIsImNoYW5uZWxPcmRlcklkIjoiMjAxNzA5MTUxODQ1MjYxMjA0NzUiLCJmaW5hbEZlZSI6IjkuOCIsInF1YW50aXR5IjoiMSIsIml0ZW1JZCI6IlgxNzAxMTkwMDA0MTYzOC0wMSIsIm9yZGVySWQiOiJWMTcwOTE1MTg0NTI2NTQiLCJkaXNjb3VudCI6IiJ9fQ== HTTP/1.1" 200 36
# req = 'ZjRmZTlhMTVhNzExN2VjM2Y5YzkyMDkyNzM1OGNhNDB7InNvdXJjZSI6IjEiLCJ2ZXJzaW9uIjoiMi4wIiwiaWRlbnRpdHlfaWQiOiJDTVYxMDk5OTcyMyIsImRhdGEiOnsidGl0bGUiOiLmtYvor5XllYblk4EiLCJwaG9uZSI6IjE4NzEwMDcwNDg0IiwicHJpY2UiOiIxMC4wIiwiY2hhbm5lbFN1Yk9yZGVySWQiOiIyMDE3MDkxNTE4NDUyNjEyMDQzMSIsImNoYW5uZWxPcmRlcklkIjoiMjAxNzA5MTUxODQ1MjYxMjA0NzUiLCJmaW5hbEZlZSI6IjkuOCIsInF1YW50aXR5IjoiMSIsIml0ZW1JZCI6IlgxNzAxMTkwMDA0MTYzOC0wMSIsIm9yZGVySWQiOiJWMTcwOTE1MTg0NTI2NTQiLCJkaXNjb3VudCI6IiJ9fQ=='
# req_b = 'f4fe9a15a7117ec3f9c920927358ca40{"source":"1","version":"2.0","identity_id":"CMV10999723","data":{"title":"测试商品","phone":"18710070484","price":"10.0","channelSubOrderId":"20170915184526120431","channelOrderId":"20170915184526120475","finalFee":"9.8","quantity":"1","itemId":"X17011900041638-01","orderId":"V17091518452654","discount":""}}'
# req_dic1 = {"source":"1","version":"2.0","identity_id":"CMV10999725",
# 		   "data":{"title":"测试商品","phone":"18710070484","price":"10.0",
# 				   "channelSubOrderId":"20170915162841536932",
# 				   "channelOrderId":"20170915162841536340","finalFee":"9.8",
# 				   "quantity":"1",
# 				   "itemId":"X17011900041638-01",
# 				   "orderId":"V17091516284189","discount":""}}
# req_dic2 = {"source":"1","version":"2.0","identity_id":"CMV10999723",
# 			"data":{"title":"测试商品","phone":"18710070484","price":"10.0",
# 					"channelSubOrderId":"20170915184526120431",
# 					"channelOrderId":"20170915184526120475","finalFee":"9.8",
# 					"quantity":"1",
# 					"itemId":"X17011900041638-01","orderId":"V17091518452654","discount":""}}'
# print common.req_to_dir(req)


i = common.req_to_dir('req=MDkxNDkxZDQzNjZiMDRlNjBmMWQwMDU1ZDAyMDBkOTZ7InNvdXJjZSI6IjEiLCJ2ZXJzaW9uIjoiMi4wIiwiaWRlbnRpdHlfaWQiOiJDTVYxMDk5OTcyMyIsImRhdGEiOnsib3JkZXJJZCI6IlYxNzA5MTUxODQ1MjY1NCJ9fQ==')
print(repr(i))

print(common.gen_vcode())