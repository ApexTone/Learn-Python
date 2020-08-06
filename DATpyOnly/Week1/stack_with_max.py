# python3
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)


class Node:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None
        self.max = None

    def Push(self, value):
        if self.empty():
            self.top = Node(value)
            return
        node = Node(value, self.top)
        self.top = node
        # if self.max is None or self.max < value:
        #    self.max = self.top

    def Pop(self):
        if self.empty():
            #print('Stack is empty')
            return -1
        buffer = self.top
        self.top = self.top.next_node
        buffer.next_node = None
        return buffer.value

    def Max(self):
        if self.empty():
            return
        buffer = self.top
        maxx = None
        while buffer is not None:
            if maxx is None or maxx < buffer.value:
                maxx = buffer.value
            buffer = buffer.next_node
        return maxx

    def empty(self):
        return self.top is None


if __name__ == '__main__':
    stack = StackWithMax()  # naive method

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
