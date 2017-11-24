#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: Dongyouyuan
# @Software: PyCharm
# @File: main.py
# @Time: 17-11-23 上午11:57
from lagou import Lagou
from db import init_db


if __name__ == "__main__":
    # 第一次运行请初始化你的数据库
    init_db()

    cookie = "user_trace_token=20171120113056-ba4eb409-b665-4fc9-8cbf-92ea7e4b1520; LGUID=20171120113057-38d05b37-cda3-11e7-996a-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; X_MIDDLE_TOKEN=8f7c1b487db070b59111650e8396d3d3; X_HTTP_TOKEN=9cfa44c75b49564bf4bb24410edeb4e7; TG-TRACK-CODE=index_hotsearch; JSESSIONID=ABAAABAACDBAAIAFDC183EB010548C17203563788B54991; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511148657,1511172863,1511258038; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511328820; LGSID=20171122133340-b23fe104-cf46-11e7-9986-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FPHP%2F%3FlabelWords%3Dlabel%3FlabelWords%3Dhot; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_PHP%3Fpx%3Ddefault%26city%3D%25E5%25B9%25BF%25E5%25B7%259E; LGRID=20171122133340-b23fe39c-cf46-11e7-9986-5254005c3644; _ga=GA1.2.525386246.1511148657; _gid=GA1.2.2044927823.1511148657; hibext_instdsigdip=1; SEARCH_ID=107bd6aa53a042e5955ff22f624fe3c5"
    city = "杭州"
    lang = "python"
    lagou = Lagou(cookie=cookie, city=city, lang=lang)
    lagou.get_data(page_sum=20)
    print(lagou.list_dict_results)
    # lagou.insert_to_db()
