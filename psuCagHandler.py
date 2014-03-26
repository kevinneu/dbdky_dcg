#!/usr/bin/python
import asynchat
import logging

from xml.etree import ElementTree

from cagAccessPoint import *

class psuCagHandler(asynchat.async_chat):
	ac_in_buffer_size = 65535
	ac_out_buffer_size = 1

	def __init__(self, sock):
		self.received_data = []
		self.logger = logging.getLogger('psuCagHandler')
		asynchat.async_chat.__init__(self, sock)
		self.process_data = self._process_data
		self.set_terminator('\n\n')

		return

	def collect_incoming_data(self, data):
		self.logger.debug('collect_incoming_data() -> (%d bytes) %r',
			len(data), data)
		self.received_data.append(data)

	def found_terminator(self):
		self.logger.debug('found_terminator()')
		self.process_data()

	def _process_data(self):
		command = ''.join(self.received_data)
		self.logger.debug('_process_data() %r', command)
		received_data = []
		self._deliver2Cag(command)

                result = self._deliver2Cag(command)
                
                if True == result:
                        self.push(chr(0x00))
                else:
                        self.push(chr(0xff))

		
	def _process_command(self):
		self.logger.debug('_process_command()')
		
	def _process_message(self):
		self.logger.debug('_process_message()')
		self.close_when_done()

	def _deliver2Cag(self, message):
		self.logger.debug('_deliver2Cag %s', message)
		client = cagAccessPoint()
		result = client.uploadCACData(message)
		return self._validResponse(result)

	def _validResponse(self, response):
                root = ElementTree.fromstring(response)
                result_node = root.find('result')
                if None == result_node:
                        open('result.txt', 'w+').write('222')
                        return False

                code = result_node.attrib['code']

                if code == '0':
                        return True
                else:
                        return False
                
		

