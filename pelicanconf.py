#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = "theme/"
AUTHOR = 'Leonardo Flores'
SITENAME = 'Leonardo Flores'
SITETITLE = 'Leonardo Flores'
SITESUBTITLE = 'B.Sc in Information Systems, Full-stack & Nutella Developer and Knowledge Hunter.'
SITEDESCRIPTION = 'Blog about dev guides and tools.'
BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'
DEFAULT_PAGINATION = 10
PATH = 'content'
MAIN_MENU = False

# Language configs
TIMEZONE = 'America/Sao_Paulo'
I18N_TEMPLATES_LANG = 'pt_BR'
DEFAULT_LANG = 'pt_BR'
OG_LOCALE = 'pt_BR'
LANGUAGE = 'pt_BR'
LOCALE = 'pt_BR'
DEFAULT_DATE_FORMAT = '%d de %B de %Y'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Contact', ''),)

# Social widget
SOCIAL = (('facebook', 'https://facebook.com/leonardo.claw/'),
          ('linkedin', 'https://www.linkedin.com/in/leonardocouy/'),
          ('github', 'https://github.com/leonardocouy/'),
          ('twitter', 'https://twitter.com/_iamleofc'),
          ('rss', '//leonardocouy.com/feeds/all.atom.xml'))

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME', 'static']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/CNAME': {'path': 'CNAME'}
}

CUSTOM_CSS = 'theme/custom.css'

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'