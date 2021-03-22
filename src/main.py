import os, json, sys
from fileHandling import fileHandling
from profileHandling import profileHandling
from cmdHandling import cmdHandling


BASEFILES_CONST = ["profiles.json", "initSettings.json", "initCK2SettingsBackup.txt"]
CK2PATH_CONST = "%UserProfile%/Documents/Paradox Interactive/Crusader Kings II"


def onOpne():
	fileHandler = fileHandling()
	fileHandler.baseFileHandler()
	fileHandler.writeBaseData()


def main():
	onOpne()


if __name__ == "__main__":
	main()
	sys.exit()
