import tarfile
from contextlib import closing
from ConfigParser import SafeConfigParser

import os
import os.path

import re

import datetime

log_files = []
tar_files = []

def visit(arg, dirname, names):
	#print dirname, arg
	pattern = log_file_prefix
	pattern += '\S*.log'
	reg = re.compile(pattern)
	
	pattern1 = 'dbdky_dcg_backup_\S*.tar'
	reg1 = re.compile(pattern1)

	global log_files
	for name in names:
		subname = os.path.join(dirname, name)
		if os.path.isdir(subname):
			continue
		else:
			if reg.search(subname):
				log_files.append(subname)
			elif reg1.search(subname):
				tar_files.append(subname)

log_path='.'
log_file_prefix='dbdky_dcg_'
log_backup_duration=30


def loadConfig():
	parser = SafeConfigParser()
	parser.read('dcg_conf.ini')
		
	for section_name in parser.sections():
		for name, value in parser.items(section_name):
			if name == 'log_path':
				global log_path
				log_path = value
			elif name == 'log_file_prefix':
				global log_file_prefix
				log_file_prefix = value
			elif name == 'log_backup_duration':
				global log_backup_duration
				log_backup_duration = int(value)
			else:
				continue

def removeExpiredPatchers():
	global tar_files
	global log_backup_duration

	days_list = []
	for i in range(0, log_backup_duration):
		date_before = datetime.date.today() - datetime.timedelta(days=i)
		days_list.append(str(date_before))

	remain_list = []
	for tarfile in tar_files:
		for day in days_list:
			ret = tarfile.find(day)
			if ret != -1:
				remain_list.append(tarfile)

	delete_list = list(set(tar_files).difference(set(remain_list)))
	for dfile in delete_list:
		os.remove(dfile)

	
if __name__ == '__main__':
	loadConfig()
	os.path.walk(log_path, visit, '(User data)')
	removeExpiredPatchers()

	if log_files != []:
		d = datetime.date.today()
		tar_file_name = log_path
		tar_file_name += '/'
		tar_file_name += log_file_prefix
		tar_file_name += 'backup_'
		tar_file_name += str(d)
		tar_file_name += '.tar'

		with closing(tarfile.open(tar_file_name, mode='w')) as out:
			for fname in log_files:
				out.add(fname)

		for fname in log_files:
			os.remove(fname)

		log_files = []
		tar_files = []
