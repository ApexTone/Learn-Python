# python3

from collections import namedtuple


class Node:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node


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
            #print('Stack is empty')
            return -1
        return self.top.value

    def pop(self):
        if self.empty():
            #print('Stack is empty')
            return -1
        buffer = self.top
        self.top = self.top.next_node
        buffer.next_node = None
        return buffer.value

    def empty(self):
        return self.top is None

    def show_all(self):  # for debug process
        if self.empty():
            #print('Stack is empty')
            return -1
        buffer = self.top
        while buffer is not None:
            print(buffer.value, end=" ")
            buffer = buffer.next_node
        print('')
        return


Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = Stack()
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.push((i, next))  # push in as tuple

        if next in ")]}":
            if opening_brackets_stack.empty():
                return i+1
            top = opening_brackets_stack.pop()
            if not are_matching(top[1], next):
                return i+1

    if opening_brackets_stack.empty():
        return 'Success'
    else:
        return opening_brackets_stack.pop()[0] + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
