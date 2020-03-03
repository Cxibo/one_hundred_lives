#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 20:59
# @Author  : Cxibo
# @File    : test_tkinter.py
# @Software: PyCharm

from tkinter import *
from tkinter import ttk
from PIL import Image
from tkinter import filedialog
from test_requests import bilibili


class Spider(ttk.Frame):
    def __init__(self, master=None):
        self.master = master
        # 标题
        self.master.title('Spider')
        # 根视窗变化时，视窗特定行列的变化相关系数
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        # 视窗参数设置
        super(Spider, self).__init__(master, padding='3 3 12 12')
        # 视窗在根视窗上的布局设置
        self.grid(row=0, column=0, sticky=(W, E))
        # 变量
        self.target_url = StringVar()
        self.prompt = StringVar()
        self.prompt.set('nothing')
        self.save_dir = None
        # 视窗内部控件布局
        self.widgets_arrange()

    def func(self, *args):
        self.save_dir = filedialog.askdirectory()

        if self.save_dir == None:
            return None

        base_url = 'https://www.bilibili.com/video/'
        target_av = self.target_url.get()
        if not target_av.startswith('av'):
            target_av = 'av' + target_av

        # # 简单测试下url，之后考虑吧
        # if not re.match(r'^\d+$', self.target_url.get()):
        #     return None

        bilibili(save_place=self.save_dir).run(base_url + target_av)
        self.prompt.set('访问' + base_url + target_av + '下载完成')

    def widgets_arrange(self):
        ttk.Label(self, text='输入b站av号：').grid(row=0, column=0)
        target_entry = ttk.Entry(self, textvariable=self.target_url)
        target_entry.grid(row=1, column=0)
        ttk.Button(self, text='Get', command=self.func).grid(row=3, column=0)
        ttk.Label(self, textvariable=self.prompt).grid(row=4, column=0)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        target_entry.focus()
        self.master.bind('<Return>', self.func)

    def run(self):
        self.master.mainloop()



class feettometersample(ttk.Frame):
    def __init__(self, master=None):
        self.master = master
        # 标题
        self.master.title('Feet to Meter')
        # 根视窗变化时，视窗特定行列的变化相关系数
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        # 视窗参数设置
        super(feettometersample, self).__init__(master, padding='3 3 12 12')
        # 视窗在根视窗上的布局设置
        self.grid(row=0, column=0, sticky=(W, E))
        # 变量
        self.feet = StringVar()
        self.meters = StringVar()
        # 视窗内部控件布局
        self.widgets_arrange()

    def widgets_arrange(self):
        # 设计图展示
        # Image.open('D:\\resource\\images\\test\\python_gui_feettometer.png').show()

        feet_entry = ttk.Entry(self, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(self, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(self, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(self, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(self, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(self, text="meters").grid(column=3, row=2, sticky=W)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        self.master.bind('<Return>', self.calculate)

    def run(self):
        self.master.mainloop()

    def calculate(self, *args):
        # 通过键盘绑定的响应函数启动，会自动接收一个event参数，eg:(<KeyPress event state=Mod1|0x40000 keysym=Return keycode=13 char='\r' x=211 y=168>,)
        # 响应函数执行中主线程是阻塞的，并且在响应函数执行完毕之后才会重画
        try:
            value = float(self.feet.get())
            self.meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except ValueError:
            pass


def test():
    root = Tk()
    Spider(root).run()
    # feettometersample(root).run()


if __name__ == "__main__":
    test()
