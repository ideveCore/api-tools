# actions.py
#
# Copyright 2023 Ideve Core
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import Callable, List, Union
import gi

gi.require_version("Adw", "1")
from gi.repository import Adw, Gio
from .define import APP_ID, VERSION


def setup_application_actions(application: Adw.Application):
    def create_action(
        name: str,
        callback: Callable,
        shortcuts: Union[List[str], None] = None,
    ) -> None:
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        application.add_action(action)
        if shortcuts:
            application.set_accels_for_action(f"app.{name}", shortcuts)

    def about_action(widget, _):
        """Callback for the app.about action."""
        about = Adw.AboutWindow(
            transient_for=application.props.active_window,
            application_name="API tools",
            application_icon=APP_ID,
            developer_name="IdeveCore",
            version=VERSION,
            developers=["Ideve Core"],
            copyright="© 2023 Ideve Core",
        )
        about.present()

    def preferences_action(widget, _):
        """Callback for the app.preferences action."""
        print("app.preferences action activated")

    create_action("quit", lambda *_: application.quit(), ["<primary>q"])
    create_action("about", about_action)
    create_action("preferences", preferences_action)
    application.set_accels_for_action("win.show-help-overlay", ["<Primary>question"])
