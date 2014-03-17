#!/usr/bin/python
import asyncore
import logging
import socket

from psuCagHandler import *

class psuCagServer(asyncore.dispatcher):
	def __init__(self, address):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind(address)
		self.address = self.socket.getsockname()
		self.listen(1)

		return

	def handle_accept(self):
		client_info = self.accept()
		psuCagHandler(sock=client_info[0])
		self.handle_close()

		return

	def handle_close(self):
		self.close()