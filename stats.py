# stats.py


def get_num_words(file_contents):
    word_list = []
    word_qty = 0

    word_list = file_contents.split()
    word_qty = len(word_list)

    return word_qty