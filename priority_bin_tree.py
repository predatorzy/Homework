class Node:
    def __init__(self, value: int, priority: int=None) -> None:
        self.value = value
        self.priority = priority
        self.right = None
        self.left = None


class Treap:
    def __init__(self) -> None:
        self.root = None

    @staticmethod
    def right_rotate(node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        return new_root

    @staticmethod
    def left_rotate(node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        return new_root

    def _insert(self, node, value, priority):
        if node is None:
            return Node(value, priority)

        if value < node.value:
            node.left = self._insert(node.left, value, priority)

            if node.left.priority > node.priority:
                node = self.right_rotate(node)

        else:
            node.right = self._insert(node.right, value, priority)

            if node.right.priority > node.priority:
                node = self.left_rotate(node)

        return node

    def insert(self, value, priority=None):
        self.root = self._insert(self.root, value, priority)

    def _delete(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)

        elif value > node.value:
            node.right = self._delete(node.right, value)

        else:
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            else:
                if node.left.priority > node.right.priority:
                    node = self.right_rotate(node)
                    node.right = self._delete(node.right, value)

                else:
                    node = self.left_rotate(node)
                    node.left = self._delete(node.left, value)

        return node

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _print_tree(self, node, indent=''):
        if node is not None:
            self._print_tree(node.right, indent + '  ')
            print(f'{indent}{node.value} (приоритет={node.priority})')
            self._print_tree(node.left, indent + '  ')

    def print_tree(self):
        self._print_tree(self.root)


t = Treap()
t.insert(5, 30)
t.insert(3, 40)
t.insert(7, 25)
t.insert(4, 35)
t.insert(6, 20)

print("дерево после вставки:")
t.print_tree()

t.delete(3)

print("\nдерево после удаления 3:")
t.print_tree()