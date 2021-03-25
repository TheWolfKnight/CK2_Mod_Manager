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
		self.uInput: str
		self.breakFlag: bool = False
		self.mainLoopFlag: bool = True

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
			if (self.mainLoopFlag):
				print(INFOMESSAGE)
			self.uInput = input("> ")
			self._commandHandling()
		return None

	def _commandHandling(self: object) -> None:
		"""
		parses and handles the commands from getCommand()\n
		:param self: object\n
		:return: None
		"""
		self.uInput = self.uInput.lower()
		if (self.uInput == "quit"):
			self.breakFlag = True
		elif (self.uInput == "profile"):
			pass
		elif (self.uInput == "Commit"):
			pass
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
		pass


class _commitSubClass(object):
	"""
	Internal commitment handler for cmdHandler, used when writing profiles to setting.txt
	"""
	def _parseUserInput(self: object, uInput: str) -> list[str]:
		self.profile: str
		pass

	def _getProfileMods(self: object):
		with open("../bin/profiles.json", 'r') as r:
			data: dict = json.load(r)
			profile = data[self.profile]
			pass


class _settingsSubClass(object):
	pass
