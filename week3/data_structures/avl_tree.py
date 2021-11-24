class Node:
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.height = 1

    def small_turn_right(self):
        new_root = self.left
        new_root.parent = None
        self.left = new_root.right
        if self.left is not None:
            self.left.parent = self
        new_root.right = self
        self.parent = new_root
        new_root.update_height()
        self.update_height()

        return new_root

    def small_turn_left(self):
        new_root = self.right
        new_root.parent = None
        self.right = new_root.left
        if self.right is not None:
            self.right.parent = self
        new_root.left = self
        self.parent = new_root
        self.update_height()
        new_root.update_height()

        return new_root

    def big_turn_right(self):
        self.left = self.left.small_turn_left()
        new_root = self.small_turn_right()

        return new_root

    def big_turn_left(self):
        self.right = self.right.small_turn_right()
        new_root = self.small_turn_left()

        return new_root

    def is_balanced(self):
        right_height = self.right.height if self.right else 0
        left_height = self.left.height if self.left else 0
        return abs(left_height - right_height) <= 1, left_height - right_height

    def update_height(self):
        self.height = max(
                        self.left.height if self.left else 0,
                        self.right.height if self.right else 0
                    ) + 1

    def balance(self):
        new_root = None
        is_balanced, height_diff = self.is_balanced()
        if not is_balanced:
            if height_diff < 0:
                # right subtree height more then left
                tmp_balanced, tmp_diff = self.right.is_balanced()
                if tmp_diff >= 0:
                    new_root = self.big_turn_left()
                else:
                    new_root = self.small_turn_left()
            else:
                # left subtree height more then right
                tmp_balanced, tmp_diff = self.is_balanced()
                if tmp_diff >= 0:
                    """turn right"""
                    new_root = self.small_turn_right()
                else:
                    """big turn right"""
                    new_root = self.big_turn_right()

        return new_root


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
            new_root = node.balance()
            # node.update_height()
            self.root = new_root or self.root
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

    def get_min_of_tree(self, node=None):
        node = node or self.root
        if node and node.left:
            return self.get_min_of_tree(node.left)
        else:
            return node.key if node else None

    def get_max_of_tree(self, node=None):
        node = node or self.root
        if node and node.right:
            return self.get_max_of_tree(node.right)
        else:
            return node.key if node else None

    def next_element_after(self, key):
        next_element = None
        node = self.find(key)
        if node is not None:
            if node.right:
                next_element = self.get_min_of_tree(node.right)
            else:
                while node.parent:
                    if node.parent.left == node:
                        next_element = node.parent.key
                        break
                    else:
                        node = node.parent
        return next_element

    def split_tree(self):
        pass

    def merge_trees(self):
        pass

    def __getitem__(self):
        pass
    

if __name__ == "__main__":
    avl_tree = AvlTree()
    # avl_tree.add(1)
    # avl_tree.add(0)
    # avl_tree.add(5)
    # avl_tree.add(4)
    # avl_tree.add(3)
    #
    # print(avl_tree.find(1))
    # print(avl_tree.find(3))
    # print(avl_tree.find(2))
    # print(avl_tree.find(0))
    # print(avl_tree.find(-2))
    #
    # print(f"max: {avl_tree.get_max_of_tree()}")
    # print(f"min: {avl_tree.get_min_of_tree()}")
    # print(f"next after 1: {avl_tree.next_element_after(1)}")
    # print(f"next after 3: {avl_tree.next_element_after(3)}")
    # print(f"next after 5: {avl_tree.next_element_after(5)}")

    # avl_tree.add(1)
    # avl_tree.add(0)
    # avl_tree.add(3)
    # avl_tree.add(2)
    # avl_tree.add(4)
    # avl_tree.add(5)

    # avl_tree.add(1)
    # avl_tree.add(0)
    # avl_tree.add(2)
    # avl_tree.add(3)
    # avl_tree.add(4)
    # avl_tree.add(5)
    # GOTO: проверить родителей у вершин в обоих примерах

    avl_tree.add(1)
    avl_tree.add(2)
    avl_tree.add(3)

    print("qwe")