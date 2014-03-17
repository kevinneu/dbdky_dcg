#!/usr/bin/python

import asyncore
import logging
import socket

from cacClient import *

logging.basicConfig(level=logging.DEBUG,
	format='%(name)-11s: %(message)s',)

address = ('localhost', 6001)
ip, port = address

client = cacClient(ip, port, message='Hello')

asyncore.loop()