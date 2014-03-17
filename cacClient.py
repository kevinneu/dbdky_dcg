#!/usr/bin/python

import asynchat
import logging
import socket

class cacClient(asynchat.async_chat):
	ac_in_buffer_size = 1;
	ac_out_buffer_size = 65535

	def __init__(self, host, port, message):
		self.message = message
		self.logger = logging.getLogger('cacClient')
		asynchat.async_chat.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.logger.debug('connecting to %s', (host, port))
		self.connect((host, port))

		return

	def handle_connect(self):
		self.logger.debug('handle_connector()')

	def collect_incoming_data(self, data):
		self.logger.debug('collect_incoming_data() -> (%d) %r', len(data), data)
		self.received_data.append(data)

	def found_terminator(self):
		self.logger.debug('found_terminator()')
		received_message = ''.join(self.received_data)
		return
