'''
Kodutoo 12
28.10.2014
Andres Liiver
'''

from PIL import Image, ImageDraw
import string
import math

def get_words(file):
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
            if (word != "") and len(word) > 1:
                words.append(word)
                word = ""
            else:
                word = ""

    if (word != "") and len(word) > 1:
        words.append(word)

    return words

def pair_frequency(words):
    result = {}

    for word in words:
        pair = ""
        for char in word:
            if len(pair) == 2:
                if pair in result.keys():
                    result[pair] += 1
                else:
                    result[pair] = 1

                pair = char
            else:
                pair += char

    return result

def create_heat_map(pair_freq, fileName):
    img = Image.new(mode="L", size=(520,520))
    draw = ImageDraw.Draw(img)
    max_val = math.log(max(pair_freq.values()))

    # loop through all pairs

    x0 = 0
    y0 = 0
    x1 = 19
    y1 = 19

    for char1 in string.ascii_lowercase:
        for char2 in string.ascii_lowercase:
            if char1+char2 in pair_freq.keys():
                val = math.log(pair_freq[char1+char2]) / max_val * 255
                draw.rectangle([x0, y0, x1, y1], fill=val)

            x0 += 20
            x1 += 20

        x0 = 0
        y0 += 20
        x1 = 19
        y1 += 20

    img.save(fileName)

def main():
    try:
        file = open("hound.txt", encoding="utf8")
    except Exception as e:
        print("Error occured when opening file:", e)
    else:
        try:
            words = get_words(file)
            pair_freq = pair_frequency(words)

            try:
                outputFile = "result.png"
                create_heat_map(pair_freq, outputFile)
            except Exception as e:
                print("Error occured when creating heat map:", e)
            else:
                print("Heat map created successfully as " + outputFile)

        except Exception as e:
            print("Error occured when processing file:", e)
        finally:
            file.close()

if __name__ == "__main__":
    main()