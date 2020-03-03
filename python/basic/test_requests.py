#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/2 23:19
# @Author  : Cxibo
# @File    : test_requests.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import os
import time
import re
import json
from requests import RequestException
from urllib.request import quote, unquote
from lxml import etree

"""request用来做小型爬虫会很方便，但是做复杂的爬虫需要造很多轮子，现在水平不够，复杂爬虫先依靠scrapy吧。
姑且用request做测试，用scrapy做开发，虽然scrapy也不熟悉"""

# headers必要
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


class learn():
    def test_quote(self):
        from urllib.request import quote, unquote

        # 编码

        url1 = "https://www.baidu.com/s?wd=中国"

        # utf8编码，指定安全字符
        ret1 = quote(url1, safe=";/?:@&=+$,", encoding="utf-8")
        print(ret1)
        # https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD

        # gbk编码
        ret2 = quote(url1, encoding="gbk")
        print(ret2)
        # https%3A//www.baidu.com/s%3Fwd%3D%D6%D0%B9%FA

        # 解码
        url3 = "https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD"

        ret3 = unquote(url3, encoding='utf-8')
        print(ret3)
        # https://www.baidu.com/s?wd=中国


class bilibili():
    def __init__(self, save_place='D:\\resource\\bilibili_video'):
        self.getHtmlHeaders = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q = 0.9'
        }

        self.downloadVideoHeaders = {
            'Origin': 'https://www.bilibili.com',
            'Referer': 'https://www.bilibili.com/video/av26522634',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
        self.save_place = save_place

    def get_html(self, url):
        try:
            response = requests.get(url=url, headers=self.getHtmlHeaders)
            if response.status_code == 200:
                return response.text
        except RequestException:
            print('请求Html错误:')

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        video_title = soup.find('h1', class_='video-title')['title']

        pattern = r'<script>window.__playinfo__=(.*?)</script>'
        result = re.search(pattern, html).group(1)

        # print(json.loads(result).get('data').get('dash').get('video')[0].get('baseUrl'))
        # video_url = json.loads(result).get('data').get('dash').get('video')[0].get('baseUrl')
        video_url = json.loads(result).get('data').get('durl')[0].get('url')
        return {

            'title': video_title,
            'url': video_url
        }

    def download_video(self, video):
        title = re.sub(r'[\/:*?"<>|]', '-', video['title'])  # 去掉创建文件时的非法字符
        url = video['url']
        filename = title + '.flv'
        with open(os.path.join(self.save_place, filename), "wb") as f:
            f.write(requests.get(url=url, headers=self.downloadVideoHeaders, stream=True, verify=False).content)

        # 这部分暂时不懂
        # closing适用于提供了 close() 实现的对象，比如网络连接、数据库连接
        # with closing(requests.get(video['url'], headers=self.downloadVideoHeaders, stream=True, verify=False)) as res:
        #     if res.status_code == 200:
        #         with open(filename, "wb") as f:
        #             for chunk in res.iter_content(chunk_size=1024):
        #                 if chunk:
        #                     f.write(chunk)

    def run(self, url):
        self.download_video(self.parse_html(self.get_html(url)))


def www_pltuku_com(url='http://www.pltuku.com/piaol/liangtku/20200617/85778.html'):
    """已经拉过：
    'http://www.pltuku.com/piaol/liangtku/20200617/85778.html'
    'http://www.pltuku.com/piaol/liangtku/20200623/85963.html'
    """
    # 本地存放姑且在这里
    images_store_path = 'D:\\resource\\images'

    r = requests.get(url, headers=headers)

    # 设置编码 r.text会自己猜，但是有的时候不灵
    r.encoding = 'gb2312'

    soup = BeautifulSoup(r.text, 'html.parser')
    # 观察，分析地址组合规则
    # print(soup.prettify())

    # 测试，继续观察
    # print(soup.find(class_='page').a)
    # print(soup.find(class_='pagelist'))

    # 提取需要的信息
    image_num = len(soup.find(class_='pagelist').find_all('a'))
    title = soup.find(class_='page').a['title']
    # src = soup.find(class_='page').a.img['src']

    if not os.path.exists(os.path.join(images_store_path, title)):
        os.mkdir(os.path.join(images_store_path, title))

    for i in range(1, image_num + 1):
        # 观察路径规则用提取的信息进行组合
        ith_image_page = url.replace('.html', '_{}.html'.format(i)) if i > 1 else url
        r = requests.get(ith_image_page)
        soup = BeautifulSoup(r.text, 'html.parser')
        src = soup.find(class_='page').a.img['src']
        # r.content是 bytes
        image_bytes = requests.get(src).content
        with open(os.path.join(images_store_path, title, '{}.jpg'.format(i)), 'wb') as fd:
            fd.write(image_bytes)
        # 停顿，不要给服务器过大的负担
        time.sleep(1)


class baidu_baike_com():
    def __init__(self):
        # self.base_url = 'http://baike.baidu.com/item/'
        # self.theme = '数据库'
        # self.url = self.base_url + self.theme
        # r = requests.get(quote(self.url, safe=";/?:@&=+$,", encoding="utf-8"), headers=headers)
        # self.url = 'https://baike.baidu.com/item/%E6%B1%89%E6%9C%9D/454839?fromtitle=%E4%B8%A4%E6%B1%89&fromid=10734204'
        self.url = 'https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E5%BA%93'
        r = requests.get(self.url, headers=headers)
        r.encoding = 'utf-8'

        # BeautifulSoup处理
        soup = BeautifulSoup(r.text, 'html.parser')
        # print(soup.prettify())
        title = soup.head.title.string
        content = soup.head.find('meta', attrs={'name': 'description'})['content']
        keywords = soup.head.find('meta', attrs={'name': 'keywords'})['content']

        from scrapy.linkextractors import LinkExtractor
        from scrapy.http import HtmlResponse

        links = LinkExtractor(allow='/item/.*', deny='#ref_.*',
                              restrict_xpaths='/html/body/div[@class="body-wrapper"]').extract_links(
            HtmlResponse(url=self.url, body=r.content, encoding='utf-8'))
        print([link.url for link in links])

        pass


def bilibili_game_comment(game_base_id):
    """b站游戏评论爬虫，可以获取玩家评论，评分，回复等信息
    101171 时之歌"""
    # 'http://line1-h5-pc-api.biligame.com/game/comment/page?game_base_id=101171&rank_type=3&page_num=2&page_size=10&_=1550165882894'
    base_url = 'http://line1-h5-pc-api.biligame.com/game/comment/page?game_base_id={}&rank_type=3&page_num={}&page_size=10&_=1550165882894'

    grade_list = []
    for page_num in range(1, 10):
        url = base_url.format(game_base_id, page_num)
        r = requests.get(url, headers=headers)
        comment_list_info = json.loads(r.text)
        comment_list = comment_list_info.get('data').get('list')
        for comment in comment_list:
            grade_list.append(int(comment.get('grade')))
    print(grade_list)
    print(sum(grade_list) / len(grade_list))


def test():
    # baidu_baike_com()
    # bilibili_game_comment(101171)
    # bilibili().run('https://www.bilibili.com/video/av44335526')
    bilibili().run('https://www.bilibili.com/video/av28730015')

if __name__ == "__main__":
    test()
