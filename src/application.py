# application.py
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


import sys
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gio, Adw
from .define import RES_PATH, APP_ID
from .window import application_window
from .actions import setup_application_actions
from .utils import Utils

application = Adw.Application(
    application_id=APP_ID,
    flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
    resource_base_path=RES_PATH,
)


def application_startup(user_data: Adw.Application):
    user_data.utils = Utils(user_data)
    setup_application_actions(user_data)


def application_activate(user_data: Adw.Application):
    application_window(user_data).present()


application.connect("startup", application_startup)
application.connect("activate", application_activate)
