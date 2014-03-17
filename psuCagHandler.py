#!/usr/bin/python
import asynchat
import logging

class psuCagHandler(asynchat.async_chat):
	ac_in_buffer_size = 65535
	ac_out_buffer_size = 1

	def __init__(self, sock):
		self.received_data = []
		self.logger = logging.getLogger('psuCagHandler')
		asynchat.async_chat.__init__(self, sock)
		self.process_data = self._process_command
		self.set_terminator('\n\n')

		return

	def collect_incoming_data(self, data):
		self.logger.debug('collect_incoming_data() -> (%d bytes) %r',
			len(data), data)
		self.received_data.append(data)

	def found_terminator(self):
		self.logger.debug('found_terminator()')
		self.process_data

	def _porcess_data(self):
		command = ''.join(self.received_data)
		self.logger.debug('_process_command() %r', command)

	def _process_command(self):
		self.logger.debug('_process_command()')
		
	def _process_message(self):
		self.logger.debug('_process_message()')
		self.close_when_done()