import os, json, sys
from fileHandling import fileHandler
from profileHandling import profileHandler
from cmdHandling import cmdHandler


def readBaseSettings() -> dict:
	with open("./subFiles/initSettings.json", 'r') as r:
		data = json.load(r.read())
	return data

def setFRF() -> None:
	with open("./subFiles/initSettings.json", 'w') as w:
		with open("./subFiles/initSettings.json", 'r') as r:
			data = json.load(r.read())
			data["firstRunPath"] = False
			r.close()
		json.dump(data, w)
		w.close()
	return None

def onOpne() -> None:
	settings = readBaseSettings()
	if (settings["firstRunFlag"]):
		baseFileHandler = fileHandler(settings["ck2path"])
		baseFileHandler.baseFileHandler()
		setFRF()


def main():
	onOpne()


if __name__ == "__main__":
	main()
	sys.exit()
