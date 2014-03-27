import tarfile
from contextlib import closing
from ConfigParser import SafeConfigParser

import os
import os.path

log_files = []

def visit(arg, dirname, names):
	#print dirname, arg
	print dirname
	for name in names:
		subname = os.path.join(dirname, name)
		if os.path.isdir(subname):
			continue
		else:
			log_files.append(subname)
	#print log_files

log_path='.'
log_file_prefix='dbdky_dcg_'
def loadConfig():
	parser = SafeConfigParser()
	parser.read('dcg_conf.ini')
		
	for section_name in parser.sections():
		for name, value in parser.items(section_name):
			if name == 'log_path':
				print('******%s', value)
				log_path = value
			elif name == 'log_file_prefix':
				log_file_prefix = value
			else:
				continue

if __name__ == '__main__':
	loadConfig()
	print('######%s', log_path)
	os.path.walk(log_path, visit, '(User data)')

	



# with closing(tarfile.open('tarfile_test.tar', mode='w')) as out:
# 	out.add('cacClient.py')
# 	out.add('cacClientMain.py')

	
		