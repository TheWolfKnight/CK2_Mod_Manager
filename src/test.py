import sys

def main():
	test: list[int] = []
	for i in range(10):
		test.append(i)
	print(test)
	test = []
	print(test)


if __name__ == "__main__":
	main()
	sys.exit()
