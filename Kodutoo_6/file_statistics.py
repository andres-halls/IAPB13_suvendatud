'''
@name File Statistics Module
@author Andres Liiver

Module processes files and:
1. Counts how many times all words are found
2. ...
... more bleh here
'''

def process_file(file):
    '''
    Returns list of words in a file.
    @arg file - handle to file
    @returns list of words
    '''
    file_contents = file.read()
    words = []
    word = ""
    
    for char in file_contents:
        char = char.lower()
        if char.isalpha():
            word += char
        else:
            if word != "":
                words.append(word)
                word = ""

    if word != "":
        words.append(word)

    return words

def count_words(word_list):
    '''
    Returns a dictionary, where key is the word in word_list
    and the corresponding value is the amount of times it is found.
    '''
    result = {}
    
    for word in word_list:
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1
    
    return result

def find_top_words(dct, n):
    '''
    Returns a dictionary, where key is
    '''
    # TODO
    pass

def print_top_words(dct, file):
    # TODO
    pass
