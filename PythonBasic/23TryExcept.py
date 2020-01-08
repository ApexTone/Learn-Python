# Like try/catch error handling

try:
    cursed_value = 10/0  # Produce ZeroDivisionError
    number = int(input("Enter a number: "))  # User might try input string here
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
except:  # Generic exception
    print("Something wrong")