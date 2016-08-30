# #!/usr/bin/env python
# # coding: utf-8
# # created by hevlhayt@foxmail.com
# # Date: 2016/5/18
# # Time: 12:03
# #
# from os.path import dirname, abspath
#
# PROJECT_DIR = dirname(dirname(abspath(__file__)))
#
# # import codecs
# # with codecs.open(PROJECT_DIR + '/Seed/static/files/README.md', 'r', encoding='utf8') as f:
# #     text = f.read()
# #
# # print text
# #
# #
# # import markdown
# # from mdx_gfm import GithubFlavoredMarkdownExtension
# #
# # md = markdown.Markdown(extensions=[GithubFlavoredMarkdownExtension()])
# # html = md.convert(text)
# #
# # print html
#
# # import scipy.io
# # mat = scipy.io.loadmat(PROJECT_DIR + '/Seed/static/files/karate.mat')
# #
# # print mat.get('A')
# #
# # import networkx as nx
# # D = nx.from_numpy_matrix(mat.get('A'))
# #
# # print D.nodes()
#
#
import codecs
import urllib2

import re
from bs4 import BeautifulSoup

# cn = codecs.open('cn.txt', 'w', 'utf-8')
# en = codecs.open('en.txt', 'w', 'utf-8')
#
# sym_reg = ur'[\u3002|\uff1f|\uff01|\uff0c|\u3001]'
# chn_reg = ur'[^\u4E00-\u9FA5]'
#
# for i in xrange(1, 30480):
#     print 'iter: ', i
#
#     try:
#         response = urllib2.urlopen('http://www.cuyoo.com/article-'+str(i)+'-1.html')
#     except:
#         print 'error: ', i
#         continue
#
#     data = response.read()
#     soup = BeautifulSoup(data, "html.parser")
#     en_news = soup.find(id='en')
#     if en_news:
#         # en_news = re.sub('[\n|(\((.|\s)*\))]', '', en_news.getText())
#         # print en_news.getText()
#         en_news_st = en_news.getText().split('.')
#         print len(en_news_st)
#
#     cn_news = soup.find(id='cn')
#     if cn_news:
#         print cn_news.getText()
#         cn_news = re.sub(ur'[\n|(\((.|\s)*\))]', '', cn_news.getText())
#         print '======='
#         print cn_news
#         cn_news_st = cn_news.split(u'。')
#         print len(cn_news_st)
#
#     a = raw_input()


