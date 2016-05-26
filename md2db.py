#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2016/5/18 
# Time: 18:55
#
import sys
sys.path.insert(0, '/usr/lib/python2.7/dist-packages')
sys.path.insert(0, '/usr/local/lib/python2.7/dist-packages')

import codecs
import os
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, MarkDown
import misaka as m


mysql_link = 'mysql://root:12345678@127.0.0.1/seed?charset=utf8'
mysql_engine = create_engine(mysql_link, echo=False)
Base.metadata.create_all(mysql_engine)
Session = sessionmaker(bind=mysql_engine)
session = Session()

mddir = os.getcwd()+'/static/files/md'
files = os.listdir(mddir)

for md in files:
    print md
    if md.endswith('md'):

        with codecs.open(mddir+'/'+md, 'r', encoding='utf8') as f:
            text = f.read()

        blog = MarkDown(title=md.rstrip('.md').split('_')[0],
                        cat=md.rstrip('.md').split('_')[1],
                        content=text,
                        timestamp=datetime.datetime.today())
        session.add(blog)

        # print text
        #
        # html = m.html(text, extensions=('fenced-code',))
        #
        # print html

session.commit()
