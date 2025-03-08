class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.previous = None
        self.value = value


class DoubleLinkedList:
    def __init__(self, cycle=False) -> None:
        self.head = None
        self.tail = None
        self.length = 0
        self.cycle = cycle

    def __str__(self):
        nodes = []
        current = self.head
        visited = set()

        while current and current not in visited:
            nodes.append(str(current.value))
            visited.add(current)
            current = current.next
            if current == self.head and self.cycle:
                break

        return ' <-> '.join(nodes)

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
            if self.cycle:
                self.head.next = self.head.previous = self.head
        else:
            new_node.previous = self.tail
            new_node.next = self.head if self.cycle else None
            self.tail.next = new_node
            if self.cycle:
                self.head.previous = new_node

            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
            if self.cycle:
                self.head.next = self.head.previous = self.head

        else:
            new_node.next = self.head
            self.head.previous = new_node

            if self.cycle:
                new_node.previous = self.tail
                self.tail.next = new_node

            self.head = new_node

        self.length += 1

    def insert(self, index, value):
        if index <= 0:
            self.prepend(value)

        elif index >= self.length:
            self.append(value)

        else:
            new_node = Node(value)
            current = self.head
            for _ in range(index - 1):
                current = current.next

            new_node.next = current.next
            new_node.previous = current
            current.next.previous = new_node
            current.next = new_node
            self.length += 1

    def remove(self, index):
        if not self.head or index < 0 or index >= self.length:
            return

        if index == 0:
            if self.length == 1:
                self.head = self.tail = None

            else:
                self.head = self.head.next
                self.head.previous = self.tail if self.cycle else None
                if self.cycle:
                    self.tail.next = self.head

        elif index == self.length - 1:
            self.tail = self.tail.previous
            self.tail.next = self.head if self.cycle else None
            if self.cycle:
                self.head.previous = self.tail

        else:
            current = self.head
            for _ in range(index):
                current = current.next

            current.previous.next = current.next
            current.next.previous = current.previous

        self.length -= 1

    def remove_value(self, value):
        current = self.head
        removed = False

        while current:
            if current.value == value:
                removed = True
                if current == self.head:
                    self.remove(0)
                    current = self.head

                elif current == self.tail:
                    self.remove(self.length - 1)
                    break

                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    self.length -= 1

            current = current.next if not removed else self.head

    def __iter__(self):
        current = self.head
        visited = set()
        while current and current not in visited:
            yield current.value
            visited.add(current)
            current = current.next
            if current == self.head and self.cycle:
                break

    def __getitem__(self, index):
        if self.length == 0:
            raise IndexError('список пустой')

        if self.cycle:
            index %= self.length

        if index < 0 or index >= self.length:
            raise IndexError('индекс аут оф ренж')

        current = self.head

        for _ in range(index):
            current = current.next

        return current.value

    def reverse(self):
        reversed_list = DoubleLinkedList(self.cycle)
        current = self.tail
        while current:
            reversed_list.append(current.value)
            current = current.previous
            if self.cycle and current == self.tail:
                break
        return reversed_list
