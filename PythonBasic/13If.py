is_male = True
is_tall = False

if is_male and is_tall:
    print("I'm a tall male")
elif is_male and not is_tall:
    print("I'm a short male")
elif not is_male and is_tall:
    print("I'm a tall female")
else:
    print("I'm neither male or tall")