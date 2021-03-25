import os, json


class profileHandler(object):
	"""
	Manages the different mod profiles
	"""
	def createProfile(self: object, profileName: str, mods: list[str]) -> None:
		"""
		Creates a new profile in profiles.json\n
		:param profileName: str, is the name of the new profile\n
		:param mods: list[str], list of mods for the new profile\n
		:return: None
		"""
		with open("../bin/profiles.json", 'r') as jFile:
			data: dict = json.load(jFile)
			jFile.close()

		with open("../bin/profiles.json", 'w') as jFile:
			if (profileName in data["present"]):
				print("Already a profile by that name, could not create a new profile")
				json.dump(data, jFile)
				jFile.close()
			else:
				data["present"].append(profileName)
				data[profileName] = mods
				json.dump(data, jFile)
				jFile.close()
		return None

	def editProfile(self: object, profileName: str, add: list[str] = None, remove: list[str] = None) -> None:
		"""
		Edits the profile by adding or removing mods\n
		:param profileName: str, name of the profile to edit\n
		:param add (optional): list[str], mods to add to the profile\n
		:param remove (optional): list[str], mods to remove from profile\n
		:return: None
		"""
		with open("../bin/profiles.json", 'r') as jFile:
			data: dict = json.load(jFile)
			jFile.close()

		with open("../bin/profiles.json", 'w') as jFile:
			if (remove):
				for item in data[profileName]:
					if (item in remove):
						data[profileName].remove(item)
			if (add):
				for mod in add:
					try:
						data[profileName].index(mod)
						continue
					except ValueError:
						data[profileName].append(mod)
			json.dump(data, jFile)
			jFile.close()
		return None

	def deleteProfile(self: object, profileName: str) -> None:
		"""
		Deletes a profile from the profiles.json file\n
		:param profileName: str, the name of the profile to be deleted\n
		:return: None
		"""
		res = {}
		with open("../bin/profiles.json", 'r') as jFile:
			data = json.load(jFile)
			jFile.close()

		try:
			data["present"].index(profileName)
		except ValueError:
			print("No profile by that name")
			return None

		with open("../bin/profiles.json", 'w') as jFile:
			keys = list(data.keys())
			keys.remove(profileName)
			for key in keys:
				res[key] = data[key]
			res["present"].remove(profileName)
			json.dump(res, jFile)
			jFile.close()
		return None
