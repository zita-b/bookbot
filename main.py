book_path = "books/frankenstein.txt"

def main():
  text = get_book_text(book_path)
  report = print_report(book_path, text)

def get_book_text(path):
  with open(book_path) as f:
    return f.read()

def num_words(text):
  return len(text.split())

def char_count(text):
  lowercase_text = text.lower()
  chars = [*lowercase_text]
  char_dict = {}

  for char in chars:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1

  return char_dict

def print_report(path, text):
  words_total = num_words(text)
  character_count = char_count(text)
  char_list = []
  for char in character_count:
    if char.isalpha():
      char_list.append(char)
  char_list.sort()

  print(f"--- Begin report of {path} ---")
  print(f"{words_total} words found in the document\n")
  for char in char_list:
    print(f"The {char} character was found {character_count[char]} times")
  print("--- End report ---")


main()
