#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

DEFAULT_METADATA = {
    'Status': 'hidden',
}

USE_LOCAL_ASSETS = False

SITEURL = 'https://www.svenkreiss.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-4070485-2"
GOOGLE_ANALYTICS_URL = "www.svenkreiss.com"

#GAUGES_ANALYTICS = "54735740eddd5b086f007b96"
