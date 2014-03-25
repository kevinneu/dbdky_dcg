#!/usr/bin/python
import asyncore
import logging
import socket

from psuCagServer import *

logging.basicConfig(level=logging.DEBUG,
	format='%(name)--11s: %(message)s',)

address = ('localhost', 6001)
#address = ('192.168.199.106', 6001)
server = psuCagServer(address)
ip, port = server.address

asyncore.loop()