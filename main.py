# main.py
import sys
from stats import get_num_words, get_letter_count, sort_dictionary


def get_book_text(path_to_file):
    file_contents = ""
    
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def get_report(book_word_count, sorted_letter_count, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for letter in sorted_letter_count:
        print(f"{letter}: {sorted_letter_count[letter]}")
    print("============= END ===============")
    


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    # note to self: relative path does not include the leading forward slash /
    #current_book = get_book_text("books/frankenstein.txt")
    current_book = get_book_text(book_path)
    book_word_count = get_num_words(current_book)
    book_letter_count = get_letter_count(current_book)
    sorted_letter_count = sort_dictionary(book_letter_count)
    print_report = get_report(book_word_count, sorted_letter_count, book_path)
    return print_report


main()