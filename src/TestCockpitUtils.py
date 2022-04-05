#!/usr/bin/python
# coding=utf-8
#
# Copyright (C) 2018-2022 by dream-alpha
#
# In case of reuse of this source code please do not remove this copyright.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# For more information on the GNU General Public License see:
# <http://www.gnu.org/licenses/>.


import os
from Debug import logger
from Plugins.SystemPlugins.MountCockpit.MountCockpit import MountCockpit


def countDiskFiles():
	bookmarks = MountCockpit.getInstance().getMountedBookmarks("MVC")
	count = 0
	for bookmark in bookmarks:
		for _root, _dirs, files in os.walk(bookmark, followlinks=True):
			for file in files:
				if os.path.splitext(file)[1] == ".ts":
					count += 1
	logger.debug("count: %s", count)
	return count
