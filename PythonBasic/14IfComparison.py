def max_num(num1, num2, num3):
    if num1 < num2:
        if num2 <= num3:
            max_number = num3
        else:
            max_number = num2
    else:
        if num1 <= num3:
            max_number = num3
        else:
            max_number = num1
    return max_number


print(max_num(33, 2, 5))