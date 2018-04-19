#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'YliesC'
SITENAME = u'The Golden Koala'
SITEURL = u'http://yliesc.github.io'

PATH = 'content'
THEME = "pelican-themes/pelican-bootstrap3"
PAGES_SORT_ATTRIBUTE = 'order'

TIMEZONE = 'Europe/Paris'

FAVICON = 'images/koala-ico.png'
SITELOGO = 'images/koala-logo.svg'
THUMBNAIL_DEFAULT = '/images/koala-logo.svg'
SEARCH_URL = '/blog/search'
# BANNER = 'images/koala-logo.png'
# BANNER_SUBTITLE = 'This is my subtitle'
SITELOGO_SIZE = 38

DEFAULT_LANG = u'fr'

PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = ['i18n_subsites', 'tipue_search', 'pelican-page-hierarchy']

MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.codehilite': { 'css_class': 'highlight' },
    'markdown.extensions.fenced_code': {},
    'markdown.extensions.extra': {},
    'markdown.extensions.toc': {}
  }
}

PYGMENTS_STYLE = 'default'

PATH_METADATA = 'pages/(?P<path>.*)\..*'

JINJA_EXTENSIONS = ['jinja2.ext.i18n']
I18N_SUBSITES = {
}

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'

BOOTSTRAP_THEME = 'readable'

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

ARTICLE_EXCLUDES = ['files']
STATIC_PATHS = ['images', 'content', 'files', 'files/licence_g1.rst', 'css']
CUSTOM_CSS = 'css/custom.css'


# Blogroll
LINKS = (('Link 1', 'https://example.org'),
         ('Link 2', 'https://example.org'),
         ('etc', '/page/content'),)

# Social widget
ACCEPTED_MENUS =  ['menu-1',
                   'menu-2',
                   'menu-3',
                   'menu-4',
                   'menu-5',
                   'menu-6']

SOCIAL = (('Link 1', 'https://example.org', 'comment'),
          ('Link 2', 'https://example.org', 'comments'),
          ('etc', '/page/content', 'etc'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

CC_LICENSE = "CC-BY-SA"

DISPLAY_ARTICLE_INFO_ON_INDEX = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
BOOTSTRAP_FLUID = False
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = False
SHOW_DATE_MODIFIED = True

GITHUB_USER = ''
GITHUB_SHOW_USER_LINK = True
GITHUB_SKIP_FORK = False
GITHUB_REPO_COUNT = 2

TWITTER_USERNAME = ''
