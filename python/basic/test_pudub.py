#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 2:31
# @Author  : Cxibo
# @File    : test_pudub.py
# @Software: PyCharm
import os

from pydub import AudioSegment
def test():

    path = r'F:\少女前线\少女前线资源文件\_vgmt_acb_ext_HK416.acb\acb\awb'

    wav = AudioSegment.from_wav(os.path.join(path, 'HK416_SOULCONTRACT_JP.wav'))
    wav.export(os.path.join(path, 'HK416_SOULCONTRACT_JP2.mp3'), format='mp3')
    pass


if __name__ == "__main__":
    test()