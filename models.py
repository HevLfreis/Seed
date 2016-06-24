#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2016/5/17 
# Time: 13:34
#
from config import db


class Log(db.Model):

    __tablename__ = 'log'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)


class MarkDown(db.Model):

    __tablename__ = 'md'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    cat = db.Column(db.String(200))
    tag = db.Column(db.String(20), nullable=True)
    content = db.Column(db.String(20000), nullable=True)
    click = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime)


class ACG(db.Model):

    __tablename__ = 'acg'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    tag = db.Column(db.Integer)
    content = db.Column(db.String(1000))
    time = db.Column(db.DateTime)


