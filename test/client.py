import asyncore
import logging
import socket
import sys

logging.basicConfig(level=logging.DEBUG,
	format='%(name)-11s: %(message)s',
	)

logger = logging.getLogger('client')

address = ('localhost', 6001)
message_data = open('test.XML', 'r').read()

logger.debug('message is %s:', message_data)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
	sock.connect(address)
	sock.sendall(message_data)
except exception, ex:
	logger.debug('exception')
	sock.close()
	exit()

try:
	sock.sendall('\n\n')
except exception, ex:
	logger.debug('exception')
	sock.close()

sock.close()
