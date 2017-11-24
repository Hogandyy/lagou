#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: Dongyouyuan
# @Software: PyCharm
# @File: request_lagou.py
# @Time: 17-11-22 下午3:40

import requests
import time
from db import Session
from models import Recruit


class Lagou(object):
    def __init__(self, cookie, lang, city):
        self.cookie = cookie
        self.lang = lang
        self.city = city
        self.url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '25',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'user_trace_token=20171120113056-ba4eb409-b665-4fc9-8cbf-92ea7e4b1520; LGUID=20171120113057-38d05b37-cda3-11e7-996a-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; X_MIDDLE_TOKEN=8f7c1b487db070b59111650e8396d3d3; X_HTTP_TOKEN=9cfa44c75b49564bf4bb24410edeb4e7; TG-TRACK-CODE=index_hotsearch; JSESSIONID=ABAAABAACDBAAIAFDC183EB010548C17203563788B54991; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511148657,1511172863,1511258038; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511328820; LGSID=20171122133340-b23fe104-cf46-11e7-9986-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FPHP%2F%3FlabelWords%3Dlabel%3FlabelWords%3Dhot; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_PHP%3Fpx%3Ddefault%26city%3D%25E5%25B9%25BF%25E5%25B7%259E; LGRID=20171122133340-b23fe39c-cf46-11e7-9986-5254005c3644; _ga=GA1.2.525386246.1511148657; _gid=GA1.2.2044927823.1511148657; hibext_instdsigdip=1; SEARCH_ID=107bd6aa53a042e5955ff22f624fe3c5',
            'Cookie': self.cookie,
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            # 'Referer': "https://www.lagou.com/jobs/list_{}?px=default&city={}".format(self.lang, self.city),
            'Referer': 'https://www.lagou.com/jobs/list_PHP?px=default&city=%E5%B9%BF%E5%B7%9E',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'X-Anit-Forge-Code': '0',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With': 'XMLHttpRequest'
            }

        self.session = Session()
        self.list_dict_results = []

    def http_requests(self, page, retry=3):
        """
        通过request请求结果
        :param page:
        :param retry:
        :return:
        """
        data = {'first': 'true', 'pn': page, 'kd': self.lang, 'city': self.city}
        for i in range(retry):
            try:
                json = requests.post(self.url, data, headers=self.headers).json()
                if json['success']:
                    return json['content']['positionResult']['result']
                else:
                    return list()
            except Exception as error_msg:
                print('Request is Error: {}'.format(error_msg))
                if i == retry-1:
                    return list()

    def get_data(self, page_sum=1):
        """
        获取搜索结果
        :param page_sum:
        :return:
        """
        for page in range(page_sum+1):
            if page == 0:
                continue
            list_result = self.http_requests(page)
            if list_result:
                self.list_dict_results.extend(list_result)
                time.sleep(1)

    def insert_to_db(self):
        """
        插入数据库
        :return:
        """
        for info in self.list_dict_results:
            # 整理数据
            if info['businessZones']:
                info['businessZones'].reverse()
            else:
                info['businessZones'] = ''

            recruit = Recruit()
            recruit.job_type = lang
            recruit.companyId = info['companyId']
            recruit.city = city
            recruit.job_city = info['city']
            recruit.work_year = info['workYear']
            recruit.education = info['education']
            recruit.industry_field = info['industryField']
            recruit.position_id = info['positionId']
            recruit.position_advantage = info['positionAdvantage']
            recruit.create_time = dataTime_to_timeStamp(info['createTime'])
            recruit.salary = info['salary']
            recruit.job_name = info['positionName']
            recruit.company_size = info['companySize']
            recruit.finance_stage = info['financeStage']
            recruit.job_nature = info['jobNature']
            recruit.company_id = info['companyId']
            recruit.company_labels = ','.join(info['companyLabelList'])
            recruit.district = info['district']
            recruit.job_labels = ','.join(info['positionLables'])
            recruit.approve = info['industryLables']
            recruit.business_zones = ','.join(info['businessZones'])
            recruit.job_first_type = info['firstType']
            recruit.job_second_type = info['secondType']
            recruit.company_short_name = info['companyShortName']
            recruit.company_full_name = info['companyFullName']
            recruit.approve = info['approve']
            recruit.job_id = info['positionId']
            recruit.detail_url = "/jobs/{}.html".format(info['positionId'])

            self.session.add(recruit)
        self.session.commit()
        print('共存储 {} 条数据'.format(len(lagou.results)))


def dataTime_to_timeStamp(data_tiem, format='%Y-%m-%d %H:%M:%S'):
    if not data_tiem:
        return 0
    else:
        try:
            time_array = time.strptime(data_tiem, format)
            time_stamp = int(time.mktime(time_array))
            return time_stamp
        except Exception as error_msg:
            print(error_msg)
            return 0


def updata_recruit():
    """
    修复数据库中的结果
    :return:
    """
    session = Session()

    list_recruit = session.query(Recruit).all()
    for rec in list_recruit:
        rec.salary = rec.salary.upper()
    session.commit()





