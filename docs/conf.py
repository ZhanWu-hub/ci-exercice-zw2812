# conf.py for Sphinx documentation

# Project information
project = 'Your Project Name'

# Extensions
extensions = [
    'myst_parser',           # Enable Markdown support
    'sphinx.ext.autodoc',    # Autogenerate docs from docstrings
]

# Source file suffixes
source_suffix = {
    '.rst': 'restructuredtext',  # Support for reStructuredText
    '.md': 'markdown',           # Support for Markdown
}

# HTML theme
html_theme = 'furo'  # Use the Furo theme for HTML docs

