import random
print("Hello! Lets play rock, paper, scissors")
n = ["rock", "paper", "scissors"]
while True:
    comp = n[random.randint(0,2)]
    # print(comp)
    player= input("rock, paper or, scissors?: ").lower()
    print(player)
    if comp == player:
        print("Tie!")
    elif player == "rock":
        if comp == "paper":
            print("You loose!")
        else:
            print("You won")
    elif player == "paper":
        if comp == "scissors":
            print("You loose!")
        else:
            print("You won!")
    elif player == "scissors":
        if comp == "rock":
            print("You loose!")
        else:
            print("You won!")
            
