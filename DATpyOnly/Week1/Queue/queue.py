from .util import Node
'''
Queue API

enqueue(value)
value dequeue()
Boolean empty()
'''


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        if self.empty():
            self.head = Node(value)
            self.tail = self.head
            return
        buffer = Node(value)
        self.tail.next_node = buffer
        self.tail = buffer

    def dequeue(self):
        if self.empty():
            print('Queue is empty')
            return -1

        value = 0
        if self.head is self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
        else:
            value = self.head.value
            buffer = self.head.next_node
            self.head.next_node = None
            self.head = buffer
        return value

    def empty(self):
        return self.head is None


def test_queue(numbers=[9, -2, 0, 1, 2, 3, 4]):
    q = Queue()
    for item in numbers:
        q.enqueue(item)
    while not q.empty():
        print(q.dequeue())


if __name__ == "__main__":
    test_queue()
