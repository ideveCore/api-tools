# utils.py
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

from typing import Dict, Callable, Union, Any
import gi

gi.require_version("Adw", "1")
from gi.repository import Adw, Gio, GObject


class Settings(Gio.Settings):
    def __init__(self, application_id: str):
        super().__init__(schema_id=application_id)

    def bind(
        self,
        key: str,
        object: GObject.Object,
        property: str,
        flags: Gio.SettingsBindFlags,
    ):
        super().bind(key, object, property, flags)


class Navigation:
    def __init__(self) -> None:
        self.__current_navigation = ""
        self.__events = {"changed": []}

    def navigate(self, navigation: str, data: Dict[str, Any] = {}) -> None:
        if not navigation is None:
            self.__current_navigation = navigation
            self.__emit_changed(data)

    def __emit_changed(self, data: Dict[str, Any]):
        for event in self.__events["changed"]:
            event(self.__current_navigation, data)

    def connect(self, event: str, callback: Callable):
        self.__events[event].append(callback)


class Utils:
    def __init__(self, application: Adw.Application) -> None:
        self.settings = Settings(application.get_application_id())
        self.navigation = Navigation()
