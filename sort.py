def merge(array1, array2):
    answer = list()
    while len(array1) > 0 and len(array2) > 0:
        buffer1 = array1[0]
        buffer2 = array2[0]
        if buffer1 <= buffer2:
            answer.append(buffer1)
            array1.pop(0)
        else:
            answer.append(buffer2)
            array2.pop(0)
    while len(array1) > 0:
        answer.append(array1.pop(0))
    while len(array2) > 0:
        answer.append(array2.pop(0))
    return answer


def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array
    middle = n//2
    b_array = merge_sort(array[:middle])
    c_array = merge_sort(array[middle:])
    array_sorted = merge(b_array, c_array)
    return array_sorted


if __name__ == "__main__":
    array = list(map(int, input().split()))
    print(merge_sort(array))
