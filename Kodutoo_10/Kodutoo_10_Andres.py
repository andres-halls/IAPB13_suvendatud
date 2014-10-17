'''
Kodutoo 10
17.10.2014
Andres Liiver
'''

def read_words(file):
    file_contents = file.read()
    word = ""

    for char in file_contents:
        char = char.lower()
        if char.isalpha():
            word += char
        else:
            if word != "":
                yield word
                word = ""

def main():
    try:
        file = open("hound.txt", encoding="utf8")
    except Exception as e:
        print("Error occured when opening file:", e)
    else:
        try:
            words_all = read_words(file)
            words = [word for i, word in enumerate(words_all) \
                             if i % 4 == 0 and i < 400]

            avg_len = sum([len(word) for word in words]) // len(words)
            words = list(filter(lambda word: len(word) > avg_len, words))
            words = list(map(lambda word: word[0].upper() + word[1:], words))
            print(words)
        except Exception as e:
             print("Error occured when processing file:", e)

if __name__ == "__main__":
    main()
