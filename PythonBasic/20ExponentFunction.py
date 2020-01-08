def exponential(base_number, exponential_num):
    result = 1
    for i in range(exponential_num):
        result *= base_number
    return result


base = int(input("Base: "))
exp = int(input("Exponent: "))
print(exponential(base, exp))