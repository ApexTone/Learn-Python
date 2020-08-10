import random
from Week2.PriorityQueue.binary_max_heap import BinaryMaxHeap


def heap_sort(to_sort):  # this one sort in descending order
    heap = BinaryMaxHeap(len(to_sort)+1)
    for item in to_sort:
        heap.insert(item)
    # print('Heap:', heap.heap)
    for i in range(len(to_sort)):
        to_sort[i] = heap.extract_max()
    return to_sort


def stress_test():
    while True:
        lst = list()
        for _ in range(50):
            lst.append(random.randint(-1000, 1000))
        random.shuffle(lst)
        print('List before sorting:', lst)
        h1 = heap_sort(lst)
        bheap = BinaryMaxHeap()
        h2 = bheap.heap_sort(lst)
        h2.reverse()
        print('Normal:', h1)
        print('With built-in:', h2)
        if h1 != h2:
            break
        else:
            print('OK')


if __name__ == '__main__':
    stress_test()
