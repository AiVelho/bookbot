from utils.common import read_file, count_words, count_character_appearances


def main():
	frankenstein_file_path = "books/frankenstein.txt"
	try:
		frankenstein_text = read_file(frankenstein_file_path)
		word_count = count_words(frankenstein_text)
		character_appearances = count_character_appearances(frankenstein_text)
		print(frankenstein_text)
		print(f"--- Begin report of {frankenstein_file_path} ---")
		print(f"Word count: {word_count}")
		for key, value in character_appearances.items():
			print(f"Character '{key}' was found {value} times")
		print("--- End report ---")
	except Exception as e:
		print(f"Error reading file: {frankenstein_file_path}, {e}")


if __name__ == "__main__":
	main()
