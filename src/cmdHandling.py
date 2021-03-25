import os, json
from ck2FileHandling import CK2Handler
from profileHandling import profileHandler


INFOMESSAGE = """Profile - open profile editor\nCommit - Enable a profile\nquit - closes the program"""


class cmdHandler(object):
	"""
	Handles the users interaction with the shell
	"""
	def __init__(self: object):
		self.fileClassHandler = _modFileSubClass()
		self.commitClassHandler = _commitSubClass()
		self.uInput
		self.breakFlag = False
		self.mainLoopFlag = True

	def getCommand(self: object) -> None:
		"""
		Gets the users command and throws it to the command handler\n
		:param self: object\n
		:return: None
		"""
		while True:
			if (self.breakFlag):
				print("Closing Program")
				break
			print(INFOMESSAGE)
			self.uInput = input("> ").lower()
			self._commandHandling()
		return None

	def _commandHandling(self: object) -> None:
		"""
		parses and handles the commands from getCommand()\n
		:param self: object\n
		:return: None
		"""
		if (self.uInput == "quit"):
			self.breakFlag = True
		elif (self.uInput == "profile"):
			while True:
				self.uInput = input("> ").lower()
				if (self.uInput == "quit"):
					break
		elif (self.uInput == "Commit"):
			while True:
				self.uInput = input("> ").lower()
				if (self.uInput == "quit"):
					break
		else:
			print(f"\"{self.uInput}\" is not a command")
		return None

	def _prfileHandling(self: object) -> None:
		pass


class _modFileSubClass(object):
	"""
	Internal mod handling for cmdHandler, used when listing mods
	"""
	def _modFileShow(self: object, mods: list[str]) -> None:
		"""
		Prints the currently downlaoded mod files from the ck2 path
		:param self: object
		"""
		for mod in mods:
			printStr = mod[:mod.index(".mod")]
			print(f"{printStr}\n")
		return None


class _commitSubClass(object):
	"""
	Internal commitment handler for cmdHandler, used when writing profiles to setting.txt
	"""
	def _parseUserInput(self: object, uInput: str) -> list[str]:
		self.profile = uInput
		pass

	def _getProfileMods(self: object) -> list[str]:
		"""
		Gets the mods from a specific profile\n
		:param self: object\n
		:return: list[str]
		"""
		with open("../bin/profiles.json", 'r') as r:
			data = json.load(r)
			profileMods = data[self.profile]
			r.close()
		return profileMods


class _settingsSubClass(object):
	"""
	Internal settings handler for the cmdHandler, used when changing settings in initSettings.json
	"""
	pass
