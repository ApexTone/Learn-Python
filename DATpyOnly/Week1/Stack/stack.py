'''
Stack API

push(value)
top()
pop()
empty()
'''
from .util import Node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        if self.empty():
            self.top = Node(value)
            return
        node = Node(value, self.top)
        self.top = node

    def top(self):
        if self.empty():
            print('Stack is empty')
            return -1
        return self.top.value

    def pop(self):
        if self.empty():
            print('Stack is empty')
            return -1
        buffer = self.top
        self.top = self.top.next_node
        buffer.next_node = None
        return buffer.value

    def empty(self):
        return self.top is None

    def show_all(self):  # for debug process
        if self.empty():
            print('Stack is empty')
            return -1
        buffer = self.top
        while buffer is not None:
            print(buffer.value, end=" ")
            buffer = buffer.next_node
        print('')
        return


def test_stack(numbers=[-1, 0, 1, 2, 3, 4]):
    stk = Stack()
    stk.pop()
    for item in numbers:
        stk.push(item)
    stk.show_all()
    for _ in numbers:
        print(stk.pop())
    stk.show_all()


if __name__ == "__main__":
    test_stack()


'''
()([]
'''
