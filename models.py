#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: Dongyouyuan
# @Software: PyCharm
# @File: Tables.py
# @Time: 17-11-22 下午8:22

from sqlalchemy import Column, Integer, CHAR
from db import Base


class Recruit(Base):
    __tablename__ = 'recruit'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, doc="id")
    site = Column('site', CHAR(32), default='lagou', info="站点")

    job_id = Column('job_id', CHAR(32), primary_key=True, index=True, info="工作id")
    job_name = Column('job_name', CHAR(64), default='', index=True, info="工作名称")
    salary = Column('salary', CHAR(32), default='', info="薪酬")
    education = Column('education', CHAR(20), default='', index=True, info="学历")
    work_year = Column('work_year', CHAR(20), default='', index=True, info="工作经验")
    job_city = Column('job_city', CHAR(20), default='', index=True, info="工作城市")
    job_nature = Column('job_nature', CHAR(20), default='', index=True, info="全职|兼职")
    job_first_type = Column('job_first_type', CHAR(20), default='', index=True, info="工作一级类型")
    job_second_type = Column('job_second_type', CHAR(20), default='', index=True, info="工作二级类型")
    job_type = Column('job_type', CHAR(32), primary_key=True, index=True, info="工作类型(关键字)")
    city = Column('city', CHAR(32), default='', index=True, info="城市")
    district = Column('district', CHAR(32), default='', index=True, info="城市区域")
    business_zones = Column('business_zones', CHAR(64), default='', index=True, info="商业区(上班地点坐标)")
    company_labels = Column('company_labels', CHAR(64), default='', index=True, info="职位诱惑")
    job_labels = Column('job_labels', CHAR(64), default='', index=True, info="职位诱惑")
    company_id = Column('company_id', CHAR(64), default='', index=True, info="公司ID")
    finance_stage = Column('finance_stage', CHAR(64), default='', info="公司阶段(A轮，B轮)")
    company_size = Column('company_size', CHAR(64), default='', info="公司规模")
    industry_field = Column('industry_field', CHAR(64), default='', index=True, info="公司行业")
    company_short_name = Column('company_short_name', CHAR(128), default='', info="公司简称")
    company_full_name = Column('company_full_name', CHAR(128), default='', info="公司全称")
    detail_url = Column('detail_url', CHAR(128), default='', info="招聘详情要求网页")
    approve = Column('approve', Integer, default=0, info="公司是否认证")

    create_time = Column('create_time', Integer, default=0, info="创建时间")

    def __repr__(self):
        return "<CallRecord(sid='%s', from='%s', to='%s', duration='%s')>" % \
               (self.sid, self.from_number, self.to_number, self.duration)