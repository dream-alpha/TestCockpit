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


from Version import VERSION
from Debug import logger
from __init__ import _
from Plugins.Plugin import PluginDescriptor
from TestCockpit import TestCockpit
from SkinUtils import initPluginSkinPath, loadPluginSkin
from ConfigInit import ConfigInit


def startTestCockpit(session, **__):
	logger.info("...")
	initPluginSkinPath()
	loadPluginSkin("skin.xml")
	session.open(TestCockpit)


def Plugins(**__):
	logger.info("  +++ Version: %s starts...", VERSION)
	ConfigInit()
	return PluginDescriptor(
		name=_("TestCockpit"),
		description=_("Cockpit Test Suite"),
		where=[
			PluginDescriptor.WHERE_PLUGINMENU,
			PluginDescriptor.WHERE_EXTENSIONSMENU,
		],
		fnc=startTestCockpit
	)
