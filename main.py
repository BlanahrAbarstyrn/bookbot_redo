# main.py
from stats import get_num_words


def get_book_text(path_to_file):
    file_contents = ""
    
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    # note to self: relative path does not include the leading forward slash /
    current_book = get_book_text("books/frankenstein.txt")
    book_word_count = get_num_words(current_book)
    print(f"Found {book_word_count} total words")


main()