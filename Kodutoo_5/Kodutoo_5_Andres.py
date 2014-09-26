def process_file(file, *functions, printStr = ""):
    '''
    Calls variable number of functions on the file.
    @arg file - handle to the file
    @arg *functions - passes the file handle to the functions and calls them
    @arg printResult - prints result of function if True
    @returns no return value
    '''
    for function in functions:
        file.seek(0)
        if printStr != "":
            print(function(file), printStr)
        else:
            function(file)

def count_words(file, unique = False):
    '''
    Counts the words in a file.
    @arg file - handle to file
    @arg unique - count only unique words. Default False.
    @returns no return value. Prints result.
    '''
    if unique:
        words = set()
    else:
        words = []
        
    word = ""
    
    for line in file:
        for char in line:
            if char.isalpha():
                word += char
            else:
                if word != "":
                    if unique:
                        words.add(word)
                    else:
                        words.append(word)
                        
                    word = ""

    if word != "":
        if unique:
            words.add(word)
        else:
            words.append(word)

    return len(words)

def count_unique_words_in_files(file1, file2):
    '''
    Counts the number of unique words in two files.
    @arg file1 - handle to file1
    @arg file2 - handle to file2
    @returns no return value. Prints result.
    '''
    count1 = count_words(file1, True)
    count2 = count_words(file2, True)
    return len(count1 | count2)

file1 = open("scarlet.txt")
file2 = open("hound.txt")
process_file(file1, count_words, printStr="number of words in " + file1.name)
process_file(file2, count_words, printStr="number of words in " + file2.name)

# pooleli
