#!/usr/bin/python
import asyncore
import logging
import socket

from ConfigParser import SafeConfigParser

from psuCagServer import *

logging.basicConfig(level=logging.DEBUG,
	format='%(name)--11s: %(message)s',)

parser = SafeConfigParser()
parser.read('dcg_conf.ini')

tIpAddress = 'localhost'
tPort = 6001

for section_name in parser.sections():
    for name, value in parser.items(section_name):
        if name == 'ipaddress':
            tIpAddress = value
        elif name == 'port':
            tPort = int(value)
        else:
            continue

address = (tIpAddress, tPort)

print address        
    
#address = ('localhost', 6001)
#address = ('192.168.199.106', 6001)
server = psuCagServer(address)
ip, port = server.address

asyncore.loop()