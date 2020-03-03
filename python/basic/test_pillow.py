#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 22:34
# @Author  : Cxibo
# @File    : test_pillow.py
# @Software: PyCharm

# 详细参考；https://www.cnblogs.com/chimeiwangliang/p/7130434.html
# 2019年10月29日00:30:18
import os
from PIL import Image

resource_images_path = r"D:\resource\images\samples"
image_name = "abigail.png"
image_path = os.path.join(resource_images_path, image_name)

project_temporary_save_path = "temporary_save"


def get_image(path=image_path):
    return Image.open(path)


def test(case=0):
    img = get_image()
    # 实用，帮助pycharm知道img类型
    assert isinstance(img, Image.Image)

    if case == 0:
        img.show()
        print(img.getbands())
        print(img.mode)
        print(img.size)
        print(img.info)
        print(img.format)
        print(img.palette)

    elif case == 1:
        # resize save
        print(img.size)
        img2 = img.resize((int(0.7 * img.size[0]), int(0.7 * img.size[1])))
        img2.save(os.path.join(project_temporary_save_path, 'temp.png'))
        img2.show()
        print(img2.size)

    elif case == 2:
        # new
        img = Image.new("RGB", (128, 128), "#FF0000")
        img = Image.new("RGB", (128, 128), 'green')
        img.show()

    elif case == 3:
        # blend
        img2 = Image.new('RGB', img.size, "#F0F000")
        # img2.show()

        img3 = Image.blend(img, img2, 0.3)
        img3.show()

    elif case == 4:
        img2 = Image.new('RGB', img.size, "#FFFF00")
        # img2.show()

        r, g, b = img.split()
        print(g.mode)

        img3 = Image.composite(img, img2, b)
        img3.show()

    elif case == 5:
        def fun(c):
            # 改变亮度
            return c * 0.89

        img2 = Image.eval(img, fun)
        img2.show()

    elif case == 6:
        pass

    elif case == 7:
        pass

    elif case == 8:
        r, g, b = img.split()
        img2 = Image.merge("RGB", [r, g, b])
        img2.show()

    # 以下为对象的方法
    elif case == 9:
        img2 = img.convert('L')
        img2.show()

    elif case == 10:
        img2 = img.copy()
        img2.show()

    elif case == 11:
        box = [0, 0, img.size[0] // 2, img.size[1] // 2]
        img2 = img.crop(box)
        img2.show()

    elif case == 12:
        # Note: This method is not implemented for most images. It is
        # currently implemented only for JPEG and PCD images.
        img2 = img.draft("L", (400, 400))
        img2.show()

    elif case == 13:
        from PIL import ImageFilter
        img2 = img.filter(ImageFilter.BLUR)
        img2.show()

    elif case == 14:
        print(img.getpixel((img.size[0] - 1, img.size[1] - 1)))

    elif case == 15:
        hist = img.histogram()
        print(len(hist))

    elif case == 16:
        img_load = img.load()
        print(img_load[20, 20])

    elif case == 17:
        img_crop = img.crop([0, 0, 200, 200])
        img.paste(img_crop, [200, 200, 400, 400])
        img.show()


if __name__ == "__main__":
    test(17)
