# Copyright (c) 2020 Teslabs Engineering S.L.
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime
import os
import re

# extensions
extensions = [
    "breathe",
    "exhale",
]

# obtain version
cmake = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "app", "CMakeLists.txt")
with open(cmake) as f:
    version = re.search(r"project\(.*VERSION\s+([0-9\.]+).*\)", f.read()).group(1)

# general
project = "app"
author = "Teslabs Engineering S.L."
year = datetime.now().year
copyright = "{:d}, Teslabs Engineering S.L.".format(year)
source_suffix = [".rst"]
master_doc = "index"

# html
html_static_path = ["_static"]
html_theme = "sphinx_rtd_theme"
html_logo = "_static/images/logo.png"
html_theme_options = {
    "logo_only": False,
    "display_version": True
}

# others
pygments_style = "sphinx"
numfig = True
mermaid_version = "8.5.2"

# breather & exhale
breathe_projects = {
    "app": "./doxyoutput/xml"
}

breathe_default_project = "app"

exhale_args = {
    "containmentFolder": "./api",
    "rootFileName": "index.rst",
    "rootFileTitle": "Application API",
    "doxygenStripFromPath": "..",
    "createTreeView": True,
    "exhaleExecutesDoxygen": True,
    "exhaleDoxygenStdin": "\n".join([
        "INPUT = ../app/include",
        "FILE_PATTERNS = *.h",
        "JAVADOC_AUTOBRIEF = YES",
        "OPTIMIZE_OUTPUT_FOR_C = YES",
        "EXCLUDE_SYMBOLS = z_*",
        "TAB_SIZE = 8",
    ])
}

cpp_id_attributes = [
    "__syscall"
]

c_id_attributes = cpp_id_attributes

def setup(app):
    app.add_stylesheet("css/custom.css")
