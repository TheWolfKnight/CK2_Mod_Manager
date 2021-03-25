import os, json


class CK2Handler(object):
	"""
	Handles the writing to CK2's settings.txt
	"""
	def __init__(self: object, ck2path: str, mods: list[str]):
		self.path: str = ck2path
		self.mods: list[str] = mods
		self._mkTempBinFile()

	def _mkTempBinFile(self:object) -> None:
		open("../bin/tempSettings.txt", 'x')
		return None

	def _rmTempBinFile(self: object) -> None:
		os.remove("../bin/tempSettings.txt")
		return None

	def _createModString(self: object) -> str:
		res: str = "{\n\t"
		for mod in self.mods:
			if (mod != self.mods[-1]):
				res += f"\"mod/{mod}\" "
			else:
				res += f"\"mod/{mod}\"\n"
		res += "}\n"
		return res

	def _writeTemp(self: object) -> None:
		modLine: int = None
		count: int = 0
		with open("../bin/tempSettings.txt", 'a') as w:
			with open(f"{self.path}/settings.txt", 'r') as r:
				for line in r.readlines():
					if (modLine is not None):
						if (count <= modLine+3):
							print("skip")
							count += 1
							continue
					if (line == "last_mods=\n"):
						print("last_mods reached")
						w.write(line)
						modLine = self._createModString()
						w.write(modLine)
						modLine = count
						count += 1
						continue
					else:
						print("write normal line")
						w.write(line)
						count += 1
						continue
				r.close()
			w.close()
		return None

	def writeProfile(self: object) -> None:
		self._writeTemp()
		with open(f"{self.path}/settings.txt", 'w') as w:
			with open("../bin/tempSettings.txt", 'r') as r:
				w.write(r.read())
				r.close()
			w.close()
		self._rmTempBinFile()
		return None
