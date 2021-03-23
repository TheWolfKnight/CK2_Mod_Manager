import os, json, sys
from fileHandling import fileHandler
from cmdHandling import cmdHandler


CK2PATH: str


def readBaseSettings() -> dict and bool:
	if (os.path.isfile("../bin/initSettings.json")):
		with open("../bin/initSettings.json", 'r') as r:
			data: dict = json.load(r.read())
			r.close()
		return data, True
	else:
		return None, False

def setFRF() -> None:
	with open("../bin/initSettings.json", 'w') as w:
		with open("../bin/initSettings.json", 'r') as r:
			data = json.load(r.read())
			data["firstRunPath"] = False
			r.close()
		json.dump(data, w)
		w.close()
	return None

def onOpne() -> None:
	settings, initPressent = readBaseSettings()
	if ((settings is None) or not settings["firstRunFlag"] or not initPressent):
		CK2PATH = settings["ck2path"]
		baseFileHandler = fileHandler(CK2PATH)
		baseFileHandler.baseFileHandler()
		setFRF()
		return None
	else:
		CK2PATH = settings["ck2path"]
		return None

def main() -> None:
	# onOpne()
	cmd = cmdHandler()
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
