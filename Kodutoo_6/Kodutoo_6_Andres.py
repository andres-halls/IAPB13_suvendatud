from file_statistics import *

def main():
    try:
        file = open("hound.txt", encoding="utf8")
    except Exception as e:
        print("Error occured when opening file:", e)
    else:
        try:
            words = process_file(file)
            word_count = count_words(words)
            top_words = find_top_words(word_count, 100)

            try:
                outputFile = open("result.txt", "w", encoding="utf8")
            except Exception as e:
                print("Error occured when opening output file:", e)
            else:
                try:
                    print_top_words(top_words, outputFile)
                except Exception as e:
                    print("Error occured when writing to output file:", e)
                else:
                    print("Result saved successfully to result.txt")
                finally:
                    outputFile.close()

        except Exception as e:
            print("Error occured when processing file:", e)
        finally:
            file.close()

if __name__ == "__main__":
    main()