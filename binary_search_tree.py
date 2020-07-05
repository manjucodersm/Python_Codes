class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, child):
        if child == self.data:
            return

        if child < self.data:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = BinarySearchTree(child)
        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = BinarySearchTree(child)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    elements = [4, 3, 1, 6, 8, 2, 9, 5]
    number_tree = build_tree(elements)
    print(number_tree.in_order_traversal())
