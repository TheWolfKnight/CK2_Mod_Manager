import os, json
from ck2FileHandling import CK2Handler
from profileHandling import profileHandler


INFOMESSAGE = """Profile - open profile editor\nCommit - Enable a profile\nSettings - Change setting for the program\nquit - closes the program"""


class cmdHandler(object):
	"""
	Handles the users interaction with the shell
	"""
	def __init__(self: object):
		self.fileClassHandler = _modFileSubClass()
		self.commitClassHandler = _commitSubClass()
		self.settingsClassHandler = _settingsSubClass()
		self.profileClassHandler = _profileSubClass()
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
			while True:
				# Profile scope
				self.uInput = input("> ").lower()
				token = self.uInput.split(" ")
				if (self.uInput == "quit"):
					break
				if (token[0] == "create" and token[1] == "profile"):
					self.profileClassHandler.createProfile(token[2])
				elif (token[0] == "edit" and token[1] == "profile"):
					self.profileClassHandler.editProfile(token[2])
				elif (token[0] == "delete" and token[1] == "profile"):
					self.profileClassHandler.deleteProfile(token[2])
				else:
					print("Invalid input")
		elif (self.uInput == "commit"):
			while True:
				# Commit Scope
				self.uInput = input("> ").lower()
				if (self.uInput == "quit"):
					break
		elif (self.uInput == "settings"):
			while True:
				# Settings Scope
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

	def getModFiles(self: object) -> dict[int]:
		res: dict
		files: list[str]
		count = 1
		with open("../bin/initSettings.json", "r") as r:
			data = json.load(r)
			path = data["ck2path"]
		for _, _, file in os.walk(path):
			files = file
		for file in files:
			res[str(count)] = file
			count += 1
		return res


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


class _profileSubClass(object):
	def __init__(self: object):
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
		data  = self.modFileSubClass.getModFiles()
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
			data  = self.modFileSubClass.getModFiles()
			for key in data.keys():
				mod = data[key][:data[key].index('.mod')]
				print(f"{key}: {mod}")
			print("Syntax: add/remove 1, 2, 3")
			uInput = input("Profile >>> ").lower()
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
		return None

	def deleteProfile(self: object, profileName: str) -> None:
		"""
		Handles the deletion of a profile, given by the user\n
		:param self: object\n
		:param profileName: str\n
		:return: None
		"""
		if (self.profileH.deleteProfile(profileName)):
			print(f"{profileName} has been deleted")
		else:
			print(f"failed to delete profile: {profileName}")
		return None
