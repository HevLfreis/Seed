# coding: utf-8
import codecs

import misaka as m
import subprocess
from flask import render_template, send_from_directory, request

from config import app, logger


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
    logger.info('('+request.remote_addr+')')
    return render_template('index.html')


@app.route('/resume')
def resume():
    logger.info('('+request.remote_addr+')')
    with codecs.open(app.static_folder+'/files/md/resume.md', 'r', encoding='utf8') as f:
        text = f.read()
    res = m.html(text)
    return render_template('blank.html', html=res)


@app.route('/songci')
def songci():
    logger.info('('+request.remote_addr+')')

    sh = ". /home/hevlfreis/torch/install/bin/torch-activate;" \
                 "th /home/hevlfreis/torch/torch-rnn/sample.lua " \
                 "-checkpoint /home/hevlfreis/model/songci/checkpoint_53000.t7 " \
                 "-length " + "250" + " -gpu -1"

    try:

        res = subprocess.check_output(sh, shell=True).strip()
    except Exception, e:
        print e
        return render_template('songci.html')

    scs = res.split('\n')

    return render_template('songci.html', scs=scs)

# @app.route('/seeleit.com.html')
# def ssl():
#     return 'bVFMVmE1aWl0OVI0Zk5oOE5aOVJtWkpkRHZXSnBuOTRpRmdVVHNEempPZz0'


# @app.route('/cat')
# def cat():
#     return render_template('cat.html')
#
#
# @app.route('/memo')
# def memo():
#     memos = db.session.query(MarkDown).filter_by(cat='memo').all()
#     # print memos
#     return render_template('cat2.html', title='Memo', cats=memos)
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

if __name__ == '__main__':
    app.run()

