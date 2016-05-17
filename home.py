# coding: utf-8

from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Memo
import misaka as m


app = Flask(__name__)

mysql_link = 'mysql://root:12345678@127.0.0.1/seed?charset=utf8'
mysql_engine = create_engine(mysql_link, echo=False)
Base.metadata.create_all(mysql_engine)
Session = sessionmaker(bind=mysql_engine)
session = Session()


@app.route('/')
def seed():
    # memo = Memo(title='hello world', timestamp=datetime.datetime.today())
    #
    # session.add(memo)
    # session.commit()
    return render_template('index.html')


@app.route('/cat')
def cat():
    return render_template('cat.html')


@app.route('/memo')
def memo():
    memos = session.query(Memo).all()
    return render_template('memo.html', memos=memos)


@app.route('/memo/<id>')
def memocat(id=None):
    # PROJECT_DIR = dirname(dirname(abspath(__file__)))
    #
    # import codecs
    # with codecs.open(PROJECT_DIR + '/Seed/static/files/README.md', 'r', encoding='utf8') as f:
    #     text = f.read()
    # #
    # # # file = open(PROJECT_DIR + '/Seed/static/files/README.md', 'rb').read()
    # # # print chardet.detect(file)
    # memo = Memo(title='hello world', content=text, timestamp=datetime.datetime.today())
    #
    # session.add(memo)
    # session.commit()
    # import markdown
    # print session.query(Memo).filter(Memo.id == id).one().content
    # html = markdown.markdown()


    html = m.html(session.query(Memo).filter(Memo.id == id).one().content, extensions=('fenced-code',))

    return render_template('blank.html', html=html)


if __name__ == '__main__':
    app.run(debug=True)
