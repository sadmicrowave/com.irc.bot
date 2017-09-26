from bot2 import Bot

class Hello(Bot):
	def __init__(self):
		super().__init__()
		
		print( self )
	
	def __str__(self):
		return self.getserv()
	