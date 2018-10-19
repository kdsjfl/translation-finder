# -*- coding: utf-8 -*-
#
# Copyright © 2018 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate translation-finder
# <https://github.com/WeblateOrg/translation-finder>
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
from __future__ import unicode_literals, absolute_import

import os.path

from .finder import PurePath
from .test_discovery import DiscoveryTestCase
from .api import discover


class APITest(DiscoveryTestCase):
    def test_discover(self):
        paths = ["locales/cs/messages.po", "locales/de/messages.po"]
        self.assert_discovery(
            discover(PurePath("."), [PurePath(path) for path in paths]),
            [{"filemask": "locales/*/messages.po", "file_format": "po"}],
        )

    def test_discover_files(self):
        self.assert_discovery(
            discover(os.path.join(os.path.dirname(__file__), "test_data")),
            [
                {"filemask": "locales/*.po", "file_format": "po"},
                {
                    "filemask": "app/src/res/main/values-*/strings.xml",
                    "file_format": "aresource",
                    "template": "app/src/res/main/values/strings.xml",
                },
            ],
        )
