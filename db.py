#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: Dongyouyuan
# @Software: PyCharm
# @File: db.py
# @Time: 17-11-22 下午8:21


import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


pymysql.install_as_MySQLdb()

DB_MYSQL_URL = "mysql://{}:{}@{}/{}?charset=utf8".format("root", "123456", "192.168.10.252", "analysis")

_engine = create_engine(DB_MYSQL_URL, pool_size=50, pool_recycle=3600, echo=True, connect_args={'charset': 'utf8'},
                        convert_unicode=True)

Session = sessionmaker(bind=_engine)

Base = declarative_base()


def init_db():
    """
        1、在初始化数据库时需要引入这些model
        2、因为存在主外键，要生成无外键的表 Logs，InResultProcessing， InTranshipmentLatestInfo
    :return:
    """
    from Lagou.models import Recruit

    Base.metadata.create_all(_engine)
