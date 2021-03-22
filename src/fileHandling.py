import os, sys, json


BASEFILES_CONST = ["profiles.json", "initSettings.json", "initCK2SettingsBackup.txt"]


class fileHandler(object):
	"""
	Handles the creation and managment of base files, not necessarily their contents
	"""
	def __init__(self: object, path: str):
		self.path = path

	def baseFileHandler(self: object) -> None:
		"""
		Handles reading and writing for the base file settings\n
		:param self: object\n
		:return: Unknown
		"""
		for file in BASEFILES_CONST:
			if (not os.path.exists(f"./subFiles/{file}")):
				open(f"./subFiles/{file}", 'x')
		self._writeBaseData()
		return None

	def _writeBaseData(self: object) -> None:
		"""
		Writes the base data for the different files\n
		:param self: object\n
		:retun: None
		"""
		for file in BASEFILES_CONST:
			if (file == "initSetting.json"):
				self._createInitSettings()
			if (file == "initCK2SettingsBackup.txt"):
				self._backupBaseSettings()
		return None

	def findMods(self: object) -> list[str]:
		"""
		Walks trough the CK2 mod folder and findes all .mod files, add them to a list and return them\n
		:param self: object\n
		:return: list
		"""
		res = []
		for _, _,file in os.walk(f"{self.path}/mod"):
			if (file.endswith('.mod')):
				res.append(file)
		return res

	def _backupBaseSettings(self: object) -> None:
		"""
		Creates an backup of the actual settings.txt from CK2\n
		:param self: object\n
		:return: None
		"""
		with open(f"./subFiles/{BASEFILES_CONST[3]}", 'a') as w:
			with open(f"{self.path}/settings.txt", 'r') as r:
				w.write(r.read())
				r.close()
			w.closed()
		return None

	def _createInitSettings(self: object) -> None:
		"""
		Creates the initial settings for the program\n
		:param self: object\n
		:return: None
		"""
		with open(f"./subFiles/{BASEFILES_CONST[2]}", 'w') as jFile:
			data = {
				"firtRunFlag": False,
				"ck2path": "%UserProfile%/Documents/Paradox Interactive/Crusader Kings II"
			}
			json.dump(data, jFile)
			jFile.close()
		return None
