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
    random.seed()
    h = 0

    for i in range(n):
        x = 2 * random.random() - 1
        y = 2 * random.random() - 1
        if x*x + y*y <= 1: h += 1

    pi = 4 * h / n
    return pi

def method_2(n):
    random.seed()
    numbers = set()

    for i in range(n):
        numbers.add(random.randint(1, 10000))

    combos = combinations(list(numbers), 2)
    num = 0

    for numbers in combos:
        if gcd(numbers[0], numbers[1]) == 1:
            num += 1

    pi = math.sqrt(6 / (num / len(combos)))
    return pi

def main():
    pi = method_1(100000)
    #pi = method_2(10000)
    print(pi)

if __name__ == "__main__":
    main()