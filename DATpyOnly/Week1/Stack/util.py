class Node:
    def __init__(self, value=0, next_node=None):
        self._value = value
        self._next_node = next_node

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        self._next_node = node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, value):
        node = Node(value, self.head)
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def pop_front(self):
        if self.head is None:
            return -1
        value = self.head.value
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return value

    def top_front(self):
        if self.head is not None:
            return self.head.value
        return -1

    def push_back(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def pop_back(self):
        if self.head is None:
            return -1
        if self.head is self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        else:
            buffer_node = self.head
            while buffer_node.next_node.next_node is not None:
                buffer_node = buffer_node.next_node
            value = self.tail.value
            buffer_node.next_node = None
            self.tail = buffer_node
            return value

    def top_back(self):
        if self.tail is not None:
            return self.tail.value
        return -1

    def empty(self):
        return self.head is None

    def find(self, value):
        if self.head is None:
            return False
        buffer = self.head
        while True:
            if buffer is None:
                return False
            if buffer.value == value:
                return True
            buffer = buffer.next_node

    def add_after(self, node, value):
        node2 = Node(value, node.next_node)
        node.next_node = node2
        if self.tail is node:
            self.tail = node2

    def add_before(self, node, value):
        pass

    def erase(self, value):
        prev = None
        buffer = self.head
        if self.empty():
            print("List is already empty!")
            return
        while buffer is not None:
            if buffer.value == value:  # delete this
                pos = ''
                if buffer is self.head:
                    pos = 'head'
                    self.head = buffer.next_node
                    buffer.next_node = None
                elif buffer is self.tail:
                    pos = 'tail'
                    prev.next_node = None
                    self.tail = prev
                else:
                    pos = 'middle'
                    prev.next_node = buffer.next_node
                    buffer.next_node = None
                print("Delete successful:", pos)
                return
            prev = buffer
            buffer = buffer.next_node

    def show_all(self):
        buffer = self.head
        while buffer is not None:
            print(buffer.value, end=" ")
            buffer = buffer.next_node
        print()
