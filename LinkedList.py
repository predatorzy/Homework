class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_linkedlist(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def add_first(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def add_last(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, index, value):
        if (index == 0):
            self.add_first(value)
            return
        if (index >= self.length):
            self.add_last(value)
            return

        new_node = Node(value)
        current = self.head
        for i in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self.length += 1

    def remove_first(self):
        if (self.length > 1):
            self.head = self.head.next

        if (self.length == 1):
            self.head = None
            self.tail = None

        if (self.length != 0):
            self.length -= 1

    def remove_last(self):
        if (self.length > 1):
            current = self.head
            for i in range(self.length - 2):
                current = current.next

            self.tail = current
            self.tail.next = None

        if (self.length == 1):
            self.head = None
            self.tail = None

        if (self.length != 0):
            self.length -= 1

    def remove(self, index):
        if (index == 0):
            self.remove_first()

            return

        if (index >= self.length):
            self.remove_last()

            return

        current = self.head

        for i in range(index - 1):
            current = current.next

        current.next = current.next.next
        self.length -= 1

    def remove_value(self, value):
        while self.head and self.head.value == value:
            self.head = self.head.next
            self.length -= 1

        current = self.head

        while current and current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.length -= 1

            else:
                current = current.next

        if self.head is None:
            self.tail = None

    def remove_duplicate(self):
        if self.head is None:
            return self

        values = set()
        current = self.head
        values.add(current.value)

        while current.next:
            if current.next.value in values:
                current.next = current.next.next
                self.length -= 1

            else:
                values.add(current.next.value)
                current = current.next

        self.tail = current

        return self

    def __iter__(self):
        return LinkedListIterator(self.head)

    @staticmethod
    def merge(linked1, linked2):
        merged_list = LinkedList()
        current1, current2 = linked1.head, linked2.head

        while current1 and current2:
            if current1.value < current2.value:
                merged_list.add_last(current1.value)
                current1 = current1.next

            else:
                merged_list.add_last(current2.value)
                current2 = current2.next

        while current1:
            merged_list.add_last(current1.value)
            current1 = current1.next

        while current2:
            merged_list.add_last(current2.value)
            current2 = current2.next

        return merged_list

    def compression(self):
        if self.head is None:
            return

        current = self.head

        while current.next:
            if current.value == current.next.value:
                current.next = current.next.next
                self.length -= 1

            else:
                current = current.next

        self.tail = current


linked_list = LinkedList()
linked_list.add_first(5)
linked_list.add_first(4)
linked_list.add_first(4)
linked_list.add_first(2)
linked_list.add_first(2)
linked_list.add_first(1)

linked_list.print_linkedlist()
linked_list.compression()
print()
linked_list.print_linkedlist()