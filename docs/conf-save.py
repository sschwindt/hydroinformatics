# -*- coding: utf-8 -*-

import sys
import os
import re
import datetime

# If we are building locally, or the build on Read the Docs looks like a PR
# build, prefer to use the version of the theme in this repo, not the installed
# version of the theme.


def is_development_build():
    # PR builds have an interger version
    re_version = re.compile(r"^[\d]+$")
    if "READTHEDOCS" in os.environ:
        version = os.environ.get("READTHEDOCS_VERSION", "")
        if re_version.match(version):
            return True
        return False
    return True


sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("..") + "/img/")

# the following modules will be mocked (i.e. bogus imports - required for C-dependent packages)
autodoc_mock_imports = [
    "numpy",
    "pandas",
    "matplotlib",
]

import sphinx_rtd_theme
from sphinx.locale import _

# HEADER VARIABLES
author = "Sebastian Schwindt"
bibtex_bibfiles = ["references.bib"]
comments_config = {"hypothesis": False, "utterances": False}
copyright = "2021"
project = u"Hydroinformatics"
release = "latest"
slug = re.sub(r"\W+", "-", project.lower())
version = "0.1"

# Variable definitions
exclude_patterns = [
    "**.ipynb_checkpoints",
    "_build/*",
    "_build",
    "Thumbs.db",
    ".DS_Store"
]

# execution
execution_allow_errors = True
execution_excludepatterns = []
execution_in_temp = False
execution_timeout = 30

extensions = [
    "myst_nb",
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
    "jupyter_book",
    "jupyterbook_latex",
    "jupyter_sphinx",
    "sphinx_book_theme",
    "sphinx_click.ext",
    "sphinx_comments",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "sphinx_panels",
    "sphinx_thebe",
    "sphinx_togglebutton",
    "sphinx.ext.autodoc",
    "sphinxcontrib.bibtex",
    # "sphinxcontrib.googleanalytics",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

gettext_compact = False
globaltoc_path = os.path.abspath("..") + "/docs/_toc.yml"

# HTML settings
html_theme = "sphinx_book_theme"
html_theme_options = {
    "extra_navbar": 'Authored by <a href="https://sebastian-schwindt.org">Sebastian Schwindt</a>',
    "extra_footer": "",
    "google_analytics_id": "",
    "home_page_in_toc": True,
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "",
        "collapse_navigation": False,
        "notebook_interface": "classic", # or jupyterlab
        "jupyterhub_url": "",
        "thebe": False,
    },
    "path_to_docs": os.path.abspath("..") + "/docs/",
    "repository_url": "https://github.com/sschwindt/hyrdo-informatics/",
    "repository_branch": "main",
    "search_bar_text": "Search this book...",
    "use_edit_page_button": False,
    "use_issues_button": False,
    "use_repository_button": True,
}

html_context = {
    "date": datetime.date.today().strftime("%Y-%m-%d"),
    "display_github": True,
    "github_user": "sschwindt",
    "github_repo": "hyrdo-informatics",
    "github_version": "main/",
    "conf_py_path": "/docs/"
}

html_add_permalinks = "¶"
html_baseurl = ""
html_copy_source = True
html_favicon = os.path.abspath("..") + "/img/icons/favicon.ico"  # relative to source dir (where confy.py lives)
html_logo = "img/icons/icon.png"
html_show_sourcelink = True
html_sourcelink_suffix = ""
html_theme = "sphinx_book_theme"
html_title = "Hydroinformatics"

if not ("READTHEDOCS" in os.environ):
    html_static_path = [os.path.abspath("") + "/_static/"]
    html_js_files = ["debug.js"]

    # Add fake versions for local QA of the menu
    html_context["test_versions"] = list(map(
        lambda x: str(x / 10),
        range(1, 100)
    ))

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.8", None),
    "rtd": ("https://docs.readthedocs.io/en/latest/", None),
    "sphinx": ("http://www.sphinx-doc.org/en/stable/", None),
}

# jupytert
jupyter_execute_notebooks = "off"
jupyter_cache = ""

language = "en"

# latex
latex_documents = [
  (master_doc, "{0}.tex".format(slug), project, author, "manual"),
]
latex_engine = "pdflatex"

locale_dirs = ["locale/", os.path.abspath("..") + "docs/"]
man_pages = [
    (master_doc, slug, project, [author], 1)
]
master_doc = "index"

# myst
myst_enable_extensions = [
        "amsmath",
        "colon_fence",
        "deflist",
        "dollarmath",
        "html_admonition",
        "html_image",
        "linkify",
        "replacements",
        "smartquotes",
        "substitution"
]
myst_url_schemes = ("mailto", "http", "https")

# other
nb_output_stderr = "show"
nitpick_ignore = [
    ("py:class", "docutils.nodes.document"),
    ("py:class", "docutils.parsers.rst.directives.body.Sidebar"),
]
numfig = True
panels_add_bootstrap_css = False
pygments_style = "sphinx"
# source_suffix = {
#     ".rst": "restructuredtext",
#     ".txt": "restructuredtext",
#     ".md": "markdown",
# }
suppress_warnings = ["image.nonlocal_uri", "myst.domains"]
templates_path = ["_templates"]
texinfo_documents = [
  (master_doc, slug, project, author, slug, project, "Miscellaneous"),
]
thebe_config = {
    "repository_url": "https://github.com/binder-examples/jupyter-stacks-datascience",
    "repository_branch": "master",
}
use_jupyterbook_latex = True

# Extensions to theme docs
def setup(app):
    from sphinx.domains.python import PyField
    from sphinx.util.docfields import Field

    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
        doc_field_types=[
            PyField(
                "type",
                label=_("Type"),
                has_arg=False,
                names=("type",),
                bodyrolename="class"
            ),
            Field(
                "default",
                label=_("Default"),
                has_arg=False,
                names=("default",),
            ),
        ]
    )


# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_custom_sections = None
