import sys
from OSC import OSCClient, OSCMessage
from EOS import eosClient


eos = eosClient()

if len(sys.argv)==4 or 5:
	try:
		eos.connectToConsole(str(sys.argv[2]),int(sys.argv[3]),"nomad")
	except:
		print "ERR CONN"
		sys.exit("Problem connecting, or you didn't specify the right things")


if str(sys.argv[1])=="go":
	eos.go()
elif str(sys.argv[1])=="stopback":
	eos.stopback()
elif str(sys.argv[1])=="chanlevel":
	if ':' in str(sys.argv[4]):
		print "yes"
		s = str(sys.argv[4])
		cmdarray = s.split(':')
		try:
			eos.chanlevel(str(cmdarray[0]),int(cmdarray[1]))
		except:
			print "Whoops"
	else:
		print "Something went wrong"
elif str(sys.argv[1])=="cmdline":
	eos.cmdline(str(sys.argv[4]))
elif str(sys.argv[1])=="newcmdline":
	eos.newcmdline(str(sys.argv[4]))
elif str(sys.argv[1])=="cmdlineevent":
	eos.cmdlineevent(str(sys.argv[4]))
elif str(sys.argv[1])=="cmdlinenewevent":
	eos.cmdlinenewevent(str(sys.argv[4]))
else:
	print "No command or invalid command specified"