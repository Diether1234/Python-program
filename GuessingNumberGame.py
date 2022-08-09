import random
num = random.randint(1, 10)
# print(num)
player = input("Hello what's your name?")
print("Hello", player, "I am thinking of a number from 1 to 10, can you guess? You got 5 tries!")
guesses = 0
while guesses < 5:
    guess =int(input("Try again!"))
    guesses += 1
    print(guesses)
    if guess < num:
        print("It's too low")
    elif guess > num:
        print("It's too high")
    elif guess == num:
        break
if guess == num:
    print("Congrats!")
else:
    print("Ran out tries, try again!")