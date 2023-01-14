def startRemove(arr, string):
	newArr = []
	for i in arr:
		if(i.startswith(string)):
			newArr.append(i.replace(string, ""))
	return newArr

def endRemove(arr, string):
	newArr = []
	for i in arr:
		if(i.endswith(string)):
			newArr.append(i.replace(string, ""))
	return newArr

def readFile(filename):
	fh = open(filename)
	out = ""
	for line in fh.readlines():
		out += line + "\n"
	fh.close()
	return out

def fn_echo(args):
	print(" ".join(args))
	return 0

def fn_echo_(args):
	print("\n")
	return 0

def fn_mkdir(args):
	from os import mkdir as mk
	if(len(args) == 0): return 1
	mk(args[0])
	return 0

def fn_exit(args):
	from sys import exit
	exit(0)

def fn_cd(args):
	if(len(args) == 0):
		from os import curdir, path
		print(path.abspath(curdir))
	else:
		from os import chdir
		chdir(args[0])

def fn_cls(args):
	from console import clear
	clear()

def fn_ls(args):
	from os import listdir, curdir
	if(len(args) == 0):
		print(", ".join(listdir(curdir)))
	else:
		print(", ".join(listdir(args[0])))

def fn_help(args):
	import internal
	print("Internal Commands:")
	print("\n".join(startRemove(dir(internal), "fn_")))
	from external import getExternalPrograms
	items = getExternalPrograms()
	if(len(items) != 0):
		print("\nExternal Programs:")
		print("\n".join(endRemove(items, ".py")))

def fn_cat(args):
	if(len(args) < 1): return 1
	print(readFile(args[0]))
	return 0

def fn_curl(args):
	if(len(args) < 1): return 1
	from urllib.request import urlopen as fetch
	r = fetch(args[0])
	print(r.read())

def isInFolder(file, folder):
	from os import listdir
	try:
		if(file in listdir(folder)): return True
		else: return False
	except FileNotFoundError:
		return False
