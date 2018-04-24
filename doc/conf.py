# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

###################################################
# edit things below as appropriate for your project

project = u'EarthML'
authors = u'Anaconda'
copyright = u'2018 ' + authors
description = 'Python tools for earth science and machine learning'

version = '0.0.1'
release = '0.0.1'

html_static_path += ['_static']
html_theme = 'sphinx_ioam_theme'
# logo file etc should be in html_static_path, e.g. _static
html_theme_options = {
#    'custom_css':'bettercolors.css',
#    'logo':'amazinglogo.png',
#    'favicon':'amazingfavicon.ico'
}

_NAV =  (
    ('Getting Started', 'getting_started/index'),
    ('User Guide', 'user_guide/index'),
    ('Gallery', 'gallery/index'),
    ('API', 'Reference_Manual/index'),
    ('FAQ', 'FAQ'),
    ('About', 'about')
)

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    # will work without this - for canonical (so can ignore when building locally or test deploying)
    'WEBSITE_SERVER': 'https://pyviz-topics.github.io/EarthML/',
    'VERSION': version,
    'NAV': _NAV,
    # by default, footer links are same as those in header
    'LINKS': _NAV,
    'SOCIAL': (
        ('Github', '//github.com/pyviz-topics/EarthML'),
    )
})
