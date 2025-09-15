from stats import get_num_words, character_count, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    word_count = get_num_words(book)
    char_dict = character_count(book)
    sorted_count = sort_dict(char_dict)
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for e in sorted_count:
        print(f"{e["char"]}: {e["num"]}")
    print("============= END ===============")
main()