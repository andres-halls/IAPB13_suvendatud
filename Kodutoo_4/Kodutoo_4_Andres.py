# Kodutoo 4
# 22.09.2014
# Andres Liiver

def treasure_map(size, treasures):
    # Best case: O(1)
    # Average case: O(n)
    # Worst case: O(n^3)

    map = [[0] * size[0] for i in range(size[1])]

    for y in range(size[1]):
        for x in range(size[0]):
            for treasure in treasures:
                if x == treasure[0] and y == treasure[1]:
                    map[y][x] = 'X'
                    break
                elif abs(x - treasure[0]) <= 1 and abs(y - treasure[1]) <= 1:
                    map[y][x] += 1

    return map

def print_treasure(map):
    for row in map: print(''.join(str(e) for e in row))

print_treasure(treasure_map((4, 5), [(2, 0), (1, 1), (2, 2), (1, 3)]))
print()
print_treasure(treasure_map((7, 9), [(2, 0), (4, 0), (1, 1), (2, 2), (1, 3), (6, 4), (3, 5), (1, 6), (6, 7), (0, 8)]))