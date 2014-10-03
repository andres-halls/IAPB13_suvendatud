'''
@name File Statistics Module
@author Andres Liiver

Module consists of 4 public methods:
1. process_file
2. count_words
3. find_top_words
4. print_top_words
'''

class InvalidInputException(Exception):
    pass

def process_file(file):
    '''
    Returns list of words in a file.

    Arguments:
        file - handle to file
    
    Returns:
        list of words
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
    and the corresponding value is the frequency of the word.

    Arguments:
        word_list - list of words

    Returns:
        dictionary
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
    Returns a dictionary, where key is the length of the word
    and the corresponding value is a dictionary where keys are the n most frequent words
    and the corresponding value is the frequency of the word.

    Arguments:
        dct - dictionary returned by count_words function
        n - integer of how many top words to display

    Returns:
        dictionary

    Raises:
        InvalidInputException: if n < 1
    '''
    if n < 1:
        raise InvalidInputException("find_top_words: n cannot be less than 1")

    result = {}

    for word in dct.keys():
        word_length = len(word)

        if word_length in result.keys():
            if len(result[word_length]) < n:
                result[word_length][word] = dct[word]
        else:
            result[word_length] = {word : dct[word]}

    return result

def print_top_words(dct, file):
    '''
    Writes the dictionary returned by find_top_words to a file as a table.

    Arguments:
        dct - dictionary returned by find_top_words function
        file - handle of file to write to

    Returns:
        no return value
    '''
    file.write("| length |       word       | count |\n")

    for word_len in dct.keys():
        for word in dct[word_len].keys():
            file.write("| " + str(word_len) + " " * (7-len(str(word_len))) \
               + "| " + word + " " * (17-len(word)) \
               + "| " + str(dct[word_len][word]) + " " * (6-len(str(dct[word_len][word]))) + "|\n")
