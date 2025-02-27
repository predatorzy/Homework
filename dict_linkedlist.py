from datetime import datetime


class Node:
    def __init__(self, action_id: int, username: str, action_type: str) -> None:
        self.prev = None
        self.next = None
        self.action_id = action_id
        self.timestamp = datetime.now()
        self.username = username
        self.action_type = action_type

    def __str__(self) -> str:
        return f'id: {self.action_id}, time: {self.timestamp}, user: {self.username}, type: {self.action_type}'


class History:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.current = None
        self.actions_map  = {}
        self.next_action_id = 1
    
    def add_action(self, username, action_type) -> None:
        new_node = Node(self.next_action_id, username, action_type)
        self.actions_map[new_node.action_id] = new_node

        if not self.head:
            self.head = self.tail = self.current = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.current = new_node

        self.next_action_id += 1

    def undo(self) -> None:
        if self.current and self.current.prev:
            self.current = self.current.prev        
        print(f'current node: {self.current}')

    def redo(self) -> None:
        if self.current and self.current.next:
            self.current = self.current.next
        print(f'current node: {self.current}')

    def find_action(self, action_id: int):
        return self.actions_map.get(action_id, None)

    def remove_action(self, action_id: int) -> None:
        node = self.actions_map.pop(action_id, None)
        if node:
            if node.prev:
                node.prev.next = node.next
            
            if node.next:
                node.next.prev = node.prev
            
            if node == self.head:
                self.head = node.next
            
            if node == self.tail:
                self.tail = node.prev

            if node == self.current:
                self.current = node.prev if node.prev else self.head

    def filter_remove(self, action_type) -> None:
        to_remove = [action_id for action_id, node in self.actions_map.items() if node.action_type == action_type]
        for action_id in to_remove:
            self.remove_action(action_id)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def display(self) -> None:
        node = self.head
        while node:
            print(node)
            node = node.next


history = History()

history.add_action('monkey2004', 'fill')
history.add_action('dog2015', 'brush')
history.add_action('cool_guy2105', 'fill')
history.add_action('monkey2004', 'rotobrush')

history.display()
print()

print('undo:')
history.undo()
history.display()
print()

print('redo:')
history.redo()
history.display()
print()

print(history.find_action(3))
print()

history.filter_remove('fill')
history.display()
