# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'RandomForest Cloud'
copyright = '2024, RandomForest Cloud'
author = 'RandomForest Cloud'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_logo = "logo_hd.svg"

html_theme_options = {
    'navigation_depth': 4,
    'logo_only': True,
    'display_version': False,
}


