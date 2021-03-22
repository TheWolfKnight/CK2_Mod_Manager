import os, json, sys
from fileHandling import fileHandler
from profileHandling import profileHandler
from cmdHandling import cmdHandler


BASEFILES_CONST = ["profiles.json", "initSettings.json", "initCK2SettingsBackup.txt"]
CK2PATH_CONST = "%UserProfile%/Documents/Paradox Interactive/Crusader Kings II"


def onOpne() -> None:
	baseFileHandler = fileHandler()
	baseFileHandler.baseFileHandler()
	baseFileHandler.writeBaseData()


def main():
	onOpne()


if __name__ == "__main__":
	main()
	sys.exit()
