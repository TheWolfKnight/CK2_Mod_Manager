import sys, json
from fileHandling import fileHandler

def main():
	handler = fileHandler("%UserProfile%/Documents/Paradox Interactive/Crusader Kings II")
	print(handler.findMods())

if __name__ == "__main__":
	main()
	sys.exit()
