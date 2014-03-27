import logging
from ConfigParser import SafeConfigParser
import datetime

import os
import os.path

import glob
import logging.handlers


class logUtil:
	def __init__(self):
		parser = SafeConfigParser()
		parser.read('dcg_conf.ini')
		self.currentDate = datetime.date.today()
		self.dateformat = '%a %b %d'

		for section_name in parser.sections():
			for name, value in parser.items(section_name):
				if name == 'log_path':
					self.log_path = value
				elif name == 'log_file_prefix':
					self.log_file_prefix = value
				elif name == 'log_size_per_file':
					self.log_size_per_file = long(value)
				elif name == 'log_piece_num':
					self.log_piece_num = int(value)
				elif name == 'log_backup_period':
					self.log_backup_period = int(value)
				elif name == 'log_backup_duration':
					self.log_backup_duration = int(value)
				else:
					continue

		self.log_file_name = self.log_path
		self.log_file_name += '/'
		self.log_file_name += self.log_file_prefix

		self.currentDate = None
		self._updateLogFileName()
		self._updateLogFile()

	def _updateLogFileName(self):
		d = datetime.date.today()
		if self.currentDate == None:
			self.currentDate = d
			self.log_file_name += str(d)
			self.log_file_name += '.log'
			self._updateLogFile()
		elif self.currentDate != d:
			self.currentDate = d
			self.log_file_name = self.log_path
			self.log_file_name += '/'
			self.log_file_name += self.log_file_prefix

			self.log_file_name += str(d)
			self.log_file_name += '.log'
			self._updateLogFile()
		# else:
		# 	logger.debug('self.log_file_name: %s', self.log_file_name)

	
	def _updateLogFile(self):
		if not os.path.exists(self.log_path):
			os.mkdir(self.log_path)

		self.logger = logging.getLogger('dbdky_dcg')
		self.logger.setLevel(logging.DEBUG)
		self.fh = logging.FileHandler(self.log_file_name)
		self.fh.setLevel(logging.DEBUG)
		self.formatter = logging.Formatter('%(asctime)s\t%(name)--11s\t%(levelname)--11s\t%(message)s')
		self.fh.setFormatter(self.formatter)
		self.logger.addHandler(self.fh)


	def info(self, module, message):
		self.logger.info('%s:\t%s', module, message)

	def debug(self, module, message):
		self.logger.debug('%s:\t%s', module, message)

	def critical(self, module, message):
		self.logger.critical('%s:\t%s', module, message)

	def warning(self, module, message):
		self.logger.warning('%s:\t%s', module, message)


# if __name__ == '__main__':
# 	log = logUtil()
# 	log.debug('server->cag', 'debug info')
# 	log.critical('server->cag', 'critical info')
# 	log.warning('server->cag', 'warning info')
