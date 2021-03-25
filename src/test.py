import os, sys
from cmdHandling import _modFileSubClass
from fileHandling import fileHandler

def main():
	fHandler = fileHandler(r"C:\Users\sys_admin\Documents\Paradox Interactive\Crusader Kings II")
	cHandler = _modFileSubClass()

	l_str = fHandler.findMods()
	cHandler._modFileShow(l_str)


if __name__ == "__main__":
	main()
	sys.exit()
