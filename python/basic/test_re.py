#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 16:15
# @Author  : Cxibo
# @File    : test_re.py
# @Software: PyCharm

import re

# https://blog.csdn.net/weixin_40907382/article/details/79654372
# 很详细，以至于进行二次整理很困难，建议参考原博文

def test(case=0):
    text = 'liuyan1'
    if case == 0:
        #
        print(type(re.match('l', text)))
        print(type(re.search('y', text)))
        print(type(re.findall('l', text)))

    elif case == 1:
        # flags
        print(re.search(r'[a-z]+', 'liuyaN1234ab9').group())
        print(re.search(r'[a-z]+', 'liuyaN1234ab9', re.I).group())

    elif case == 2:
        pass


    # elif case == 3:
    # elif case == 4:
    # elif case == 5:
    # elif case == 6:

    pass


if __name__ == "__main__":
    test(1)
