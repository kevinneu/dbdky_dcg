from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import

from ConfigParser import SafeConfigParser

import logging


class cagAccessPoint:
	def __init__(self):
                self.logger = logging.getLogger('cagAccessPoint')
		#self.url = 'http://10.162.211.14:7003/TRANSFCAG/services/CAGAccessService?wsdl'
		#self.imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
		#self.imp.filter.add('http://10.162.211.14:7003/TRANSFCAG/services/')
                self._loadConfigs()
                self.imp = Import(self.schama, location=self.schema_location)
                self.imp.filter.add(self.cag_filter)
		self.d = ImportDoctor(self.imp)
		self.client = Client(self.url, doctor=self.d)
		
                
	def uploadCACData(self,data):
                result = self.client.service.uploadCACData(data)
                return result
		#return self.client.service.uploadCACData(data)
	
	def uploadCACHeartbeatInfo(self,data):
		return self.client.service.uploadCACHeartbeatInfo(data)

	def _loadConfigs(self):
                self.url = ''
                self.schema = ''
                self.schema_location = ''
                self.cag_filter = ''

                parser = SafeConfigParser()
                parser.read('dcg_conf.ini')

                for section_name in parser.sections():
                        for name, value in parser.items(section_name):
                                if name == 'cag_url':
                                        self.url = value
                                elif name == 'schema':
                                        self.schama = value
                                elif name == 'schema_location':
                                        self.schema_location = value
                                elif name == 'cag_filter':
                                        self.cag_filter = value
                                else:
                                        continue
