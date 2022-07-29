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
from enigma import eTimer


timer_instances = []


class DelayTimer():

	def __init__(self, delay, function, *args):
		timer_instances.append(self)
		self.function = function
		self.args = args
		self.timer = eTimer()
		self.timer_conn = self.timer.timeout.connect(self.fire)
		self.timer.start(delay, True)

	def fire(self):
		timer_instances.remove(self)
		self.timer.stop()
		try:
			self.function(*self.args)
		except Exception as e:
			logger.error("exception: %s", e)
