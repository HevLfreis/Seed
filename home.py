# coding: utf-8
import codecs

import datetime
import misaka as m
import subprocess
from flask import render_template, send_from_directory, request

from config import app, logger, db


# @app.route('/static/images/md/<path>')
# def send_md_img(path):
#     return send_from_directory(app.static_folder+'/images/md/', path)


@app.route('/')
def seed():
    # try:
    #     log = Log(timestamp=datetime.datetime.today())
    #     db.session.add(log)
    #     db.session.commit()
    #
    #     return render_template('index.html')
    # except Exception, e:
    #     print 'Seed Exception: ', e
    # finally:
    #     print 'Seed'
    logger.info('(' + get_addr(request) + ')')
    db.counter.update_one({'counter': 'home'}, {'$inc': {'value': 1}})
    return render_template('index.html')


@app.route('/memo')
def memo():
    day = datetime.datetime.now()
    mem = datetime.datetime(2017, 3, 12)
    return render_template('memo.html', title='Memo', days=(day-mem).days)


@app.route('/resume')
def resume():
    logger.info('(' + get_addr(request) + ')')
    db.counter.update_one({'counter': 'resume'}, {'$inc': {'value': 1}})
    with codecs.open(app.static_folder + '/files/md/resume.md', 'r', encoding='utf8') as f:
        text = f.read()
    res = m.html(text)
    return render_template('blank.html', html=res, title='Resume')


@app.route('/songci')
def songci():
    logger.info('(' + get_addr(request) + ')')

    sh = ". /home/hevlfreis/torch/install/bin/torch-activate;" \
         "th /home/hevlfreis/torch/torch-rnn/sample.lua " \
         "-checkpoint /home/hevlfreis/model/songci/checkpoint_53000.t7 " \
         "-length " + "300" + " -gpu -1"

    try:
        res = subprocess.check_output(sh, shell=True).strip()
    except Exception, e:
        print e
        return render_template('songci.html')

    scs = res.split('\n')[1:-1]
    db.songci.insert_one({'host': get_addr(request), 'content': scs})
    count = db.counter.find_one({'counter': 'songci'})['lines']
    db.counter.update_one({'counter': 'songci'}, {'$inc': {'value': 1, 'lines': len(scs)}})

    return render_template('songci.html', scs=scs, count=count)


@app.route('/dot')
def dot():
    return render_template('dot.html', title='Dot')


# @app.route('/seeleit.com.html')
# def ssl():
#     return 'bVFMVmE1aWl0OVI0Zk5oOE5aOVJtWkpkRHZXSnBuOTRpRmdVVHNEempPZz0'


# @app.route('/cat')
# def cat():
#     return render_template('cat.html')
#
#
#
#
# @app.route('/acg')
# def acg():
#     acgs = db.session.query(MarkDown).filter_by(cat='acg').all()
#     return render_template('cat2.html', title='ACG', cats=acgs)
#
#
# @app.route('/piece')
# def piece():
#     pieces = db.session.query(MarkDown).filter_by(cat='piece').all()
#     return render_template('cat2.html', title='Piece', cats=pieces)

#
# @app.route('/md/<id>')
# def md(id=None):
#     html = m.html(MarkDown.query.filter_by(id=id).one().content, extensions=('fenced-code',))
#
#     return render_template('blank.html', html=html)


def get_addr(req):
    if req.headers.getlist("X-Forwarded-For"):
        ip = req.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = req.remote_addr
    return ip

if __name__ == '__main__':
    app.run()
