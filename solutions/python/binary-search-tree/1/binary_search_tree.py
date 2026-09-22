class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.tree_data = tree_data
        self.root = TreeNode(self.tree_data[0])
        for i in self.tree_data[1:]:
            self._insert(self.root, i)

    def _insert(self, current_node, new_num):
        if current_node.data >= new_num:
            if current_node.left:
                self._insert(current_node.left, new_num)
            else:
                current_node.left = TreeNode(new_num)
        else:
            if current_node.right:
                self._insert(current_node.right, new_num)
            else:
                current_node.right = TreeNode(new_num)

    def _print(self, current_node):
        if current_node.left:
            self._print(current_node.left)
        self.test.append(current_node.data)
        if current_node.right:
            self._print(current_node.right)
        return self.test

    def data(self):
        return self.root

    def sorted_data(self):
        self.test = []
        self._print(self.root)
        return self.test