import sys
import clipboard
import json

def save_items(filepath, data):
	with open(filepath, 'w') as f:
		json.dump(data, f)

def load_items(filepath):
	try:
		with open(filepath, 'r') as f:
			data = json.load(f)
			return data
	except FileNotFoundError:
		return {}

FILEPATH = 'clipboard.json'

def main():
	data = load_items(FILEPATH)
	if len(sys.argv) == 2:
		command = sys.argv[1]
	if len(sys.argv) == 1:
		print("No command given, usage: python main.py save | load | list")
	if len(sys.argv) > 2:
		print("Too many arguments, usage: python main.py save | load | list")

	if command == "save":
		key = input("Enter a key:")
		data[key] = clipboard.paste()
		save_items(FILEPATH,data)
		print("Clipboard saved!")
	if command == "load":
		key = input("Enter a key:")
		if key in data:
			clipboard.copy(data[key])
			print("Copied to clipboard!")
	if command == "list":
		for key in data:
			print(f"{key}: {data[key]}")

if __name__ == '__main__':
	main()

