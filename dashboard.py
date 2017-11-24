#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: Dongyouyuan
# @Software: PyCharm
# @File: dashboard.py
# @Time: 17-11-22 下午9:45

from Lagou.db import Session
from Lagou.models import Recruit


class Dashboard(object):
    def __init__(self):
        self.session = Session()

    def build_word_cloud_job_labels(self):

        list_recruit_job_labels = self.session.query(Recruit.job_labels).filter(Recruit.job_labels != '').all()
        list_job_labels = [obj.job_labels for obj in list_recruit_job_labels]

        list_job_labels.reverse()
        str_job_labels = ','.join(list_job_labels)
        print(str_job_labels.replace(',', ' '))

    def build_word_cloud_company_labels(self):

        list_recruit_company_labels = self.session.query(Recruit.company_labels).filter(Recruit.company_labels != '').all()
        list_company_labels = [obj.company_labels for obj in list_recruit_company_labels]

        list_company_labels.reverse()
        str_company_labels = ','.join(list_company_labels)
        print(str_company_labels.replace(',', ' '))

    def count_industry_field(self):
        list_industry_field = ["健康医疗", "生活服务", "旅游", "金融", "信息安全", "广告营销", "数据服务", "智能硬件", "文化娱乐",
                          "网络招聘", "分类信息", "电子商务", "移动互联网", "企业服务", "社交网络", "教育培训", "O2O", "游戏",
                          "互联网", "媒体", "IT软件", "通信", "公关会展", "房地产/建筑", "汽车", "供应链/物流", "咨询/翻译/法律",
                          "采购/贸易", "非互联网行业"]
        list_recruit_industry_field = self.session.query(Recruit.industry_field).\
            filter(Recruit.industry_field != '').\
            filter(Recruit.city == '深圳').\
            all()
        list_db_recruit_industry_field = [obj.industry_field for obj in list_recruit_industry_field]

        count_industry_field = {}

        for industry in list_industry_field:
            for recruit_industry_field in list_db_recruit_industry_field:
                if industry in recruit_industry_field:
                    if industry in count_industry_field:
                        count_industry_field[industry] += 1
                    else:
                        count_industry_field[industry] = 1
        print(count_industry_field)
