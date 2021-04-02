import time


class DisjointSetNaive:
    def __init__(self):  # use starting index as 1
        self.smallest = [float('inf')]*100000  # smallest will store 'id' of the set using smallest number in set

    def make_set(self, i):
        self.smallest[i] = i

    def find(self, i):
        return self.smallest[i]

    def union(self, i, j):
        i_id = self.smallest[i]
        j_id = self.smallest[j]
        if i_id == j_id:
            return
        m = min(i_id, j_id)
        for k in range(1, len(self.smallest)):  # take linear time (edited from len(self.smallest)+1)
            if self.smallest[k] in [i_id, j_id]:
                self.smallest[k] = m


class DisjointSet:  # use tree-like structure to store data
    def __init__(self):
        self.parent = [float('inf')]*100000
        self.rank = [0]*100000  # store tree height

    def make_set(self, i):
        self.parent[i] = i  # root is it own parent
        self.rank[i] = 0

    def find(self, i):  # return root(id) -> O(tree height = log n)
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union(self, i, j):  # append shorter tree to taller tree's root for faster performance
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:  # same root -> no union
            return
        if self.rank[i_id] > self.rank[j_id]:  # append shorter tree to taller tree
            self.parent[j_id] = i_id  # tree height don't increase
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:  # adding tree height
                self.rank[j_id] = self.rank[j_id] + 1


class CompressedDisjoint(DisjointSet):  # reduce time to almost constant!
    # rank[] >= tree height
    def find(self, i):  # this method will shorten the tree height by a lot
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])  # find+change the root recursively
        return self.parent[i]


def test_disjoint(choice=0):
    if choice == 0:
        network = DisjointSetNaive()
        method = 'Naive'
    elif choice == 1:
        network = DisjointSet()
        method = 'Efficient'
    elif choice == 2:
        network = CompressedDisjoint()
        method = 'Path Compression'
    else:
        print('Invalid choice (0=naive, 1=eff, 2=compressed)')
        return
    print(f'Start test:{method}'.center(50, '-'))
    start = time.time()
    for device in range(1, 7):
        network.make_set(device)
    network.union(2, 4)
    network.union(4, 5)
    network.union(3, 1)
    for i in range(1, 7):
        print(network.find(i))
    end = time.time()
    print(f'Time used:{end-start}'.center(50, '-'))


def quiz1():
    ds = DisjointSetNaive()
    for i in range(1, 13):
        ds.make_set(i)
    ds.union(2, 10)
    ds.union(7, 5)
    ds.union(6, 1)
    ds.union(3, 4)
    ds.union(5, 11)
    ds.union(7, 8)
    ds.union(7, 3)
    ds.union(12, 2)
    ds.union(9, 6)
    print(ds.find(6))
    print(ds.find(3))
    print(ds.find(11))
    print(ds.find(9))


def quiz2():
    ds = DisjointSet()
    for i in range(1, 13):
        ds.make_set(i)
    ds.union(2, 10)
    ds.union(7, 5)
    ds.union(6, 1)
    ds.union(3, 4)
    ds.union(5, 11)
    ds.union(7, 8)
    ds.union(7, 3)
    ds.union(12, 2)
    ds.union(9, 6)
    print(ds.parent[:13])


if __name__ == '__main__':
    test_disjoint(0)
    test_disjoint(1)
    test_disjoint(2)
    quiz2()
