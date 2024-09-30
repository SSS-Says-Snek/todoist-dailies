"""This only exists because I can only import stuff from the outside :sob:"""

from src import main

pkgdatadir = r"/usr/local/share/todoist_dailies"

import os
import gi

gi.require_version("Gio", "2.0")

from gi.repository import Gio
resource = Gio.Resource.load(os.path.join(pkgdatadir, 'todoist_dailies.gresource'))
resource._register() # type: ignore

main.main()
