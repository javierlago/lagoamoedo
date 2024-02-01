import os
import sys

sys.path.insert(0,os.path.abspath('C:\\Users\\a22javierla\\PycharmProjects\\lagoamoedo'))


project = 'LagoAmoedo'
copyright = '2024, Javier'
author = 'Javier'
release = 'v:0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc','sphinx.ext.intersphinx','sphinx.ext.ifconfig','sphinx.ext.viewcode','sphinx.ext.githubpages']

templates_path = ['_templates']
exclude_patterns = []

language = 'es'
source_patterns = '.rst'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'classic'
html_theme = 'haiku'
# html_static_path = ['_static']
