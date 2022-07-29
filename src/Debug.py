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


from Version import ID, PLUGIN, VERSION
import logging
import os
import sys
import time
from Components.config import config, ConfigSubsection, ConfigDirectory, ConfigSelection  # pylint: disable=W0611


logger = None
streamer = None
format_string = (ID + ": " + "%(levelname)s: %(filename)s: %(funcName)s: %(message)s")
log_levels = {"ERROR": logging.ERROR, "INFO": logging.INFO, "DEBUG": logging.DEBUG}
plugin = PLUGIN.lower()
exec("config.plugins." + plugin + " = ConfigSubsection()")  # pylint: disable=W0122
exec("config.plugins." + plugin + ".debug_log_path = ConfigDirectory(default='/media/hdd')")  # pylint: disable=W0122
exec("config.plugins." + plugin + ".debug_log_level = ConfigSelection(default='INFO', choices=log_levels.keys())")  # pylint: disable=W0122


def initLogging():
	global logger
	global streamer
	if not logger:
		logger = logging.getLogger(ID)
		formatter = logging.Formatter(format_string)
		streamer = logging.StreamHandler(sys.stdout)
		streamer.setFormatter(formatter)
		logger.addHandler(streamer)
		logger.propagate = False
		setLogLevel(log_levels[eval("config.plugins." + plugin + ".debug_log_level").value])
		logger.info("********** %s %s **********", PLUGIN, VERSION)


def setLogLevel(level):
	logger.setLevel(level)
	streamer.setLevel(level)
	logger.info("level: %s", level)


def createLogFile():
	log_dir = eval("config.plugins." + plugin + ".debug_log_path").value
	log_file = os.path.join(log_dir, ID + "_" + time.strftime("%Y%m%d_%H%M%S" + ".log"))
	logger.info("log_file: %s", log_file)
	if os.path.exists(log_dir):
		os.popen("journalctl | grep " + ID + " > " + log_file)
	else:
		logger.error("log dir does not exist: %s", log_dir)
