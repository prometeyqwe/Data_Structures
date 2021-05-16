from typing import Mapping


class Node:
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.height = 1

    def small_turn_right(self):
        pass

    def small_turn_left(self):
        pass

    def big_turn_right(self):
        pass

    def big_turn_left(self):
        pass

    def is_balanced(self):
        right_height = self.right.height if self.right else 0
        left_height = self.left.height if self.left else 0
        return abs(left_height - right_height) <= 1, left_height > right_height

    def update_height(self):
        self.height = max(
                        self.left.height if self.left else 1, 
                        self.right.height if self.right else 1
                    ) + 1

    def balance(self):
        is_balanced, turn_to_right = self.is_balanced()
        if not is_balanced:
            if not turn_to_right:
                """ doing turn left """
            else:
                """ doing turn right """
                self.left.parent = self.parent
                self.parent.right = self.left
                self.left.right = self
                self.parent = self.left


class AvlTree:
    def __init__(self):
        self.root = None

    def add(self, key, node=None):
        node = node or self.root
        if node is not None:
            if key > node.key:
                if node.right is not None:
                    self.add(key, node=node.right)
                else:
                    node.right = Node(key)
                    node.right.parent = node
            else:
                if node.left is not None:
                    self.add(key, node=node.left)
                else:
                    node.left = Node(key)
                    node.left.parent = node
            node.update_height()
            node.balance()
        else:
            self.root = Node(key)  # node == self.root only

    def find(self, key, node=None):
        node = node or self.root

        if key > node.key:
            if node.right is not None:
                result = self.find(key, node.right)
            else:
                result = None
        elif key < node.key:
            if node.left is not None:
                result = self.find(key, node.left)
            else:
                result = None
        else:
            result = node
        return result

    def delete(self, key):
        pass

    def _min(self):
        pass

    def _max(self):
        pass

    def next_element_after(self, key):
        pass

    def _split(self):
        pass

    def _merge(self):
        pass

    def __getitem__(self):
        pass
    

if __name__ == "__main__":
    avl_tree = AvlTree()
    avl_tree.add(1)
    avl_tree.add(0)
    avl_tree.add(5)
    avl_tree.add(4)
    avl_tree.add(3)

    print(avl_tree.find(1))
    print(avl_tree.find(3))
    print(avl_tree.find(2))
    print(avl_tree.find(0))
    print(avl_tree.find(-2))
