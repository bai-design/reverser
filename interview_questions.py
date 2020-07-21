# print(sum(range(1,101)))
# def fn_global():
#     global a
#     print("value is {}".format(a))
#     b = 4
#     a = 4
#     return a+b
# a = 3
# print(fn_global())
# import os
# import math
# import re
# import sys
# import datetime
#
# dict_a = {"a":1, "b":2}
# dict_b = {"m":1, "n":2}
# dict_a.update(dict_b)
# del dict_b["m"]
# print(dict_a)
# print(dict_b)
# list_a = ["a","b","c","c","d","a"]
# print(list(set(list_a)))
# print(list(dict.fromkeys(list_a).keys()))
# print([i for i in list(map(lambda x:x*x ,[1,2,3,4,5])) if i > 10])
# import random
# import numpy
# print(random.random())
# print(numpy.random.rand())
# print(numpy.random.randn())
#
# print(random.randint(1,11))
# print(numpy.random.randint(1,11,size=5))
# print(numpy.random.choice(a=["m","n","x"], size=2, replace=False, p=(0.5, 0.2, 0.3)))
# import re
# china_re = re.compile(r'<div class=".*">(.*?)</div>')
# print(china_re.findall('<div class="nam">中国</div>'))
# select distinct name from student
# ll touch mkdir rm vi more less git cp mv
# print(''.join(sorted(list(set("ajldjlajfdljfddd")))))
# cf_math = lambda x,y : x*y
# print(cf_math(5,6))
# message = {"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
# print({i:message[i] for i in sorted(message.keys())})
# from collections import Counter
# count_char = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
# print(Counter(count_char))
# import re
# chinese_re = re.compile(r'[\u4E00-\u9FA5]+')
# print(chinese_re.findall("not 404 found 张三 99 深圳"))
# def fn_odd(n):
#     return n % 2 == 1
# print([ i for i in filter(fn_odd, list(range(1,11)))])
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([i for i in a if i%2==1])
# print([i for i in list(map(lambda x:x,a)) if i %2 ==1])
# list_old = [1,5,7,9]
# list_old.extend([2,2,6,8])
# list_old.sort(reverse=False)
# print(list_old)
# import os
# os.remove()
# import shutil
# shutil.rmtree()
# rm -rf
# import datetime
# print(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"))
# print(datetime.datetime.now().isoweekday())
# from matplotlib import pyplot
# import pygal
# x_lable = [1,2,3,4,5]
# y_lable = [i^3-i^2+2*i for i in x_lable]
# pyplot.xlabel("x_value", fontsize=5)
# pyplot.ylabel("y_value", fontsize=5)
# pyplot.tick_params(axis="both", labelsize=6, labelcolor="red")
# pyplot.plot(x_lable, y_lable, linewidth=3,color="green")
# pyplot.show()
# list_l = [[1,2],[3,4],[5,6]]
# print([j for i in list_l for j in i])
# x="abc"
# y="def"
# z=["d","e","f"]
# print(x.join(z))
# print(x.join(y))
# j_a = 3
# j_b = 2
#
# j_a, j_b = j_b, j_a
# print(j_a)
# print(j_b)
# zip_str = "abcd"
# zip_list = ["m","n","o"]
# print(list(zip(zip_str,zip_list)))
# import re
# gold_re = re.compile(r'\d+')
# print(gold_re.sub('100', '张明 98分'))
# bt_a = b"hello"
# bt_b = "你好".encode()
# print(bt_a)
# print(bt_b)
# import re
# url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
# date_re = re.compile(r'dateRange=(.*?)%7C(.*?)&date')
# print(date_re.search(url).group(1))
# order_list = [2,3,5,4,9,6]
# for i in range(len(order_list)-1):
#     for j in range(len(order_list)-1-i):
#         if order_list[j] > order_list[j+1]:
#             order_list[j], order_list[j+1] = order_list[j+1], order_list[j]
# print(order_list)
# class Singlist(object):
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
# sin_a = Singlist()
# sin_b = Singlist()
# print(id(sin_a))
# print(id(sin_b))
# def dict_fn(key, value, dic={}):
#     dic[key]=value
#     print(dic)
#
# dict_fn(key="m", value="1")
# dict_fn(key="n", value="2")
# dict_fn(key="o", value="3",dic={})
# dic={"name":"zs","age":18}
# del dic["name"]
# dic_new = dic.pop("age")
# print(dic)
# print(dic_new)
# import copy
# list_ex = ["1","2",["m","n"]]
# list_copy = copy.copy(list_ex)
# list_deecopy = copy.deepcopy(list_ex)
# list_ex[2][1]="o"
# print(list_ex)
# print(list_copy)
# print(list_deecopy)
# import sys
# print(sys.argv)
# print((i for i in range(3)))
# a = "  hehheh  "
# print(a.strip())
# rt_list=[0,-1,3,-10,5,9]
# print(sorted(rt_list, reverse=False))
# rt_list.sort(reverse=False)
# print(rt_list)
# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# print(sorted(foo,key=lambda x:x, reverse=False))
# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# print(sorted(foo,key=lambda x:(x<0, abs(x)), reverse=False))
# import re
# s = "info:xiaoZhang 33 shandong"
# s_re = re.compile(r'\w+')
# print(s_re.findall(s))
# def di_sum(n):
#     if n == 0:
#         return 0
#     else:
#         sum = n + di_sum(n-1)
#         return sum
# import re
# a = "  hehheh  "
# a_re = re.compile(r'\s+')
# print(a_re.sub('',a))
# import re
# a = "  hehheh  "
# a_re = re.compile(r'\w+')
# print(a_re.search(a).group())
# count_a = "hehheh"
# print(count_a.count("h"))
# import json
# dict_x = {"name": "Lucy", "sex": "female"}
# dict_json = json.dumps(dict_x)
# json_dict = json.loads(dict_json)
# print(type(json_dict))
# print(type(dict_json))
# ult = "hehheh"
# print(ult.title())
# print(ult.upper())
# print(ult.lower())
# print(u'\u4E00')
# print(u'\u9FA5')
import time
s = "简述乐观锁和悲观锁"
for i in range(10):
    print('\r', s[:9-i]+'|', end='')
    time.sleep(0.5)
