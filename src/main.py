import os, json, sys, misc
from fileHandling import fileHandler
from cmdHandling import cmdHandler


CK2PATH: str = None


def readBaseSettings() -> (dict, bool):
	if (os.path.isfile("../bin/initSettings.json")):
		with open("../bin/initSettings.json", 'r') as r:
			data: dict = json.load(r)
			r.close()
		return data, True
	else:
		return None, False

def setFRF() -> None:
	data = misc.getData("../bin/initSettings.json")
	data["firstRunFlag"] = False
	with open("../bin/initSettings.json", 'w') as w:
		json.dump(data, w)
		w.close()
	return None

def onOpen() -> None:
	global CK2PATH
	settings, initPressent = readBaseSettings()
	if ((settings is None) or not settings["firstRunFlag"] or not initPressent):
		baseFileHandler = fileHandler("../tmp")
		baseFileHandler.baseFileHandler()
		CK2PATH = "../tmp"
		setFRF()
		return None
	else:
		CK2PATH = settings["ck2path"]
		return None

def main() -> None:
	onOpen()
	cmd = cmdHandler(CK2PATH)
	cmd.getCommand()
	return None


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Shutting down")
	except EOFError:
		print("Shutting down")
	sys.exit()
