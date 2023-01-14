import os

def getExternalPrograms():
	try:
		extensions = os.listdir("programs")
		extensions.remove("__init__.py")
		return extensions
	except FileNotFoundError:
		return []
