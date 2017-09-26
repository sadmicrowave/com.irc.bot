import re, datetime

class Bot(object):
	ircsock  = None
	sendnick = None
	channel	 = None
	
	@classmethod
	def push(cls,msg):
		"""Send the expressed command/msg to the remote server we are connected to."""
		print( msg )
		cls.ircsock.send(str(msg).encode())
		
	@classmethod
	def get_user(cls, msg):
		"""Get the sending user from the msg string."""
		results = re.search('^:(.*)!', msg)
		return results.group(1) if results else None
	
	@classmethod
	def get_command(cls, msg):
		r = re.compile(" :.*").findall(msg)
		if r:
			return r[0][2:].split(' ',1)
		else:
			return None
				
	@classmethod
	def private(cls, msg): 
		cls.push("PRIVMSG %s %s\n" % (cls.sendnick, msg))
	
	@classmethod
	def public(cls, msg):
		cls.push("/MSG %s %s" % (cls.channel, msg))
	
	# ------------------- COMMANDS ------------------ #
	
	@classmethod
	def hello(cls):
		cls.private("Hello!")
	
	@classmethod
	def time(cls):
		cls.public(datetime.datetime.now())