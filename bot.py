# Import some necessary libraries.
import socket, re
from commands import Bot


class Construct(object):
	
	def __init__(self):
		# Some basic variables used to configure the bot
		self.server  = "irc.freenode.net"
		self.channel = "#sadmicrowave"
		self.port	 = 6667
		self.nick 	 = "sadbot1" # Your bots nick
		self.email 	 = "sadmicrowave@gmail.com"
		self.pwd 	 = "Ic@Rus2010"
		self.ircsock = None
	
	def _construct(self):
		"""Construct the socket connection to the remote server."""
		# Perform the standard socket connect commands
		self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	def _connect(self):
		self.ircsock.connect((self.server, self.port))

	def _configure(self):
		"""Set any extra specs for the connection object."""
		#self.ircsock.setblocking(0)

	def _signin(self):
		"""Perform the freenode connection handshake to register and identify the bot."""
		self.push("NICK %s\n" % self.nick) # here we actually assign the nick to the bot
		self.push("USER %s %s %s %s\n" % (self.nick,self.nick,self.nick,self.nick)) # user authentication
		self.push("NS register %s %s\n" % (self.pwd, self.email)) # here we actually assign the nick to the bot
		# here we join the channel
		self.join(self.channel)
	
	def push(self, msg):
		"""Send the expressed command/msg to the remote server we are connected to."""
		self.ircsock.send(msg.encode())
	
	# This function is used to join channels.
	def join(self, channel):
		self.push("JOIN %s\n" % channel)





if __name__ == "__main__":
	try:
		c = Construct()
		c._construct()
		c._connect()
		c._configure()
		c._signin()
		
		Bot.ircsock = c.ircsock	
		Bot.channel = c.channel
	
		while 1: # Be careful with these! It might send you to an infinite loop
			ircmsg = Bot.ircsock.recv(2048).decode().strip('\n\r') # receive data from the server
			#ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
			print(ircmsg) # Here we print what's coming from the server
		
			command	 = Bot.get_command(ircmsg)
			
			if command and command[0].lower() == c.nick and len(command) == 2:
				Bot.sendnick = Bot.get_user(ircmsg)	
				ex   = command[1].split(' ',1)
				args = ''
				
				if hasattr(Bot, ex[0]):
					if len(ex) == 2:
						args = ex[1]
					
					print( ex )
					
					eval("Bot.%s(%s)" % (ex[0], args))
			
			#if ":HELLO %s" % c.nick.upper() in ircmsg.upper(): # If we can find "Hello Mybot" it will call the function hello()
			#	Bot.hello(senduser)
			
			
				
	except Exception as e:
		raise e
		
		
		
		
		