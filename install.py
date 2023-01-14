import requests
import base64
import os
print("Installing PySh...")

os.mkdir("pysh")

contentURL = "https://api.github.com/repos/AnimaTed6422/pysh/contents/"

files = ["__init__.py", "external.py", "internal.py", "meta.json", "shell.py"]

for file in files:
    with open("pysh/" + file, 'w') as fh:
        fh.write(base64.b64decode(requests.get(contentURL + file).json()["content"]).decode())
    print("- {}".format(file))

for folder in ["programs", "scripts"]:
    os.mkdir("pysh/" + folder)
    print("- {}".format(folder))

print("Successfully installed PySh")