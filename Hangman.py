import random
print("Hangman")
name = input("Hello! What's your name?")
print("Hello", name, "Goodluck!")
words = ["Run", "sleep", "found", "get", "shocked", "confusion", "wonderful", "problem", "trouble", "trap"]
word = random.choice(words)
print(word)
print("Can you guess what word this is?")
guesses = ""
turns = 5
while turns>0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            failed +=1 
            print("___")  
    if failed == 0:
        print("You guessed the right word! Congrats.")
        break

    guess = input("Guess the character!")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("wrong, you only got", turns,"guesses left")
        if turns == 0:
            print("You loose!")

