"""
Dynamic Array API (similar to C Vector, Java ArrayList, Python List)

value get(i)
set(i, val)
push_back(val)
remove(i)
length size()

arr,capacity,size
"""


# Python can handle this easily with list, but here's the implementation anyway
class DynamicArray:
    def __init__(self, capacity=2):
        self.__arr = [0] * capacity
        self.__size = 0
        if capacity > 0:
            self.__capacity = capacity
        else:
            print("Capacity can't be lower or equal to 0")
            self.__capacity = 2

    def get(self, i):
        if i < 0 or i >= self.__size:
            print('Index out of range')
            return
        return self.__arr[i]

    def set(self, i, val):
        if i < 0 or i >= self.__size:
            print('Index out of range')
            return
        self.__arr[i] = val

    def push_back(self, value):
        if self.__size == self.__capacity:
            new_array = [0] * self.__capacity * 2
            for item in range(1, self.__size):
                new_array[item] = self.__arr[item]
            self.__arr = new_array
            self.__capacity *= 2
        self.__arr[self.__size] = value
        self.__size += 1

    def remove(self, i):  # bug
        if self.__size <= 0:
            print('Dynamic Array is empty')
            return
        if i < 0 or i >= self.__size:
            print("index out of range: max index =", str(self.size()-1) + ", get = ", i)
            return
        for j in range(i, self.__size):
            self.__arr[j] = self.__arr[j + 1]
        self.__size -= 1

    def size(self):
        return self.__size

    def show_info(self):
        print('Array:', self.__arr, "\nSize:", self.__size, "\nCap:", self.__capacity)


if __name__ == '__main__':
    da = DynamicArray(1)
    print(da.size())
    lst = [-1, 0, 1, 2, 3]
    for i in lst:
        da.push_back(i)
    print(da.size())
    print(da.get(4))

    da.show_info()
    for _ in range(da.size()):
        print(da.get(0), end=" ")
        da.remove(0)
    print()
    da.show_info()
