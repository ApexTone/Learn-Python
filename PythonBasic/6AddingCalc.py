num1 = input("Enter number: ")
num2 = input("Enter number: ")

# By default, everything is string in python
# result = num1+num2 # Will result in string concatenation
# result = int(num1)+int(num2)
result = float(num1)+float(num2) # Make it more universal for number input

print(result)