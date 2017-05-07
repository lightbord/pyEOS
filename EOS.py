import sys

from OSC import OSCClient, OSCMessage

client_connected = False
client = OSCClient()
console_type = 0

class eosClient():

	def setConsoleType(self,argument):
	 	global console_type
	 	if argument=="ti":
	 		console_type=1
	 	elif argument=="gio":
	 		console_type=2
 		elif argument=="ion":
 			console_type=3
		elif argument=="element":
			console_type=4
		elif argument=="nomad":
			console_type=5
		elif argument=="other":
			console_type=6
		elif argument=="eosclassic":
			console_type=7
		else:
			console_type=6

	def connectToConsole(self,consoleAddress,consolePortRx,consoleType):
		client.connect( (consoleAddress, consolePortRx) )
		self.setConsoleType(consoleType)
		global client_connected
		client_connected = True

	def go(self):
		if client_connected == True:
			client.send( OSCMessage("/eos/key/go") )
			return 1
		else:
			raise ValueError("Not connected")
			return 0

	def stopback(self):
		if client_connected==1:
			client.send( OSCMessage("/eos/key/stop") )
			return 1
		else:
			raise ValueError("Not connected")
			return 0

	def chanlevel(self,channel,level):
		if client_connected==1:
			client.send( OSCMessage("/eos/chan/%s/at" % (channel), [level] ) )
			return 1
		else:
			raise ValueError("Not connected")
			return 0

	def cmdline(self,commandline):
		if client_connected==1:
			client.send( OSCMessage("/eos/cmd", [commandline] ) )
			return 1
		else:
			raise ValueError("Not connected")
			return 0

	def newcmdline(self,commandline):
		if client_connected==1:
			client.send( OSCMessage("/eos/newcmd", [commandline] ) )
			return 1
		else:
			raise ValueError("Not connected")
			return 0

	def cmdlineevent(self,commandline):
		if client_connected==1:
			client.send( OSCMessage("/eos/event", [commandline] ) )
			return 1
		else:
			raise ValueError("Not connected")
			return 0

	def cmdlinenewevent(self,commandline):
		if client_connected==1:
			client.send( OSCMessage("/eos/newevent", [commandline] ) )
			return 1
		else:
			raise ValueError("Not connected")
			return 0