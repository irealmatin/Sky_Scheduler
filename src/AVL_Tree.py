class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AvlTree:
    def __init__(self):
        self.root = None

    def __get_height(self, node):
        return node.height if node else 0

    def __get_balance(self, node):
        return self.__get_height(node.left) - self.__get_height(node.right) if node else 0

    def __update_height(self, node):# we write this method to avoid duplicate code in insert && delete 
        if node:
            node.height = 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def __right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        self.__update_height(node)
        self.__update_height(new_root)
        return new_root

    def __left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        self.__update_height(node)
        self.__update_height(new_root)
        return new_root

    def __rebalance(self, node, key):
        balance = self.__get_balance(node)

        if balance > 1:
            if key < node.left.key:  # L-L
                return self.__right_rotate(node)
            else:  # L-R
                node.left = self.__left_rotate(node.left)
                return self.__right_rotate(node)

        
        if balance < -1:
            if key > node.right.key:  # R-R
                return self.__left_rotate(node)
            else:  # R-L
                node.right = self.__right_rotate(node.right)
                return self.__left_rotate(node)

        return node

    def __insert(self, node, key, value):
        if not node:
            return TreeNode(key, value)

        if key < node.key:
            node.left = self.__insert(node.left, key, value)
        else:
            node.right = self.__insert(node.right, key, value)

        self.__update_height(node)
        return self.__rebalance(node, key)

    def __min_value_node(self, node): # we using this for delete process method in case of min of Rchild (or we can write max of Lchild too)!
        """Return the node with 
        the smallest key
        in the tree."""
        current = node
        while current.left:
            current = current.left
        return current

    def __delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self.__delete(node.left, key)
        elif key > node.key:
            node.right = self.__delete(node.right, key)
        else:
            # Node with one or no children
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Node with two children: Get the in-order {successor: is the node with the smallest key greater than the given nodes key.}
            successor = self.__min_value_node(node.right)
            node.key, node.value = successor.key, successor.value
            node.right = self.__delete(node.right, successor.key)

        self.__update_height(node)
        return self.__rebalance(node, key)

    #------------------------ Public Method-------------------------------#

    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value)

    def delete(self, key):
        self.root = self.__delete(self.root, key)

    def search(self, node, key):
        if not node or node.key == key:
            return node
        return self.search(node.left, key) if key < node.key else self.search(node.right, key)

    def inorder_traversal(self, node):# we should return 1by1 not a list-> fixed : using python generator  
        if node:
            yield from self.inorder_traversal(node.left)
            yield (node.key, node.value)
            yield from self.inorder_traversal(node.right)

    def print_inorder(self):
        for key, value in self.inorder_traversal(self.root):
            print(f"Flight Number: {key} | Details -> {value}")


