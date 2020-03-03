#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/5 12:29
# @Author  : Cxibo
# @File    : test_pywin32.py
# @Software: PyCharm
import win32api
import win32con
import win32gui
import time


# 绝对坐标 click 左键
def doubleClick(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# 相对坐标 相对左上点坐标 click 可以后台 左键
def hwndClick(hwnd, x, y):
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
    time.sleep(0.005)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))


def main(startminute=0):
    t1, t2, t3, t4 = 30, 30, 150, 180

    # minutes
    harvest_time = get_harvest_time(t1, t2, t3, t4)
    curtime = startminute

    # second
    harvest_delay = 120

    print('Start harvest at: %s' % time.ctime(time.time()))
    print("Harvest period is %d, %d, %d, %d" % (t1, t2, t3, t4))

    for target_time in harvest_time:
        wait_time = (target_time[0] - curtime) * 60
        if wait_time <= 0:
            continue
        curtime = target_time[0]
        print('Next harvest time is at %s' % time.ctime(wait_time + time.time()))
        time.sleep(wait_time - harvest_delay)
        harvest(target_time[1])


def harvest(count):
    playing = True
    # start bluestacks
    if win32gui.FindWindow(None, 'BlueStacks App Player') == 0:
        playing = False
        win32api.ShellExecute(0, 'open', 'F:\BluestacksCN\BluestacksGP.exe', '', '', 1)
        time.sleep(40)

    wm = win32gui.FindWindow(None, 'BlueStacks App Player')

    # 测试关闭
    if playing:
        # 提示
        win32api.ShellExecute(0, 'open', r'D:\resource\bilibili_video\【少女前线手书】这次轮到AR小队来跳舞啦.flv', '', '',
                              0)
        time.sleep(130)

    # start gf
    if not playing:
        hwndClick(wm, 470, 200)
        time.sleep(30)

    # def func(hwnd, arg):
    # print(hex(hwnd))
    # win32gui.EnumChildWindows(wm, func, arg)

    app_host_hwnd = win32gui.FindWindowEx(wm, 0, None, 'HOSTWND')
    sq_hwnd = win32gui.FindWindowEx(app_host_hwnd, 0, None, 'BlueStacks Android PluginAndroid')

    # login gf
    if not playing:
        hwndClick(sq_hwnd, 325, 568)
        time.sleep(30)
        hwndClick(sq_hwnd, 325, 568)
        time.sleep(30)

    # harvest
    for i in range(count):
        hwndClick(sq_hwnd, 380, 390)
        time.sleep(3)
        hwndClick(sq_hwnd, 380, 390)
        time.sleep(3)

    # confirm
    hwndClick(sq_hwnd, 16, 360)
    time.sleep(3)

    # shut down bluestacks
    # WM_CLOSE 不行
    if not playing:
        win32gui.SendMessage(wm, win32con.WM_DESTROY)


def go_8_1():
    pass


def go_0_2():
    change1_0_2 = [(374, 528), (131, 500), (621, 537), (653, 320), (550, 220), (594, 641), (594, 641), (52, 73),
                   (336, 402), (619, 500), (124, 396), (612, 500), (598, 652), (122, 400), (122, 400), (610, 469),
                   (344, 402), (49, 617), (349, 118), (271, 224), (516, 110), (564, 169), (621, 654)]
    change2_0_2 = [(350, 452), (130, 500), (50, 394), (626, 536), (655, 326), (540, 274), (598, 638), (600, 652),
                   (49, 69), (352, 421), (34, 334), (623, 513), (149, 418), (617, 514), (617, 514), (612, 650),
                   (147, 418), (147, 418), (607, 469), (350, 422), (59, 614), (354, 158), (291, 255), (515, 125),
                   (561, 209), (620, 649)]
    for x, y in change2_0_2:
        click(x, y)
        time.sleep(5)


def get_harvest_time(t1, t2, t3, t4):
    # value that should be greater than the Least Common Multiple of 4t
    gtLCM = 760

    event_list = [0] * gtLCM
    for i in range(t1, gtLCM, t1):
        event_list[i] += 1
    for i in range(t2, gtLCM, t2):
        event_list[i] += 1
    for i in range(t3, gtLCM, t3):
        event_list[i] += 1
    for i in range(t4, gtLCM, t4):
        event_list[i] += 1

    # print([(i, j) for i, j in enumerate(event_list) if j > 0])
    return [(i, v) for i, v in enumerate(event_list) if v > 0]


def test():
    wm = win32gui.FindWindow(None, 'BlueStacks App Player')
    # wm = win32gui.FindWindow(None, 'sq.txt - 记事本')
    # wm = win32gui.FindWindow(None, '今天又有什么骚操作？')
    # wm = win32gui.FindWindow(None, 'test.mp4 - KMPlayer')
    print(wm)

    # cursor position test
    # time.sleep(5)
    # print(win32gui.GetCursorPos())

    # ret (x1, y1, x2, y2) # lefttop (x1, y1) rightbottom (x2, y2)
    # wm_rect = win32gui.GetWindowRect(wm)

    # win32api.SetCursorPos((200, 200))
    hwndClick(wm, 470, 200)

    # app_host_hwnd = win32gui.FindWindowEx(wm, 0, None, 'HOSTWND')
    # sq_hwnd = win32gui.FindWindowEx(app_host_hwnd, 0, None, 'BlueStacks Android PluginAndroid')
    # hwndClick(sq_hwnd, 325, 568)
    # time.sleep(30)
    # hwndClick(sq_hwnd, 325, 568)

    pass


def testMousePos():
    event_list = []
    print('start 5 4 3 2 1 ...')
    time.sleep(5)
    for i in range(27):
        click = win32api.GetCursorPos()
        event_list.append(click)
        print(i, click)
        time.sleep(5)

    print(event_list)
    pass


if __name__ == "__main__":

    # debug = True
    debug = False

    if debug:
        # test()
        # testMousePos()
        harvest(2)
        # print(get_harvest_time(30, 30, 150, 180))
    else:
        main(0)
