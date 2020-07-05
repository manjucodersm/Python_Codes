class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = self.get_level() * ' ' * 3
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

root = TreeNode('INDIA')

state = TreeNode('STATE')
state.add_child(TreeNode('KARNATAKA'))
state.add_child(TreeNode('ANDHRA'))
state.add_child(TreeNode('TAMILNADU'))

lan = TreeNode('LAUNGUES')
lan.add_child(TreeNode('KANNADA'))
lan.add_child(TreeNode('TELUGU'))
lan.add_child(TreeNode('TAMIL'))

root.add_child(state)
root.add_child(lan)

root.print_tree()
