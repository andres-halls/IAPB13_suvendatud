'''
Kodutoo 9
15.10.2014
Andres Liiver
'''

import random
import timeit as t
import math

def combinations(items, r, strResult = False):
    '''
    Calculates all r length combinations of items 
    @arg items - list of items
    @arg r - length of combinations
    @arg strResult - if True, returns result as multi-line string
    @returns two-dimensional list of combinations or multi-line string
    '''
    if items == []:
        return []

    if r > len(items):
        if strResult:
            return "combinations: r cannot be bigger than the number of items!"
        else:
            return []

    if r == 1:
        return [[item] for item in items]

    result = []; subCombinations = []

    for i, item in enumerate(items):
        subCombinations = combinations(items[i+1:], r-1)
        if subCombinations == []: break
        for item2 in subCombinations:
            result += [[item] + item2]

    if strResult:
        resultStr = ""
        for subList in result:
            resultStr += ', '.join(str(item) for item in subList)
            resultStr += '\n'

        return resultStr
    else:
        return result

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t

    return a

def method_1(n):
    global pi
    random.seed()
    h = 0

    for i in range(n):
        x = 2 * random.random() - 1
        y = 2 * random.random() - 1
        if x*x + y*y <= 1: h += 1

    pi = 4 * h / n
    return pi

def method_2(n):
    global pi
    random.seed()
    num = 0

    while num == 0:
        numbers = set()

        for i in range(n):
            numbers.add(random.randint(2, 100))

        combos = combinations(list(numbers), 2)
        num = 0

        for numbers in combos:
            if gcd(numbers[0], numbers[1]) == 1:
                num += 1

    pi = math.sqrt(6 / (num / len(combos)))
    return pi

def main():
    print("| algorithm \t| n \t\t| pi \t\t| time \t\t| accuracy")

    # Tests for method_1

    for i in range(23):
        n = 2**i
        time = t.timeit("method_1({0})".format(n), "from __main__ import method_1", number = 1)
        accuracy = abs(math.pi - pi)
        if n < 10000:
            print("| {0} \t| {1} \t\t| {2:.8f} \t| {3:.4f} \t| {4:.8f}".format("method_1", n, pi, time, accuracy))
        else:
            print("| {0} \t| {1} \t| {2:.8f} \t| {3:.4f} \t| {4:.8f}".format("method_1", n, pi, time, accuracy))

    print()
    # Tests for method_2

    for i in range(1, 23):
        n = 2**i
        time = t.timeit("method_2({0})".format(n), "from __main__ import method_2", number = 1)
        accuracy = abs(math.pi - pi)
        if n < 10000:
            print("| {0} \t| {1} \t\t| {2:.8f} \t| {3:.4f} \t| {4:.8f}".format("method_2", n, pi, time, accuracy))
        else:
            print("| {0} \t| {1} \t| {2:.8f} \t| {3:.4f} \t| {4:.8f}".format("method_2", n, pi, time, accuracy))


if __name__ == "__main__":
    pi = 0 # global pi variable
    main()