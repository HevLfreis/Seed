#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2016/5/18 
# Time: 18:55
#
import sys
from config import db

sys.path.insert(0, '/usr/lib/python2.7/dist-packages')
sys.path.insert(0, '/usr/local/lib/python2.7/dist-packages')

import codecs
import os
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import MarkDown
import misaka as m


db.create_all()

mddir = os.getcwd()+'/static/files/md'
files = os.listdir(mddir)

for md in files:
    print md
    if md.endswith('memo.md'):

        with codecs.open(mddir+'/'+md, 'r', encoding='utf8') as f:
            text = f.read()

        blog = MarkDown(title=md.rstrip('.md').split('_')[0],
                        cat=md.rstrip('.md').split('_')[1],
                        content=text,
                        timestamp=datetime.datetime.today())
        db.session.add(blog)

        # print text
        #
        # html = m.html(text, extensions=('fenced-code',))
        #
        # print html

db.session.commit()
