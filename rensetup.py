from setuptools import setup, find_packages
from pathlib import Path

text = Path("./jupyter_book/__init__.py").read_text(encoding="utf8")
for line in text.split("\n"):
    if "__version__" in line:
        break
version = line.split("= ")[-1].strip('"')

# Documentation requirements
path_doc_reqs = Path(__file__).parent.joinpath("docs", "requirements.txt")
doc_reqs = [
    ii
    for ii in path_doc_reqs.read_text(encoding="utf8").split("\n")
    if not ii.startswith("#")
]
# Test requirements
test_reqs = [
    "coverage",
    "texsoup",
    "pytest>=3.6,<4",
    "pytest-cov",
    "pytest-xdist",
    "pytest-timeout",
    "beautifulsoup4",
    "matplotlib",
    "pytest-regressions",
    "altair",
    "sphinx_click",
    "sphinx_tabs",
    "pyppeteer",
    "beautifulsoup4",
    "cookiecutter",
]
# Define all extras
extras = {
    "code_style": ["flake8<3.8.0,>=3.7.0", "black", "pre-commit==1.17.0"],
    "sphinx": doc_reqs,
    "testing": test_reqs,
    "pdfhtml": ["pyppeteer"],
}
# Set alias for all extras with "all"
extras["all"] = set(ii for jj in extras.values() for ii in jj)


setup(
    name="jupyter-book",
    version=version,
    python_requires=">=3.6",
    author="Sebastian Schwindt",
    author_email="sebastian.schwindt AT iws.uni-stuttgart.de",
    url="https://sebastian-schwindt.org/",
    project_urls={
        "Documentation": "https://hyrdroinformatics.readthedocs.io",
        "Funding": "https://sebastian-schwindt.org",
        "Source": "https://github.com/sschwindt/hydroinformatics/",
        "Tracker": "https://github.com/sschwindt/hydroinformatics/issues",
    },
    # this should be a whitespace separated string of keywords, not a list
    keywords="eco-hydraulics, morphodynamics, teaching, research, python, water resources",
    description="Online learning materials",
    long_description=open("./README.md", "r").read(),
    long_description_content_type="text/markdown",
    license="BSD",
    packages=find_packages(),
    install_requires=[
        "pyyaml",
        "docutils>=0.15,<0.17",
        "sphinx>=2,<4",
        "linkify-it-py~=1.0.1",
        "myst-nb~=0.12.0",
        "jupytext>=1.8,<1.11",
        "click",
        "setuptools",
        "nbformat",
        "nbconvert<6",
        "jsonschema",
        "sphinx_togglebutton",
        "sphinx-copybutton",
        "sphinx-comments",
        "sphinxcontrib-bibtex~=2.2.0",
        "sphinx_book_theme>=0.0.39",
        "sphinx-thebe>=0.0.6",
        "sphinx-panels~=0.5.2",
        "nested-lookup~=0.2.21",
        "jupyterbook-latex~=0.2.0",
    ],
    extras_require=extras,
    entry_points={
        "console_scripts": [
            "jb = jupyter_book.commands:main",
            "jupyter-book = jupyter_book.commands:main",
        ]
    },
    include_package_data=True,
)
