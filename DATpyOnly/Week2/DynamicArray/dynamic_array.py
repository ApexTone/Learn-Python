"""
Dynamic Array API (C Vector, Java ArrayList, Python List)

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

    def get(self, i): # O(1)
        if i < 0 or i >= self.__size:
            print('Index out of range')
            return
        return self.__arr[i]

    def set(self, i, val):  # O(1)
        if i < 0 or i >= self.__size:
            print('Index out of range')
            return
        self.__arr[i] = val

    def push_back(self, value):  # O(n)
        """
        Amortized analysis
        Aggregate Method: like average of each operation (brute-force sum)
            Cost(n operation)/n => O(n)/n => O(1)
        Banker's Method: charge 'extra' for cheap operations and use that to 'pay' for expensive operations (tokens)
            Charge 3 for each insertion, 1 coin is the raw cost for insertion
            Resize: pay for moving elements by coins
            Place a coin to newly-inserted element and another coin at capacity/2 element
        Physicist's Method: define a potential function that map states of DS to integers (potential function)
            f(H0) = 0, f(Ht) >= 0
            amortized cost for operation t = Ct + f(H0) - f(Ht-1)
            sum of amortized costs (n)= Sum(c1,cn) - f(H0) + f(Hn) = Sum(c1,cn) + f(Hn)
            n calls to push_back -> f(x) = 2 * size - capacity -> f(H0) = 0, f(Hi) > 0 is true
            without resizing: 1 + (2*sizei - capi) - (2*sizei-1 - capi-1) = 1+ 2*(sizei - sizei-1)
            with resizing: sizei + 2 - k = k+1+2-k = 3 (when k=sizei-1=capi-1)
        """
        if self.__size == self.__capacity:
            new_array = [0] * self.__capacity * 2  # double the size since it uses the shortest time and it's efficient
            for v in range(1, self.__size):
                new_array[v] = self.__arr[v]
            self.__arr = new_array
            self.__capacity *= 2
        self.__arr[self.__size] = value
        self.__size += 1

    def remove(self, i):  # O(n)
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
    for item in lst:
        da.push_back(item)
    print(da.size())
    print(da.get(4))

    da.show_info()
    for _ in range(da.size()):
        print(da.get(0), end=" ")
        da.remove(0)
    print()
    da.show_info()
