class Node:
    def __init__(self, value=None, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class Queue:
    def __init__(self):
        self.head = None
        pass

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        else:
            curr = self.head
            while curr.nextNode is not None:
                curr = curr.nextNode
            curr.nextNode = Node(value)
            return

    def pop(self):
        if self.head is None:
            print("Queue is empty")
        else:
            popped = self.head
            self.head = self.head.nextNode
            print(popped.value)
            return popped

    def print_queue(self):
        curr = self.head
        while curr is not None:
            print(str(curr.value)+" ")
            curr = curr.nextNode


if __name__ == '__main__':
    queue = Queue()
    queue.push(1)
    queue.push(10)
    queue.push(20)
    queue.push(30)
    queue.pop()
    queue.pop()
    queue.pop()
    queue.pop()
    queue.pop()


