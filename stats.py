# stats.py


def get_num_words(file_contents):
    word_list = []
    word_qty = 0

    word_list = file_contents.split()
    word_qty = len(word_list)

    return word_qty


def get_letter_count(file_contents):
    letter_dictionary = {}
    letters_list = list(file_contents.lower())
    for letter in letters_list:
        if letter not in letter_dictionary:
            letter_dictionary[letter] = 1
        else:
            letter_dictionary[letter] += 1
    return letter_dictionary