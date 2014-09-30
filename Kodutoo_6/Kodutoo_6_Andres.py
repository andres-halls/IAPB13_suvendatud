from file_statistics import *

def main():
    try:
        file = open("hound.txt")
    except Exception as e:
        print("Error occured when opening file:", e)

    words = process_file(file)
    word_count = count_words(words)
    print(word_count['had'])
    file.close()

if __name__ == "__main__":
    main()
