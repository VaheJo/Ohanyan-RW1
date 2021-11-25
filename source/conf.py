# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
numfig = True
numfig_secnum_depth = 3

# -- Project information -----------------------------------------------------

# project = u'Руководство по качеству группы клинической дозиметрии'
project = u'Ohanyan-RW1'
copyright = '2021, Oganyan'
author = u'Oganyan Vage Robertovich'

# The full version, including alpha/beta/rc tags
version = '1.0.0'  # this is meant to reference the version of EasyBuild
release = '0.0.1'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%d %B %Y'  # e.g., 03 Июня 2020

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.inkscapeconverter',
    'sphinxcontrib.spelling',
    'sphinxcontrib.bibtex'
]

image_converter = 'inkscape'
inkscape_converter_args = ['-d', '600']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ru'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = 'nature'

# https://github.com/readthedocs/sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": True,
    "display_version": True,
    "sticky_navigation": True,  # Set to False to disable the sticky nav while scrolling.
    "logo_only": True,  # if we have a html_logo below, this shows /only/ the logo with no title text
    "style_nav_header_background": "#FBFBFB",
}
html_context = {
    "display_github": True,
    "github_user": "greenstm137",
    "github_repo": "RWOfStudents",
    "github_version": "main",
    "conf_py_path": "/source/",
}
html_scaled_image_link = False
html_show_sourcelink = True
html_favicon = "../images/mephi_logo.jpg"
html_logo = "../images/mephi_logo.jpg"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# locale_dirs = ['locale/']   # path is example but recommended.
# gettext_compact = False     # optional.

master_doc = 'contents'

latex_elements = {
   'papersize': 'a4paper'
#    'pointsize': '10pt',
#    'pxunit': '0.75bp',
#    'babel': 'russian'
}

# Bibliography staff
# https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html
bibtex_bibfiles = ['refs.bib']
bibtex_encoding = 'latin'
bibtex_default_style = 'unsrt'

html_static_path = ["../_static"]
html_css_files = ["custom.css", "mystyle.css"]