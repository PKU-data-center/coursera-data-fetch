#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import re


# 抓取khan公开课类
class Spider:
    # 页面初始化
    def __init__(self):
        self.siteURL = 'http://open.163.com/khan/'
        self.tool = tool.Tool()

    def get_page(self):
        try:
            url = self.siteURL
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"Fail", e.reason
                return None

    # 获取索引页面所有课程信息
    def get_contents(self):
        page = self.getPage()
        pattern = re.compile(
            '<div class="g-cell1 g-card1">.*?<a href="(.*?)" .*?', re.S)
        items = re.findall(pattern, page)
        if items:
            contents = []
            for item in items:
                contents.append(item)
            return contents
        else:
            return None

    # 获取课程具体详情页面
    def get_detail_page(self, infoURL):
        response = urllib2.urlopen(infoURL)
        return response.read()

    # 获取课程名称
    def get_course_name(self, page):
        pattern = re.compile('<div class="m-cdes">.*?<h2>(.*?)</h2>', re.S)
        result = re.search(pattern, page)
        if result:
            return self.tool.replace(result.group(1))
        else:
            return None

    # 获取课程讲师
    def get_teacher(self, page):
        pattern = re.compile('<div class="m-cteacher">.*? ', re.S)
        result = re.search(pattern, page)
        if result:
            return self.tool.replace(result.group(1))
        else:
            return None

    # 获取课程简介
    def get_brief(self, page):
        pattern = re.compile('<div class="m-cdes">.*?</h2>(.*?)<b>', re.S)
        result = re.search(pattern, page)
        if result:
            return self.tool.replace(result.group(1))
        else:
            return None

    # 获取课程列表
    def get_course_list(self, page):
        pattern = re.compile(
            ' <td class="u-ctitle">.*?(.*?)<a href=.*?>(.*?)</a>', re.S)
        list = re.findall(pattern, page)
        if list:
            contents = []
            for li in list:
                contents.append([li[0], li[1]])
            return contents
        else:
            return None

    # 获取跟帖人数
    def get_tie_show(self, page):
        pattern = re.compile(
            '<div class="tie-titlebar">.*?<a href.*?>(.*?)</a>', re.S)
        result = re.search(pattern, page)
        if result:
            return self.tool.replace(result.group(1))
        else:
            return None

