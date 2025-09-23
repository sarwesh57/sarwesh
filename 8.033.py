class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.ins(self.root, key)

    def ins(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self.ins(node.left, key)
        elif key > node.key:
            node.right = self.ins(node.right, key)
        return node

    def delete(self, key):
        self.root = self._del(self.root, key)

    def _del(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._del(node.left, key)
        elif key > node.key:
            node.right = self._del(node.right, key)
        else:
           
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            min_node = self.min(node.right)
            node.key = min_node.key
            node.right = self._del(node.right, min_node.key)
        return node

    def min(self, node):
        while node.left:
            node = node.left
        return node

    def search(self, key):
        return self.srh(self.root, key)

    def srh(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self.srh(node.left, key)
        else:
            return self.srh(node.right, key)

    def inorder(self):
        self._in(self.root)
        print()

    def _in(self, node):
        if node:
            self._in(node.left)
            print(node.key, end=' ')
            self._in(node.right)

    def preorder(self):
        self._pre(self.root)
        print()

    def _pre(self, node):
        if node:
            print(node.key, end=' ')
            self._pre(node.left)
            self._pre(node.right)
bst = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

print("In-order:")
bst.inorder()

print("Pre-order:")
bst.preorder()

print("Search 60:", bst.search(60))  
print("Search 25:", bst.search(25))

bst.delete(70)
bst.delete(30)
bst.delete(20)

print("After Deletion:")
bst.inorder()
bst.preorder()
