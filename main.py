# main.py

def get_book_text(path_to_file):
    file_contents = ""
    
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def word_count(file_contents):
    word_list = []
    word_qty = 0

    word_list = file_contents.split()
    word_qty = len(word_list)

    return word_qty


def main():
    # note to self: relative path does not include the leading forward slash /
    current_book = get_book_text("books/frankenstein.txt")
    book_word_count = word_count(current_book)
    print(f"Found {book_word_count} total words")


main()