# Let say the random language use 'g' as all vowels
def translate(text):
    translation = ""
    for letter in text:
        if letter in "AEIOUaeiou":  # If inside this string
            if letter.isupper():
                translation += 'G'
            else:
                translation += 'g'
        else:
            translation += letter
    return translation.capitalize()


print(translate(input("The text: ")))
