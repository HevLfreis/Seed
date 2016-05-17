#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2016/5/17 
# Time: 13:34
#
from sqlalchemy import Column, String, DateTime
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Memo(Base):
    __tablename__ = 'memo'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    tag = Column(String(20), nullable=True)
    content = Column(String(20000), nullable=True)
    timestamp = Column(DateTime)


class ACG(Base):
    __tablename__ = 'acg'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    tag = Column(Integer)
    content = Column(String(1000))
    time = Column(DateTime)


