#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 20:13
# @Author  : Cxibo
# @File    : test_struct.py
# @Software: PyCharm

# 参考网址
# https://www.cnblogs.com/kuzhon/articles/5627977.html
# update2019年10月29日16:02:17
# 作用:网络数据传输，字节流文件管理

import struct


def test():
    s = struct.pack('B4sII', 0x44, b'aaaa', 0x01, 0x0e)
    print(type(s))
    # <class 'bytes'>
    print(struct.calcsize('B4sII'))
    # 16

    a, b, c, d = struct.unpack('B4sll', s)
    print(a, b, c, d)
    # 68 b'aaaa' 1 14

if __name__ == "__main__":
    test()
