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
from Plugins.SystemPlugins.CacheCockpit.FileManager import FileManager
from Plugins.SystemPlugins.MountCockpit.MountCockpit import MountCockpit
from FileManagerUtils import FILE_OP_DELETE, FILE_OP_MOVE
from DelayTimer import DelayTimer


class Test8():

	def __init__(self, _session):
		logger.info("...")
		self.home_dir = MountCockpit.getInstance().getHomeDir("MVC")
		mounted_bookmarks = MountCockpit.getInstance().getMountedBookmarks("MVC")
		self.source = ""
		self.destination = ""
		if len(mounted_bookmarks) >= 2:
			self.source = mounted_bookmarks[0]
			self.destination = mounted_bookmarks[1]
		self.file_manager = FileManager.getInstance()

	def start(self, callback):
		logger.info("...")
		self.callback = callback
		self.file_manager.execFileManagerOp(FILE_OP_DELETE, self.source + "/bigfile.ts", None, self.prepareTest)

	def prepareTest(self, *__):
		logger.info("...")
		os.system("dd if=/dev/null of=" + self.source + "/bigfile.ts seek=1MB")

		self.file_manager.loadDatabase()
		self.file_manager.onDatabaseLoaded(self.databaseLoaded)

	def databaseLoaded(self):
		logger.info("...")
		self.callbacks = 0
		self.success = True
		self.file_manager.execFileManagerOp(FILE_OP_MOVE, self.source + "/bigfile.ts", self.destination, self.cancelCallback)
		DelayTimer(100, self.file_manager.cancelJobs)

	def cancelCallback(self, file_op, path, target_dir, error):
		logger.info("error: %s", error)
		logger.debug("file_op: %s, path: %s, target_dir: %s, error: %s", file_op, path, target_dir, error)
		self.success = self.success and error == 2
		self.success = self.success and (
			self.file_manager.exists(self.source + "/bigfile.ts")
			and os.path.exists(self.source + "/bigfile.ts")
		)
		self.success = self.success and not (
			self.file_manager.exists(self.destination + "/bigfile.ts")
			or os.path.exists(self.destination + "/bigfile.ts")
		)
		self.callback(self.success)
