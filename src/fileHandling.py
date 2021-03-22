import os, sys, json
import main

class fileHandler(object):
	"""
	Handles the creation and managment of base files, not necessarily their contents
	"""
	def baseFileHandler(self: object) -> None:
		"""
		Handles reading and writing for the base file settings\n
		:param self: object\n
		:return: Unknown
		"""
		for file in main.BASEFILES_CONST:
			if (not os.path.exists(f"./subFiles/{file}")):
				open(f"{file}", 'x')

	def writeBaseData(self: object) -> None:
		"""
		Writes the base data for the different files\n
		:param self: object\n
		:retun: None
		"""
		for file in main.BASEFILES_CONST:
			if (file is "initSetting.json"):
				break
			if (file is "initCK2SettingsBackup.txt"):
				break

	def findMods(self: object) -> list[str]:
		"""
		Walks trough the CK2 mod folder and findes all .mod files, add them to a list and return them\n
		:param self: object\n
		:return: list
		"""
		res = []
		for _, _,file in os.walk(f"{main.CK2PATH_CONST}/mod"):
			if (file.endswith('.mod')):
				res.append(file)
		return res
