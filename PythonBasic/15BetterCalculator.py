def calculator(num1, operator, num2):
    if operator == '-':
        return num1-num2
    elif operator == '+':
        return  num1+num2
    elif operator == '*':
        return  num1*num2
    elif operator == '/':
        return  num1/num2
    else:
        print("Invalid operator")


num1 = float(input("First number: "))
operator = input("Operator: ")
num2 = float(input("Second num: "))

print(calculator(num1, operator, num2))