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
from FileUtils import createDirectory, writeFile
from FileManagerUtils import FILE_OP_DELETE, FILE_OP_MOVE


class Test6():

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
		self.callback = callback
		self.file_manager.execFileManagerOp(FILE_OP_DELETE, self.source + "/test4", None, self.prepareTest1)

	def prepareTest1(self, *__):
		self.file_manager.execFileManagerOp(FILE_OP_DELETE, self.destination + "/test4", None, self.prepareTest2)

	def prepareTest2(self, *__):
		if self.source and self.destination:
			createDirectory(self.source + "/test4/test11/test111")
			writeFile(self.source + "/test4/file1.ts", "test")
			writeFile(self.source + "/test4/test11/file11.ts", "test")
			writeFile(self.source + "/test4/test11/file12.ts", "test")
			writeFile(self.source + "/test4/test11/test111/file111.ts", "test")
			self.file_manager.loadDatabase()
			self.file_manager.onDatabaseLoaded(self.databaseLoaded)
		else:
			logger.debug("terminating test...")
			self.callback(False)

	def databaseLoaded(self):
		logger.info("...")
		self.file_manager.execFileManagerOp(FILE_OP_MOVE, self.source + "/test4", self.destination, self.copyCallback)

	def copyCallback(self, _file_op, _path, _target_dir, error):
		success = error == 0
		success = success and (
			self.file_manager.exists(self.destination + "/test4")
			and self.file_manager.exists(self.destination + "/test4/test11")
			and self.file_manager.exists(self.destination + "/test4/test11/test111")
			and self.file_manager.exists(self.destination + "/test4/file1.ts")
			and self.file_manager.exists(self.destination + "/test4/test11/file11.ts")
			and self.file_manager.exists(self.destination + "/test4/test11/file12.ts")
			and self.file_manager.exists(self.destination + "/test4/test11/test111/file111.ts")
			and os.path.exists(self.destination + "/test4")
			and os.path.exists(self.destination + "/test4/test11")
			and os.path.exists(self.destination + "/test4/test11/test111")
			and os.path.exists(self.destination + "/test4/file1.ts")
			and os.path.exists(self.destination + "/test4/test11/file11.ts")
			and os.path.exists(self.destination + "/test4/test11/file12.ts")
			and os.path.exists(self.destination + "/test4/test11/test111/file111.ts")
		)
		success = success and not (
			self.file_manager.exists(self.source + "/test4")
			or self.file_manager.exists(self.source + "/test4/test11")
			or self.file_manager.exists(self.source + "/test4/test11/test111")
			or self.file_manager.exists(self.source + "/test4/file1.ts")
			or self.file_manager.exists(self.source + "/test4/test11/file11.ts")
			or self.file_manager.exists(self.source + "/test4/test11/file12.ts")
			or self.file_manager.exists(self.source + "/test4/test11/test111/file111.ts")
			or os.path.exists(self.source + "/test4")
			or os.path.exists(self.source + "/test4/test11")
			or os.path.exists(self.source + "/test4/test11/test111")
			or os.path.exists(self.source + "/test4/file1.ts")
			or os.path.exists(self.source + "/test4/test11/file11.ts")
			or os.path.exists(self.source + "/test4/test11/file12.ts")
			or os.path.exists(self.source + "/test4/test11/test111/file111.ts")
		)
		self.callback(success)
