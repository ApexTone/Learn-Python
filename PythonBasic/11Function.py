# Don't like JAVA, the function name will always be lowercase
# Declare the function


def say_hi(username, userage):
    print("Hi " + username + ", you are " + str(userage))


# Call the function
name = input("Your name: ")
age = input("Your age: ")
say_hi(name, age)
