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
from __init__ import _
from Screens.Screen import Screen
from Components.Pixmap import Pixmap
from Components.Button import Button
from Components.Label import Label
from Components.Sources.List import List
from Components.ActionMap import ActionMap
from Components.config import config
from ConfigScreen import ConfigScreen
from Screens.MessageBox import MessageBox
from SkinUtils import getSkinName
from CockpitContextMenu import CockpitContextMenu
from Plugins.SystemPlugins.CacheCockpit.FileManager import FileManager
from Test1 import Test1 # pylint: disable=W0611
from Test2 import Test2 # pylint: disable=W0611
from Test3 import Test3 # pylint: disable=W0611
from Test4 import Test4 # pylint: disable=W0611
from Test5 import Test5 # pylint: disable=W0611
from Test6 import Test6 # pylint: disable=W0611
from Test7 import Test7 # pylint: disable=W0611
from Test8 import Test8 # pylint: disable=W0611
#from Test9 import Test9 # pylint: disable=W0611
#from Test10 import Test10 # pylint: disable=W0611
#from Test11 import Test11 # pylint: disable=W0611


class TestCockpit(Screen):

	def __init__(self, session):
		logger.info("...")
		Screen.__init__(self, session)
		self.skinName = getSkinName("TestCockpit")

		if self.skinName == getSkinName("NoSupport"):
			actions = {
				"cancel":	self.exit,
			}
		else:
			actions = {
				"menu":		self.openContextMenu,
				"cancel":	self.exit,
				"red":		self.exit,
				"green":	self.green,
				"ok":		self.ok
			}

		self["actions"] = ActionMap(
			["OkCancelActions", "ColorActions", "MenuActions"],
			actions,
			prio=-1
		)

		self.setTitle(_("TestCockpit"))
		self["no_support"] = Label()
		self["preview"] = Pixmap()
		self["key_green"] = Button(_("Run all"))
		self["key_red"] = Button(_("Exit"))
		self["key_yellow"] = Button()
		self["key_blue"] = Button()

		self.list = []
		self.list.append(("Test 1: CacheCockpit: Load cache"))
		self.list.append(("Test 2: CacheCockpit: Delete File(s)"))
		self.list.append(("Test 3: CacheCockpit: Copy File(s) to same bookmark"))
		self.list.append(("Test 4: CacheCockpit: Copy File(s) to different bookmark"))
		self.list.append(("Test 5: CacheCockpit: Move File(s) to same bookmark"))
		self.list.append(("Test 6: CacheCockpit: Move File(s) to different bookmark"))
		self.list.append(("Test 7: CacheCockpit: PurgeTrashcan"))
		self.list.append(("Test 8: CacheCockpit: Abort large file move"))
		#self.list.append(("Test 9: MovieCockpit: Start/stop recording"))
		#self.list.append(("Test 6: Move File(s) to different bookmark"))
		self["list"] = List(self.list)

		self.file_manager = FileManager.getInstance()
		self.run_all = False
		self.success = True
		self.index = 0

		self.onShow.append(self.onDialogShow)

	def onDialogShow(self):
		logger.info("...")

	def onSelectionChanged(self):
		logger.info("...")

	def ok(self):
		self.index = self["list"].getIndex()
		self.success = True
		self.file_manager.onDatabaseLoaded(self.runTest)

	def runTest(self):
		logger.info("self.runTest%d()" % (self.index + 1))
		self["list"].setIndex(self.index)
		exec("Test%d(self.session).start(self.runTestCallback)" % (self.index + 1))

	def runTestCallback(self, success):
		logger.info("self.index: %s, success: %s", self.index, success)
		self.success = self.success and success
		if not self.run_all or self.index >= len(self.list) - 1 or not self.success:
			logger.debug("stopping...")
			self.run_all = False
			msg = _("completed successfully.") if self.success else _("failed.")
			self.session.open(MessageBox, _("Test(s) ") + msg, MessageBox.TYPE_INFO)
		else:
			self.index += 1
			self.runTest()

	def openContextMenu(self):
		self.session.open(
			CockpitContextMenu,
			self,
		)

	def openConfigScreen(self):
		logger.info("...")
		self.session.openWithCallback(self.openConfigScreenCallback, ConfigScreen, config.plugins.testcockpit)

	def openConfigScreenCallback(self, _result=None):
		logger.info("...")

	def exit(self):
		logger.info("...")
		self.close()

	def green(self):
		if not self.run_all:
			self.index = 0
			self.success = True
			self.run_all = True
			self.file_manager.onDatabaseLoaded(self.runTest)
