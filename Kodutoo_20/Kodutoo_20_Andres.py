'''
Kodutoo 20
05.12.2014
Andres Liiver
'''

from tree import *

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
        words = read_words(file)
        tree = Tree(next(words))
        [tree.add(Tree(word)) for word in words]
        node, dist = tree.search("was")
        if node:
            node.printTree(1)
            print('Distance from root:', dist)

        print(tree.maxDepth())
        #outputFile = open("result.txt", "w", encoding="utf8")
        #tree.printToFile(outputFile)
        #outputFile.close()
    finally:
        file.close()

if __name__ == "__main__":
    main()