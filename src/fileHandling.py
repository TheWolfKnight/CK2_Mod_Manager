import os, json


BASEFILES_CONST = ["profiles.json", "initSettings.json", "initCK2SettingsBackup.txt"]


class fileHandler(object):
	"""
	Handles the creation and managment of base files, not necessarily their contents
	"""
	def __init__(self: object):
		self.path = self._getModFilePath()
		self.BckUpHandler = _BackupHandler(self.path)

	def baseFileHandler(self: object) -> None:
		"""
		Handles reading and writing for the base file settings\n
		:param self: object\n
		:return: Unknown
		"""
		for file in BASEFILES_CONST:
			if (not os.path.exists(f"../bin/{file}")):
				open(f"../bin/{file}", 'x')
		self._writeBaseData()
		return None

	def findMods(self: object) -> list[str]:
		"""
		Walks trough the CK2 mod folder and findes all .mod files, add them to a list and return them\n
		:param self: object\n
		:return: list[str]
		"""
		res: list = []
		for file in os.listdir(f"{self.path}/mod"):
			if (file.endswith(".mod")):
				res.append(file)
		return res

	def _getModFilePath(self: object) -> str:
		while True:
			print("Path is usually fund in dockuments folder under \"Paradox Interactiv\"")
			uInput = input("Path to CK2 root folder > ")
			isDir = True if os.path.isdir(uInput) else False
			if (isDir):
				return uInput
			else:
				print("Not a valid path")

	def _writeBaseData(self: object) -> None:
		"""
		Writes the base data for the different files\n
		:param self: object\n
		:retun: None
		"""
		for file in BASEFILES_CONST:
			if (file == BASEFILES_CONST[1]):
				self.BckUpHandler._createInitSettings()
			if (file == BASEFILES_CONST[2]):
				self.BckUpHandler._backupBaseSettings()
			if (file == BASEFILES_CONST[0]):
				self.BckUpHandler._profilesInitSettings()
		return None

class _BackupHandler(object):
	"""
	Handles the backup functions for fileHandling
	"""
	def __init__(self: object, ckpath: str):
		self.path: str = ckpath

	def _backupBaseSettings(self: object) -> None:
		"""
		Creates an backup of the actual settings.txt from CK2\n
		:param self: object\n
		:return: None
		"""
		with open(f"../bin/{BASEFILES_CONST[2]}", 'a') as w:
			with open(f"{self.path}/settings.txt", 'r') as r:
				w.write(r.read())
				r.close()
			w.close()
		return None

	def _createInitSettings(self: object) -> None:
		"""
		Creates the initial settings for the program\n
		:param self: object\n
		:return: None
		"""
		with open(f"../bin/{BASEFILES_CONST[1]}", 'w') as w:
			data = {
				"firstRunFlag": True,
				"ck2path": str(self.path)
			}
			json.dump(data, w)
			w.close()
		return None

	def _profilesInitSettings(self: object) -> None:
		"""
		Creates the initial setting for the profiles\n
		:param self: object\n
		:return: None
		"""
		with open(f"../bin/{BASEFILES_CONST[0]}", 'w') as w:
			data = {
				"present": []
			}
			json.dump(data, w)
			w.close()
		return None
