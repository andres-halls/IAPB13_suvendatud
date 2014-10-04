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
    and the corresponding value is a list of tuples such as (word, frequency)

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
    dctFreq = {}
    dctLen = {}

    # Build a dictionary where key is the frequency
    # and value is a list of words with that frequency

    for word, freq in dct.items():
        if freq in dctFreq.keys():
            dctFreq[freq].append(word)
        else:
            dctFreq[freq] = [word]

    # Build a dictionary where key is the word length
    # and value is a list of words with that length

    for word in dct.keys():
        word_len = len(word)

        if word_len in dctLen.keys():
            dctLen[word_len].append(word)
        else:
            dctLen[word_len] = [word]

    # Build result dictionary

    freqs = sorted(dctFreq.keys(), reverse = True)

    for word_len, word_list in dctLen.items():
        for freq in freqs:
            for word in word_list:
                if word_len in result.keys() and len(result[word_len]) == n:
                    break

                if word in dctFreq[freq]:
                    if word_len in result.keys():
                        result[word_len][word] = freq
                    else:
                        result[word_len] = {word : freq}

    # Sort by frequency
    for key, dct in result.items():
        result[key] = sorted(dct.items(), key=lambda x:x[0])
        result[key] = sorted(result[key], key=lambda x:x[1], reverse = True)

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

    for word_len, word_dct in dct.items():
        for word, freq in word_dct:
            file.write("| " + str(word_len) + " " * (7-len(str(word_len))) \
               + "| " + word + " " * (17-len(word)) \
               + "| " + str(freq) + " " * (6-len(str(freq))) + "|\n")
