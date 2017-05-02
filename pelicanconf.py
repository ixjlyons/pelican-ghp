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

PLUGIN_PATHS = ["custom-plugins"]
PLUGINS = ["references"]

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('Home', SITEURL+'/index.html'),
             ('About', SITEURL+'/pages/about.html'),
             ('Projects', SITEURL+'/pages/projects.html'),
             ('Publications', SITEURL+'/pages/publications.html')]

REFERENCES = {
    'template':
        """
        <p>
            <font color="#244668">
                {year} - <strong>{title}</strong>
            </font>
            <br>
            {authors}
            <br>
            <font color="#536f8b">
                <i>{proc}</i> {tail}
            </font>
        </p>
        """
}

# tuple of (name, fontawesome icon, link) pairs
SOCIAL = [
    ('GitHub', 'fa-github', 'https://github.com/ixjlyons'),
    ('LinkedIn', 'fa-linkedin-square', 'https://www.linkedin.com/in/ixjlyons/'),
    ('Resume', 'fa-file-text-o', 'https://www.dropbox.com/s/49t8ne7wbfsr0ni/cv.pdf?dl=1')
]

#AVATAR = SITEURL+'/images/north-coast.jpg'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_PAGINATION = False
