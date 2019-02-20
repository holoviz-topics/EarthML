# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

###################################################
# edit things below as appropriate for your project

project = u'EarthML'
authors = u'Anaconda'
copyright = u'2018-2019 ' + authors
description = 'Python tools for earth science and machine learning'

version = '0.0.1'
release = '0.0.1'

nbbuild_cell_timeout = 10000

html_static_path += ['_static']
html_theme = 'sphinx_ioam_theme'
# logo file etc should be in html_static_path, e.g. _static


html_theme_options = {
    'logo':'logo.png',
    'favicon':'favicon.ico',
    'custom_css':'site.css'
}

_NAV =  (
    ('Introduction', 'index'),
    ('Tutorial', 'tutorial/index'),
    ('Topics', 'topics/index'),
    ('FAQ', 'FAQ'),
    ('About', 'about')
)

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    'WEBSITE_SERVER': 'https://pyviz-topics.github.io/EarthML/',
    'VERSION': version,
    'NAV': _NAV,
    # by default, footer links are same as those in header
    'LINKS': _NAV,
    'SOCIAL': (
        ('Github', '//github.com/pyviz-topics/EarthML'),
    )
})
