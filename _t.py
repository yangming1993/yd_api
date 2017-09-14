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
import chardet
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
json_sort_dir = '"""""""""""""""""""""""""""""""""""""""""""""",,,,,,,,,,-...0000000000000000000000000011111111111112222333344555666677788::::::::::::CFIIMVVX_aaaacccdddddddeeeeeeeeeefhiiiiiiiiiillmnnnnnnoooooppqrrrrrssstttttttttuuuvyy{{}}测试'
sign = common.gen_sign(dir)
t1 = common.gen_req(sign,dir)
print t1

t = '汉'
print t.encode('gbk'),chardet.detect(t)