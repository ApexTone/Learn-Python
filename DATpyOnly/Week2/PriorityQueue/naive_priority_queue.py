"""
Priority Queue API (C priority_queue, Java PriorityQueue, Python heapq)

insert(item)
item extract_max()
------------------------------
remove(item)
item get_max()
change_priority(item,priority)
"""


class NaivePriorityQueue:  # other naive methods (sorted array and sorted list) have some trade-off differ from this one
    def __init__(self):
        self.lst = list()

    def insert(self, item):
        self.lst.append(item)

    def extract_max(self):
        max_elem = max(self.lst)
        self.lst.remove(max_elem)
        return max_elem


if __name__ == '__main__':
    pq = NaivePriorityQueue()
    pq.insert(5)
    pq.insert(6)
    print(pq.extract_max())
    pq.insert(10)
    pq.insert(-1)
    pq.insert(3)
    print(pq.extract_max())