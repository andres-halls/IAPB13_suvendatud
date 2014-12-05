class Tree:
    def __init__(self, data, count = 1, left = None, right = None):
        self.data = data
        self.count = count
        self.left = left
        self.right = right

    def add(self, node):
        if self.data == node.data:
            self.count += 1
            return

        if self.data > node.data: # insert left
            if self.left is None:
                self.left = node
            else:
                self.left.add(node)
        else: # insert right
            if self.right is None:
                self.right = node
            else:
                self.right.add(node)

    def delete(self, node):
        pass

    def maxDepth(self, depth=0):
        if self is None: return depth

    def minValue(self):
        pass

    def printTree(self):
        pass

    def search(self, word):
        pass

if __name__ == "__main__":
    pass