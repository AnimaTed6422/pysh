try:
	import internal
	import external
	import importlib
	import os
	from json import loads
except ModuleNotFoundError as e:
	print("Error: The required files could not be loaded. Ensure " + str(e.name) + " is a proper module or file in the current directory")
	exit(1)

def parseCommand(command, args):
	if("fn_" + command in dir(internal)):
		program = getattr(internal, "fn_" + command)
		# exec("output = internal.fn_" + command + "(args)")
		output = program(args)
		if(output == 1): print("Program exited with exit code 1")
	elif(command + ".py" in external.getExternalPrograms()):
		try:
			program = importlib.import_module("programs." + command)
			try:
				output = program.run(args)
			except AttributeError:
				print("Invalid Program \"{}\"".format(command))
				return None
			if(output): print("Program exited with exit code 1")
		except ImportError:
			print("Unable to acquire program")
	elif(internal.isInFolder(command, "scripts")):
		with open("scripts/" + command) as fh:
			for line in fh.readlines():
				args = line.split(" ")
				cmd = args.pop(0).replace("\n", "")
				parseCommand(cmd, args)
	else:
		print(command + " is not recognized as a operable program or internal command")

ver = loads(internal.readFile("meta.json"))["version"]

print("PySh " + str(ver))

while(True):
	command = input("$ ")
	args = command.split(" ")
	command = args.pop(0)
	parseCommand(command, args)
