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
# import codecs
# import urllib2
#
# from bs4 import BeautifulSoup
#
# jitang = codecs.open('jitang.txt', 'w', 'utf-8')
#
# for i in xrange(1, 1609):
#     print 'iter: ', i
#
#     try:
#         response = urllib2.urlopen('http://www.59xihuan.cn/index_'+str(i)+'.html')
#     except:
#         print 'error: ', i
#         continue
#
#     data = response.read()
#     soup = BeautifulSoup(data, "html.parser")
#     for link in soup.find_all('a'):
#         # print link
#         if not link.get('title'):
#             a = link.get('href')
#             if a and (a.startswith(u'/yulu') or a.startswith(u'content')):
#                 jitang.write(link.string+'\n')
# jitang.close()

