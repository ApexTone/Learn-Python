if __name__ == '__main__':
    r = range(10)  # [0, 10)
    print(r)  # Show range
    print(list(r))  # Print all value in range
    print(len(r))
    print(type(r))

    r1 = range(5, 20)  # [5, 20)
    print(list(r1))

    r2 = range(5, 20, 2)  # Increment by 2
    print(list(r2))

    r3 = range(10, 0)
    print(list(r3))  # List only work in increasing order except...

    r4 = range(10, 0, -1)
    print(list(r4))

    r5 = range(-1, -10, -1)
    print(list(r5))

    n = range(1, 11)
    print(sum(n))  # sum in range

    
