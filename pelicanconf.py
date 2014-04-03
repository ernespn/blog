#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ernesto Perez'
SITENAME = u'Ernesto vs Code'
SITEURL = 'http://ernespn.github.io/blog'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_PAGES_ON_MENU = True

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
THEME = 'notmyidea'
OUTPUT_PATH = 'output'
PATH = 'content'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

# Custom Home page
#DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
#PAGINATED_DIRECT_TEMPLATES = (('blog',))
#TEMPLATE_PAGES = {'home.html': 'index.html',}

#STATIC_PATHS  = ['blog']
GITHUB_URL = 'http://github.com/ernespn/'
