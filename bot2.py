# Import some necessary libraries.
import socket, re
import commands2

class Bot(object):
	def __init__(self):
		self.server  = "irc.freenode.net"
			
	def getserv(self):
		return self.server
		

if __name__ == "__main__":
	commands2.Hello()
		
		
		