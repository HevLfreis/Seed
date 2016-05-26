# coding: utf-8
import datetime

from flask import Flask, render_template, send_from_directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, MarkDown, Log
import misaka as m


app = Flask(__name__, static_folder='static')

mysql_link = 'mysql://root:12345678@127.0.0.1/seed?charset=utf8'
mysql_engine = create_engine(mysql_link, echo=False, pool_recycle=7200)
Base.metadata.create_all(mysql_engine)
Session = sessionmaker(bind=mysql_engine)
session = Session()


@app.route('/static/images/md/<path>')
def send_md_img(path):

    return send_from_directory(app.static_folder+'/images/md/', path)


@app.route('/')
def seed():

    try:

        log = Log(timestamp=datetime.datetime.today())
        session.add(log)
        session.commit()

        return render_template('index.html')
    except Exception, e:
        print 'Seed Exception: ', e
    finally:
        print 'Seed'


@app.route('/cat')
def cat():
    return render_template('cat.html')


@app.route('/memo')
def memo():
    memos = session.query(MarkDown).filter_by(cat='memo').all()
    # print memos
    return render_template('cat2.html', title='Memo', cats=memos)


@app.route('/acg')
def acg():
    acgs = session.query(MarkDown).filter_by(cat='acg').all()
    return render_template('cat2.html', title='ACG', cats=acgs)


@app.route('/piece')
def piece():
    pieces = session.query(MarkDown).filter_by(cat='piece').all()
    return render_template('cat2.html', title='Piece', cats=pieces)


@app.route('/md/<id>')
def md(id=None):
    html = m.html(session.query(MarkDown).filter(MarkDown.id == id).one().content, extensions=('fenced-code',))

    return render_template('blank.html', html=html)


if __name__ == '__main__':

    app.run(debug=True)

