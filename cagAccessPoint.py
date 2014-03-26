from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import

import logging


class cagAccessPoint:
	def __init__(self):
                self.logger = logging.getLogger('cagAccessPoint')
		self.url = 'http://10.162.211.14:7003/TRANSFCAG/services/CAGAccessService?wsdl'
		self.imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
		self.imp.filter.add('http://10.162.211.14:7003/TRANSFCAG/services/')
		self.d = ImportDoctor(self.imp)
		self.client = Client(self.url, doctor=self.d)
		
                
	def uploadCACData(self,data):
                result = self.client.service.uploadCACData(data)
                return result
		#return self.client.service.uploadCACData(data)
	
	def uploadCACHeartbeatInfo(self,data):
		return self.client.service.uploadCACHeartbeatInfo(data)
