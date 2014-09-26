import re

def file_get_words(*fileNames):
    '''
    Takes a variable number of fileNames and returns
    a two-dimensional list of words for each file.
    @arg *fileNames - variable number of file names.
    @returns list of words for each file
    '''
    words = []

    for fileName in fileNames:
        file = open(fileName)
        words.append(words_in_file_re(file))
        file.close()

    return words

#######################################

def words_in_file(file):
    '''
    Returns list of words in a file.
    @arg file - handle to file
    @returns list of words
    '''
    file_contents = file.read()
    words = []
    word = ""
    
    for char in file_contents:
        if char.isalpha():
            word += char
        else:
            if word != "":
                words.append(word)
                word = ""

    if word != "":
        words.append(word)

    return words

#######################################

def words_in_file_re(file):
    '''
    Returns list of words in a file using regular expression.
    @arg file - handle to file
    @returns list of words
    '''
    return re.findall(r'\w+', file.read())

#######################################

def print_results(functions, printStrs):
    '''
    Higher-order function that calls variable number of functions and
    prints the results with the corresponding printStr appended from printStrs.
    @arg functions - list of functions to call
    @arg printStr - list of strings to append to print of each result
    @returns no return value
    '''
    for i, function in enumerate(functions):
        result = function()
        print(result, printStrs[i])

#######################################

file1 = "scarlet.txt"
file2 = "hound.txt"
words = file_get_words("scarlet.txt", "hound.txt")
words_unique = [set(words[0]), set(words[1])]

functions = [
    lambda: len(words[0]), lambda: len(words[1]),
    lambda: len(words_unique[0]), lambda: len(words_unique[1]),
    lambda: len(words_unique[0] | words_unique[1]),
    lambda: len(words_unique[0] - words_unique[1]),
    lambda: len(words_unique[1] - words_unique[0]),
    lambda: len(words_unique[0] & words_unique[1])
]

printStrs = [
    "words in file " + file1, "words in file " + file2,
    "unique words in file " + file1, "unique words in file " + file2,
    "total unique words in files " + file1 + " and " + file2,
    "unique words in " + file1 + " not present in " + file2,
    "unique words in " + file2 + " not present in " + file1,
    "unique words that are in both " + file1 + " and " + file2
]

print_results(functions, printStrs)