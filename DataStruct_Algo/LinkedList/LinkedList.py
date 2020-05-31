class Node:
    def __init__(self, data):
        self.data = data  # data for this node
        self.next_node = None  # next element is nothing


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if not prev_node:
            print("Can't find previous node in the list")
            return
        new_node = Node(data)
        new_node.next_node = prev_node.next_node
        prev_node.next_node = new_node

    def delete_node(self, key):
        curr_node = self.head
        if curr_node is not None and curr_node.data == key:  # delete at head
            self.head = curr_node.next_node
            curr_node = None
            return
        else:
            prev_node = None
            while curr_node.data != key:
                prev_node = curr_node
                curr_node = curr_node.next_node
            if curr_node is not None:
                prev_node.next_node = curr_node.next_node
                curr_node = None
            else:
                print("Can't find element to delete")

    def delete_at_index(self, key):  # deletion by index
        if key < 0:  # index out of bound
            print("Index must be a non-negative number")
            return
        counter = 0
        curr_node = self.head
        if key == 0:  # head deletion
            self.head = curr_node.next_node
            curr_node = None
            return
        else:
            prev_node = None
            while counter < key and curr_node is not None:
                prev_node = curr_node
                curr_node = curr_node.next_node
                counter += 1

            if curr_node is not None:
                prev_node.next_node = curr_node.next_node
                curr_node = None
            else:
                print("Index out of bound\nLast index is: " + str(counter-1) + "\nQuery value: " +str(key))

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node

    def length_iter(self):  # iterative approach
        counter = 0
        curr_node = self.head
        while curr_node is not None:
            curr_node = curr_node.next_node
            counter += 1
        return counter

    def length_rec(self, node):  # recursive approach
        if node is None:  # base case
            return 0
        else:
            return 1 + self.length_rec(node.next_node)

    def reverse_iter(self): # reverse list order
        # A->B->C to C->B->A
        pass


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append("a")
    linked_list.append("b")
    linked_list.append("c")

    linked_list.prepend("d")
    linked_list.prepend("z")

    linked_list.insert_after(linked_list.head.next_node, "x")  # using pointer to node to insert

    linked_list.delete_node("d")
    linked_list.delete_at_index(1)

    linked_list.print_list()
    print("iterative length: " + str(linked_list.length_iter()))
    print("recursive length: " + str(linked_list.length_rec(linked_list.head)))

