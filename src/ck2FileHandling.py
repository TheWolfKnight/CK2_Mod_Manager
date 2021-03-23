import os, sys, json

class CK2Handler(object):
	def __init__(self: object, ck2path: str, mods: list[str]):
		self.ck2path: str = ck2path
		self.mods: list[str] = mods

	def _mkTempBinFile(self:object) -> None:
		open("../bin/tempSettings.txt", 'x')
		return None

	def _rmTempBinFile(self: object) -> None:
		os.remove("../bin/tempSettings.txt")
		return None

	def _createModString(self: object) -> str:
		res = "{\n\t"
		for mod in self.mods:
			if (mod != self.mods[-1]):
				res += mod+" "
			else:
				res += mod+"\n"
		res += "}"
		return res

	def _writeTemp(self: object) -> None:
		modLine: int = None
		count: int = 0
		with open("../bin/tempSettings.txt", 'a') as w:
			with open(f"{self.ck2path}/settings.txt") as r:
				for line in r.readlines():
					if (modLine is not None):
						if (count <= modLine+3):
							count += 1
							continue
					if (line == "last_mods="):
						w.write(line)
						modLine = self._createModString()
						w.write(modLine)
						modLine = count
						count += 1
						continue
					else:
						w.write(line)
						count += 1
						continue
		return None

	def writeProfile(self: object) -> None:
		return None
