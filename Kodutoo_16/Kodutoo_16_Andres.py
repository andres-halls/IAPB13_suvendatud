'''
Kodutoo 16
14.11.2014
Andres Liiver
'''

import timeit as t
from matplotlib import pyplot
from Tund16gen import *

def linear_search(lst, num):
    for item in lst:
        if item == num:
            return True

    return False

def binary_search(lst, num, sort=False):
    if sort:
        lst = sorted(lst)

    imin = 0
    imax = len(lst)

    while imax >= imin:
        imid = (imin+imax) // 2

        if lst[imid] == num:
            return True
        elif lst[imid] < num:
            imin = imid + 1
        else:
            imax = imid - 1

    return False

def main():
    linearTimes = []
    binary1Times = []
    binary2Times = []

    for i in range(16):
        n = 2**i
        gen = gimme_my_input(n, "blah")

        # linear search test
        linearTimes.append(t.timeit("linear_search(gen[0], next(gen[1]))", "from __main__ import linear_search", number = 1))

        # binary search test 1
        sortedData = sorted(gen[0])
        #binary1Times.append(binary_search(sortedData, next(gen[1])))

        # binary search test 2
        #binary_search(gen[0], next(gen[1]), True)

if __name__ == "__main__":
    main()