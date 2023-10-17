class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"

    def insert(self, data):
        if data <= self.data:
            if self.left == None:
                self.left = TreeNode(data, None, None)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = TreeNode(data, None, None)
            else:
                self.right.insert(data)

    def sorted_data(self):
        data = []
        if self.left != None:
            data += self.left.sorted_data()
        data.append(self.data)
        if self.right != None:
            data += self.right.sorted_data()

        return data


class BinarySearchTree:
    def __init__(self, tree_data):
        if len(tree_data) == 0:
            self.root = TreeNode(None)
        else:
            self.root = TreeNode(tree_data[0])

        for datum in tree_data[1:]:
            self.root.insert(datum)

    def data(self):
        return self.root

    def sorted_data(self):
        return self.root.sorted_data()
