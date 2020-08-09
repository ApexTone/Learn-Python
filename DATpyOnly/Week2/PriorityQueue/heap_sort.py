from Week2.PriorityQueue.binary_max_heap import BinaryMaxHeap


def heap_sort(to_sort):
    heap = BinaryMaxHeap(len(to_sort)+1)
    for item in to_sort:
        heap.insert(item)
    for i in range(len(to_sort)):
        to_sort[i] = heap.extract_max()
    return to_sort


if __name__ == '__main__':
    lst = [8, 0, 5, 3, -4, 99, -10, -87]
    print(heap_sort(lst))
