#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kenneth Lyons'
SITENAME = 'Kenneth Lyons'
SITEURL = ''
THEME = 'theme'
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["references"]

DISPLAY_PAGES_ON_MENU = False

# tuple of (name, fontawesome icon, link) pairs
SOCIAL = [
    ('GitHub', 'fa-github',
        'https://github.com/ixjlyons'),
    ('LinkedIn', 'fa-linkedin-square',
        'https://www.linkedin.com/in/ixjlyons/'),
    ('Resume', 'fa-file-text-o',
        'https://www.dropbox.com/s/49t8ne7wbfsr0ni/cv.pdf?dl=1')
]

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

STATIC_PATHS = ['images', 'extra', 'documents']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

DEFAULT_PAGINATION = False
