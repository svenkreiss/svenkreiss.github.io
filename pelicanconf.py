#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sven Kreiss'
SITENAME = u'Sven Kreiss'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Make about page the front page
INDEX_SAVE_AS = 'blog/index.html'

# Blogroll
LINKS = (
    ('unicodeit.net', 'http://www.unicodeit.net'),
)

# Social widget
SOCIAL = (
    ('rss', 'https://trivial.io'),
    ('github', 'https://github.com/svenkreiss/'),
    ('twitter', 'https://twitter.com/svenkreiss'),
    ('linkedin', 'https://www.linkedin.com/in/svenkreiss/'),
    ('envelope', 'mailto:me@svenkreiss.com'),
    ('file-text', '/files/cv.html'),
)
TWITTER_USERNAME = 'svenkreiss'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PATH = 'content'
PAGE_EXCLUDES = ['files']
ARTICLE_EXCLUDES = ['files', 'pages']

STATIC_PATHS = ['images', 'files', 'extras']

EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/CNAME': {'path': 'CNAME'},
}

THEME = "../pelican-theme-pure"

# plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [
    'sitemap', 'gravatar', 'render_math',
    'liquid_tags.img', 'liquid_tags.video',
    'liquid_tags.youtube', 'liquid_tags.vimeo',
    'liquid_tags.include_code',
    # 'liquid_tags.notebook',
    'representative_image',
    'image_process',
    'pelican-cite',
    'related_posts',
]

# Pelican cite plugin
PUBLICATIONS_SRC = 'content/publications.bib'

# Image Process plugin
IMAGE_PROCESS = {
    'crisp': {'type': 'responsive-image',
              'srcset': [('1x', ["scale_in 800 600 True"]),
                         ('2x', ["scale_in 1600 1200 True"]),
                         ('4x', ["scale_in 3200 2400 True"]),
                         ],
              'default': '1x',
              },
    'large-photo': {'type': 'responsive-image',
                    'sizes': '(min-width: 1200px) 800px, (min-width: 992px) 650px, (min-width: 768px) 718px, 100vw',
                    'srcset': [('600w', ["scale_in 600 450 True"]),
                               ('800w', ["scale_in 800 600 True"]),
                               ('1600w', ["scale_in 1600 1200 True"]),
                               ],
                    'default': '800w',
                    },
}

# pure theme specific
COVER_IMG_URL = '/images/winter_mountains_1600.jpeg'
AUTHOR_EMAIL = 'me@svenkreiss.com'
AUTHOR_IMAGE = '/images/me_nyc_square_500.jpeg'
TAGLINE = 'Data Scientist with a focus on Machine&nbsp;Learning and Computer&nbsp;Vision.'
META_DESCRIPTION = 'my personal website'
# DISQUS_SITENAME = 'svenkreisscom'
COPYRIGHT_YEARS = '2014 &ndash; 2018'

ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
AUTHOR_URL = 'blog/author/{slug}/'
AUTHOR_SAVE_AS = 'blog/author/{slug}/index.html'
CATEGORY_URL = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'

# do not make pages of the type {slug}/index.html as this clashed with
# other github repositories with the same name as {slug}
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

ARCHIVES_SAVE_AS = 'blog/archives.html'
AUTHORS_SAVE_AS = 'blog/authors.html'
CATEGORIES_SAVE_AS = 'blog/categories.html'
TAGS_SAVE_AS = 'blog/tags.html'

MENUITEMS = [
    ('About', ''),
    ('Projects', 'projects.html'),
    ('Blog: trivial.io', 'files/forward_trivialio.html'),
]
DISPLAY_PAGES_ON_MENU = True


# plugin render_math
MATH = {'color': 'blue', 'align': 'left'}

TYPOGRIFY = True
