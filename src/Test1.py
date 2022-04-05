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


from Debug import logger
from Plugins.SystemPlugins.CacheCockpit.FileManager import FileManager
from Plugins.SystemPlugins.MountCockpit.MountCockpit import MountCockpit
from TestCockpitUtils import countDiskFiles


class Test1():

	def __init__(self, _session):
		logger.info("...")
		self.file_manager = FileManager.getInstance()

	def start(self, callback):
		self.callback = callback
		self.count = countDiskFiles()
		self.file_manager.loadDatabase()
		self.file_manager.onDatabaseLoaded(self.databaseLoaded)

	def databaseLoaded(self):
		logger.info("...")
		home_dir = MountCockpit.getInstance().getHomeDir("MVC")
		count, _size = self.file_manager.getCountSize(home_dir)
		logger.debug("cache count: %s", count)
		success = self.count == count
		self.callback(success)
