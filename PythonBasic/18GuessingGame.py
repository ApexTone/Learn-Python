secret_word = "secret"
guess = ""
strikes = 0
limit = 3
lose = False

while guess != secret_word:
    if strikes < limit:
        guess = input("Guess the word: ")
        strikes += 1
    else:
        lose = True
        break

if not lose:
    print("Yay! You're correct. The secret word is "+secret_word +".")
else:
    print("You lose! The word is " + secret_word +".")