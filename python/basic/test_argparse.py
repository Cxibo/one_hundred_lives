#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 13:03
# @Author  : Cxibo
# @File    : test_argparse.py
# @Software: PyCharm

# https://www.cnblogs.com/dengtou/p/8413609.html

import argparse


def test(case=0):
    parser = argparse.ArgumentParser()

    if case == 0:
        # 如果只有一个参数且参数不由'-'开始，认为是位置参数
        parser.add_argument('echo')

    elif case == 1:
        # 第一个--后的字符串成为dest，选项参数必须以-开头
        parser.add_argument('-user', '--tasdff', '-a')

    elif case == 2:
        # python test_argparse.py -u
        parser.add_argument('-u', '--user', action='store_true')

    elif case == 3:
        # python test_argparse.py -v 2
        # 必要且必须为int类型，否则报错
        parser.add_argument('--ver', '-v', required=True, type=int)

    elif case == 4:
        # 必要且必须在choices中选
        # dest   - 设置这个选项的value解析出来后放到哪个属性中
        parser.add_argument('-file', choices=['test1', 'test2'], dest='world')

    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    test(4)
