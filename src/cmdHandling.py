import os, sys


INFOMESSAGE = """
quit - closes the program
"""


class cmdHandler(object):
	"""
	Handles the users interaction with the shell
	"""
	def __init__(self: object):
		self.uInput: str
		self.breakFlag: bool = False
		self.mainLoopFlag: bool = True

	def getCommand(self: object) -> None:
		while True:
			if (self.breakFlag):
				break
			if (self.mainLoopFlag):
				print()
			self.uInput = input("> ")
			self._commandHandling()
		return None

	def _commandHandling(self: object) -> None:
		self.uInput = self.uInput.lower()
		if (self.uInput == "quit"):
			self.breakFlag = True
		return None

	def _modFileShow(self: object, mods: list[str]) -> None:
		pass
