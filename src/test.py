import os, sys


def main():
	files: list
	for _, _, file in os.walk("../tmp/"):
		files = file
	for file in files:
		if (file.endswith(".mod")):
			(file.index(".mod"))

if __name__ == "__main__":
	main()
	sys.exit()
