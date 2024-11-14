def read_file(file_path: str) -> str:
	try:
		with open(file_path) as f:
			return f.read()
	except FileNotFoundError:
		raise FileNotFoundError(f"File not found: {file_path}")
	except Exception as e:
		raise Exception(f"Error reading file: {file_path}, {e}")


def count_words(text: str) -> int:
	return len(text.split())


def count_character_appearances(text: str) -> "dict[str, int]":
	char_list = list(text.lower())
	unique_characters = set(char_list)
	char_count_dict = {character: 0 for character in unique_characters}
	for char in char_list:
		char_count_dict[char] += 1
	return dict(sorted(char_count_dict.items(), key=lambda x: -x[1]))
