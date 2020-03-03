#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 23:07
# @Author  : Cxibo
# @File    : test_os.py
# @Software: PyCharm

# https://www.cnblogs.com/feifeifeisir/p/9519282.html
# update:2019年10月29日16:35:47

import os

def test():
    os.chdir("C:\Program Files (x86)\Google\Chrome\Application")
    os.system("chrome.exe")

    os.makedirs()
    os.mkdir()

    # 只能删除空dir
    os.removedirs()
    os.rmdir()

    os.listdir()

    os.remove()

    os.rename()

    os.stat()

    # os.path
    os.path.abspath()
    os.path.split()
    os.path.dirname()
    os.path.basename()

    os.path.exists()
    os.path.isabs()
    os.path.isfile()
    os.path.isdir()
    os.path.join()
    os.path.getatime()
    os.path.getctime()
    os.path.getsize()

    os.environ.get('path')

    pass


if __name__ == "__main__":
    # test()
    pass