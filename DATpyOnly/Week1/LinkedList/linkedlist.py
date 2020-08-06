'''
List API

PushFront(value)
value TopFront()
PopFront()
PushBack(value)
value TopBack()
PopBack()
Boolean Find(value)
Erase(value)
Boolean Empty()
AddBefore(Node,value)
AddAfter(Node,value)
'''
from .node import Node
import random
import time


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


class DoubleLinkedList:  # use DoublyNode
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, value):
        node = DoublyNode(value)
        if self.tail is None:
            self.head = node
            self.tail = node
            node.prev_node = None
        else:
            self.tail.next = node
            node.prev_node = self.tail
            self.tail = node

    def pop_back(self):
        if self.head is None:
            return -1
        if self.head is self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
        else:
            value = self.tail.value
            self.tail = self.tail.prev_node
            self.tail.next_node = None

    def add_before(self, node, value):
        node2 = DoublyNode(value, node, node.prev_node)
        node.prev_node = node2
        if node2.prev_node is not None:
            node2.prev_node.next_node = node2
        if self.head is node:
            self.head = node2

    def top_front(self):
        if self.head is not None:
            return self.head.value
        return -1

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

    def show_all(self):
        buffer = self.head
        while buffer is not None:
            print(buffer.value, end=" ")
            buffer = buffer.next_node
        print()

    def push_front(self, value):
        node = DoublyNode(value, self.head, None)
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def pop_front(self):
        if self.head is None:
            return -1
        value = self.head.value
        self.head = self.head.next_node
        self.head.prev_node = None
        if self.head is None:
            self.tail = None
        return value

    # the command below need to be edit to utilize DoublyNode
    def add_after(self, node, value):
        buffer = node.next_node
        node2 = DoublyNode(value, buffer)
        buffer.prev_node = node2
        node.next_node = node2
        node2.prev_node = node
        if self.tail is node:
            self.tail = node2

    def erase(self, value):
        pass


def test_single_linked(numbers=[-1, 0, 1, 2, 3, 4]):
    numbers = numbers
    lst = LinkedList()
    random.seed(time.time())
    print("------------Start test------------")
    for item in numbers:
        if random.random() < random.random():
            lst.push_front(item)
        else:
            lst.push_back(item)
    lst.show_all()
    print("back:", lst.top_back())
    print("front:", lst.top_front())
    lst.show_all()
    # print("pop front:", lst.pop_front())
    print("pop back:", lst.pop_back())
    lst.show_all()
    lst.erase(0)
    lst.show_all()
    print("------------End test------------")


def test_double_linked(numbers=[-1, 0, 1, 2, 3, 4]):
    numbers = numbers
    lst = DoubleLinkedList()
    random.seed(time.time())
    print("------------Start test------------")
    for item in numbers:
        if random.random() < random.random():
            lst.push_front(item)
        else:
            lst.push_back(item)
    lst.show_all()
    print("back:", lst.top_back())
    print("front:", lst.top_front())
    lst.show_all()
    # print("pop front:", lst.pop_front())
    print("pop back:", lst.pop_back())
    lst.show_all()
    print("------------End test------------")


if __name__ == "__main__":
    test_single_linked()
    # test_double_linked()
