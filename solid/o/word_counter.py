# def count_word_occurrences(word, localfile):
#     content = open(localfile, "r").read()
#     counter = 0
#     for e in content.split():
#         if word.lower() == e.lower():
#             counter += 1
#     return counter


def read_localfile(file):
    '''Read file'''
    return open(file, "r").read()


def count_word_occurrences(word, content):
    '''Count number of word occurrences in a file'''
    counter = 0
    for e in content.split():
        if word.lower() == e.lower():
            counter += 1
    return counter








