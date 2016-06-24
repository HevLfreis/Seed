#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2016/5/28 
# Time: 10:13
#
import logging
import logging.config
import yaml
from flask import Flask

app = Flask(__name__, static_folder='static')

logger_config = yaml.load(open(app.root_path+'/logging.conf'))
logger_config['handlers']['file']['filename'] = app.root_path + '/logs/seed.log'
logging.config.dictConfig(logger_config)
logger = logging.getLogger('icomm_logger')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@127.0.0.1/seed?charset=utf8'
# app.config['SQLALCHEMY_POOL_RECYCLE'] = 1800
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)
# db.create_all()
