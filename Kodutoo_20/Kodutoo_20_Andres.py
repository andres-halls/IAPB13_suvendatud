'''
Kodutoo 20
05.12.2014
Andres Liiver
'''

from tree import *

def main():
    left = Tree("blah")
    right = Tree("zeus")
    tree = Tree("car", left=left, right=right)
    tree.add(Tree("test"))
    tree.add(Tree("test"))
    tree.maxDepth()
    tree = tree

if __name__ == "__main__":
    main()