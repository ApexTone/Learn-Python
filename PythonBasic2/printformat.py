from datetime import datetime

if __name__ == "__main__":
    # Normal .format()
    first_name = 'Slim'
    last_name = 'Shady'
    sentence = 'My name is {} {}'.format(first_name, last_name)
    print(sentence)

    person = {'name': 'John', 'age': '23'}
    sentence = 'My name is {} and I am {} years old'.format(
        person['name'], person['age'])
    print(sentence)

    # F-string (formatted string) => like JS template string
    sentence = f'My name is {first_name.upper()} {last_name.upper()}'
    print(sentence)

    # must use difference quote (single/double)
    sentence = f"My name is {person['name']} and I am {person['age']} years old"
    print(sentence)

    a = 4
    b = 11
    calculation = f"{a} times {b} is equal to {4*11}"
    print(calculation)

    # leading zeros
    for n in range(1, 11):
        # format for 2 digits zero padding (this doesn't work in VSCode)
        sentence = f'The value is {n:02}'
        print(n)

    pi = 3.14159265
    # 4 digits floating point with proper rounding
    sentence = f'Pi is equal to {pi:.4f}'
    print(sentence)

    bday = datetime(1990, 1, 1)
    # output in string-ish style (month day, year)
    sentence = f'John has birthday on {bday:%B %d, %Y}'
    print(sentence)
