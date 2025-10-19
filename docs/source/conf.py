# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sys
from pathlib import Path

sys.path.insert(0, str(Path("../..").absolute()))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "PySpotify"
copyright = "2025, Sebastian Domagała"
author = "Sebastian Domagała"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

add_module_names = False
python_use_unqualified_type_names = True
autodoc_typehints_format = "short"
napoleon_preprocess_types = True

autodoc_member_order = "groupwise"
autodoc_default_options = {
    "members": True,
    "no-undoc-members": True,
    "show-inheritance": True,
    "imported-members": False,
    "exclude-members": "model_config",
}

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
