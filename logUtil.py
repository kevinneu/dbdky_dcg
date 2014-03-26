import logging
from ConfigParser import SafeConfigParser
import datetime

import glob
import logging.handlers

# log_path=.
# log_file_prefix=dbdky_dcg_
# log_size_per_file=4096
# log_piece_num=10
# log_backup_period=1
# log_backup_duration=30

logging.basicConfig(level=logging.DEBUG,
	format='%(name)-11s: %(message)s',)


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
		logging.basicConfig(filename=self.log_file_name,
			level=logging.DEBUG,)


		# self.logger = logging.getLogger('logUtilLogger')
		# self.logger.setLevel(logging.DEBUG)
		# self.handler = logging.handlers.RotatingFileHandler(self.log_file_name,
		# 	maxBytes=self.log_size_per_file,
		# 	backupCount=self.log_piece_num,)
		# self.logger.addHandler(self.handler)

	def unittest(self):
		for i in range(20):
			logging.debug('i=%d' % i)


if __name__ == '__main__':
	logger = logging.getLogger('logUtil')
	logger.setLevel(logging.DEBUG)
	fh = logging.FileHandler('logUtil.log')
	fh.setLevel(logging.DEBUG)

	formatter = logging.Formatter('%s(asctime)s - %(name)s - %(levelname)s - %(message)s')

	fh.setFormatter(formatter)
	logger.addHandler(fh)

	logger.debug('This message should go to file')


