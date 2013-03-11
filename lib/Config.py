'''
Created on 2013-3-8

@author: Moxiaoyong
'''

class Config(object):
	'''
	classdocs
	'''

	def __init__(self,type):
		'''
		Constructor
		'''
		if type == 'client':
			#client
			self.SrvIP = None
			self.SrvPort = None
		elif type == 'service':
			#service
			self.CtrlIP = None
			self.CtrlPort = None
			self.CltIP = None
			self.CltPort = None

#===============================================================================
# log
#===============================================================================

PRINT_LOG = True

PRINT_RUNLOG = True

PRINT_PERFORMANCELOG = True

#===============================================================================
# program parameter
#===============================================================================

Status = 'debug'