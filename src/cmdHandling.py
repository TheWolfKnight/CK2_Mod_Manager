import os, json, misc, sys
from ck2FileHandling import CK2Handler
from profileHandling import profileHandler
from pathlib import Path


INFOMESSAGE = """Profile - open profile editor\nCommit - Enable a profile\nSettings - Change setting for the program\nquit - closes the program"""


class cmdHandler(object):
	"""
	Handles the users interaction with the shell
	"""
	def __init__(self: object, gamePath: str):
		self.fileClassHandler = _modFileSubClass()
		self.commitClassHandler = _commitSubClass(gamePath)
		self.settingsClassHandler = _settingsSubClass()
		self.profileClassHandler = _profileSubClass(gamePath)
		self.uInput: str
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
			print("Create Profile <Name> - Make a new profile\nEdit Profile <Name> - eddit a profile\nDelete Profile <Name> - Deletes a profile\nquit - Goes back")
			while True:
				# Profile scope
				self.uInput = input(">>> ").lower()
				token = self.uInput.split(" ")
				if (self.uInput == "quit"):
					break
				if (token[0] == "create" and token[1] == "profile"):
					self.profileClassHandler.createProfile(token[2])
				elif (token[0] == "edit" and token[1] == "profile"):
					self.profileClassHandler.editProfile(token[2])
				elif (token[0] == "delete" and token[1] == "profile"):
					self.profileClassHandler.deleteProfile(token[2])
				elif (token[0] == "show" and token[1] == "profile"):
					self.profileClassHandler.showProfile()
				else:
					print("Invalid input")
		elif (self.uInput == "commit"):
			while True:
				# Commit Scope
				self.uInput = input("> ").lower()
				token = self.uInput.split(' ')
				if (self.uInput == "quit"):
					break
				elif (token[0] == "commit"):
					self.commitClassHandler.commitProfile(token[1])
				elif (token[0] == "show" and token[1] == "profile"):
					self.profileClassHandler.showProfile()
				else:
					print("Invalid input")
		elif (self.uInput == "settings"):
			while True:
				# Settings Scope
				self.uInput = input("> ").lower()
				token = self.uInput.split(' ')
				if (self.uInput == "quit"):
					break
				elif (token[0] == "show" and token[1] == "settings"):
					self.settingsClassHandler.showSettings()
				elif (token[0] == "change" and token[1] == "settings"):
					self.settingsClassHandler.changeSettings()
				else:
					print("Invalid input")
		else:
			print(f"\"{self.uInput}\" is not a command")
		return None


class _modFileSubClass(object):
	"""
	Internal mod handling for cmdHandler, used when listing mods
	"""
	def modFileShow(self: object, mods: list[str]) -> None:
		"""
		Prints the currently downlaoded mod files from the ck2 path\n
		:param self: object\n
		:return: None
		"""
		for mod in mods:
			if (mod is not None):
				printStr = mod[:mod.index(".mod")]
				print(f"{printStr}")
		return None

	def getModFiles(self: object, path: str) -> dict[int, str]:
		"""
		Gets the mods from the CK2 mod folder\n
		:param path: str\n
		:param self: object\n
		:return: dict[int]
		"""
		res: dict[int, str] = {}
		files: list[str] = []
		count = 1
		for _, _, file in os.walk(f"{path}/mod"):
			files = file
		for file in files:
			if (file.endswith(".mod")):
				res[str(count)] = file
				count += 1
		return res


class _commitSubClass(object):
	"""
	Internal commitment handler for cmdHandler, used when writing profiles to setting.txt
	"""
	def __init__(self: object, gamePath: str):
		self.path = gamePath

	def commitProfile(self: object, profileName: str) -> None:
		"""
		When called, commits the given profile
		:param profileName: str\n
		:param gamePath: str\n
		:param self: object\n
		:return: None
		"""
		mods = self._getProfileMods(profileName)
		self.CK2Object = CK2Handler(self.path, mods)
		self.CK2Object.writeProfile()

	def _getProfileMods(self: object, profileName: str) -> list[str]:
		"""
		Gets the mods from a specific profile\n
		:param self: object\n
		:return: list[str]
		"""
		data = misc.getData("../bin/profiles.json")
		return data[profileName]


class _settingsSubClass(object):
	"""
	Internal settings handler for the cmdHandler, used when changing settings in initSettings.json
	"""
	def showSettings(self: object) -> None:
		"""
		Prints the list of settings\n
		:param self: object\n
		:return: None
		"""
		data = misc.getData("../bin/initSettings.json")
		for key in data.keys():
			print(f"{key}: {data[key]}")
		return None

	def changeSettings(self: object) -> None:
		"""
		Changes a given setting\n
		:param self: object\n
		:return: None
		"""
		data = misc.getData("../bin/initSettings.json")
		uInput = input("Settings >>> ").lower()
		token = uInput.split(' ')
		try:
			key = data.keys()[data.keys().index(token[0])]
			data[key] = token[1]
		except ValueError:
			print("No setting by that name")
		print("Setting changed")
		return None


class _profileSubClass(object):
	def __init__(self: object, gamePath: str):
		self.path = "../bin/profiles.json"
		self.gamePath = gamePath
		self.profileH = profileHandler()
		self.modFileSubClass = _modFileSubClass()

	def createProfile(self: object, profileName: str) -> None:
		"""
		Creates a new profile from the given user input\n
		:param self: object\n
		:param profileName: str\n
		:return: None
		"""
		res: list[str] = []
		data  = self.modFileSubClass.getModFiles(self.gamePath)
		for key in data.keys():
			mod = data[key][:data[key].index('.mod')]
			print(f"{key}: {mod}")
		print("select wanted mod, format: 1, 2, 3")
		selectedMods = input("Profile >>> ").strip().split(',')
		for mod in selectedMods:
			res.append(data[mod])
		self.profileH.createProfile(profileName, res)
		return None

	def editProfile(self: object, profileName: str) -> None:
		"""
		Enables the user to edit the profile, by trapping in a new while True loop\n
		:param self: object\n
		:param profileName: str\n
		:return: None
		"""
		while True:
			res: list[str] = []
			data  = self.modFileSubClass.getModFiles(self.path)
			for key in data.keys():
				mod = data[key][:data[key].index('.mod')]
				print(f"{key}: {mod}")
			print("Syntax: add/remove 1, 2, 3")
			uInput = input("Profile >>> ").lower()
			try:
				if (uInput == "quit"):
					break
				elif (uInput == "add"):
					selectedmods = uInput.remove(2).strip().split(',')
					for mod in selectedmods:
						res.append(mod)
					self.profileH.editProfile(profileName, add=selectedmods)
					res = []
				elif (uInput == "remove"):
					selectedmods = uInput.remove(2).strip().split(',')
					for mod in selectedmods:
						res.append(mod)
					self.profileH.editProfile(profileName, remove=selectedmods)
					res = []
				else:
					print("Invalid input")
			except self.profileH.InvalidProfileError as e:
				print(e.asString())
		return None

	def deleteProfile(self: object, profileName: str) -> None:
		"""
		Handles the deletion of a profile, given by the user\n
		:param self: object\n
		:param profileName: str\n
		:return: None
		"""
		try:
			self.profileH.deleteProfile(profileName)
			print(f"{profileName} has been deleted")
		except self.profileH.InvalidProfileError as e:
			print(e.asString())
		return None

	def showProfile(self: object) -> None:
		"""
		Showes all the available profiles\n
		:param self: object\n
		:return: None
		"""
		data = misc.getData("../bin/profile.json")
		keys = data["present"]
		for key in keys:
			print(key)
			misc.printList(data[key])
		return None
