# for 0-based array see Week3 Heap sort, Final remark
# can also be modified to make it BinaryMinHeap
# for d-ary Heap (each node on every level except last one has d children) will run faster for some action O(logd n)

class BinaryMaxHeap:  # complete binary tree with parent node's value >= child nodes' value
    def __init__(self, max_size=64):
        self.max_size = max_size  # maximum heap size possible
        self.size = 0  # current heap size
        self.heap = [float('-inf')] * self.max_size  # heap representation in array

    # index of ... of node at index i [index start from 1]
    def parent(self, i):
        return i//2

    def left_child(self, i):
        return 2*i

    def right_child(self, i):
        return 2*i+1

    def sift_up(self, i):
        while i > 1 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def sift_down(self, index):
        # print("Current heap:", self.heap)
        max_index = index
        left = self.left_child(index)
        # print("Max:", max_index, "Left:", left)
        if left <= self.size and self.heap[left] > self.heap[max_index]:
            max_index = left
        right = self.right_child(index)
        # print("Max:", max_index, "Right:", right)
        if right <= self.size and self.heap[right] > self.heap[max_index]:
            max_index = right
        if index != max_index:
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            self.sift_down(max_index)

    def insert(self, priority):
        if self.size == self.max_size:
            print("heap is full")
            return  # error
        self.size += 1
        self.heap[self.size] = priority
        self.sift_up(self.size)
        # print("inserted:", self.h)

    def extract_max(self):
        result = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.sift_down(1)
        return result

    def remove(self, i):
        self.heap[i] = float('inf')
        self.sift_up(i)
        self.extract_max()

    def change_priority(self, i, priority):
        old_priority = self.heap[i]
        self.heap[i] = priority
        if priority > old_priority:
            self.sift_up(i)
        else:
            self.sift_down(i)

    def build_heap(self, array):
        # comment input out for stress testing
        choice = input("This action will replace your old heap, would you like to continue? Y/n : ")
        if choice == 'Y':
            self.max_size = len(array)
            self.size = len(array)
            self.heap = [None]+array
            for i in range(self.size//2, 0, -1):
                self.sift_down(i)
        else:
            return

    def heap_sort(self, array):  # sort in ascending order -> this one use less mem than the stand-alone function one
        self.build_heap(array)
        for _ in range(len(array)-1):
            self.heap[1], self.heap[self.size] = self.heap[self.size], self.heap[1]
            self.size -= 1
            self.sift_down(1)
        return self.heap[1:]

    def partial_sort(self, array, k):  # output first k elements in descending order
        self.build_heap(array)
        lst = list()
        for i in range(1, k+1):
            lst.append(self.extract_max())
        return lst
