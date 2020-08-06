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


class DoublyNode:
    def __init__(self, value=0, next_node=None, prev_node=None):
        self._value = value
        self._next_node = next_node
        self._prev_node = prev_node

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

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, node):
        self._prev_node = node


if __name__ == "__main__":
    test = Node(5, Node(123))
    print(test.value)
    print(test.next_node.value)

    test2 = DoublyNode(5, DoublyNode(123), DoublyNode(0))
    print(test2.value)
    print(test2.prev_node.value)
    print(test2.next_node.value)
