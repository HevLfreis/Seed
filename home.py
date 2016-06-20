# coding: utf-8
import codecs

import misaka as m
from flask import render_template, send_from_directory

from config import app


@app.route('/static/images/md/<path>')
def send_md_img(path):
    return send_from_directory(app.static_folder+'/images/md/', path)


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
    return render_template('index.html')


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


@app.route('/resume')
def resume():
    with codecs.open(app.static_folder+'/files/md/resume.md', 'r', encoding='utf8') as f:
        text = f.read()
    res = m.html(text)
    return render_template('blank.html', html=res)

#
# @app.route('/md/<id>')
# def md(id=None):
#     html = m.html(MarkDown.query.filter_by(id=id).one().content, extensions=('fenced-code',))
#
#     return render_template('blank.html', html=html)


if __name__ == '__main__':

    app.run(debug=True)

