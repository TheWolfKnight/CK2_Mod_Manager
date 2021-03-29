def printList(elem: list) -> None:
	for item in elem:
		print(f"\t{item}")
	return None

def getData(path: str) -> dict:
	import json
	with open(path, 'r') as r:
		data = json.load(r)
		r.close()
	return data
