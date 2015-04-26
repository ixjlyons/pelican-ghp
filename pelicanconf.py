#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kenneth Lyons'
SITENAME = 'Kenneth Lyons'
SITESUBTITLE = 'thought for your thoughts'
SITEURL = ''
THEME = 'theme'
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["render_math"]

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (('github', 'https://github.com/ixjlyons'),
          ('bitbucket', 'https://bitbucket.org/ixjlyons'),
          ('linkedin', 'https://www.linkedin.com/pub/kenneth-lyons/70/61b/21b'))

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_PAGINATION = False
