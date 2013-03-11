'''
Created on 2013-3-8

@author: Moxiaoyong
'''

import socket, threading

from config import CltConfig

if __name__ == '__main__':
	srvSock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	srvSock.connect( ( CltConfig.SrvIP, CltConfig.SrvPort ) )