
import random

computer = random.choice(["r", "p", "s"])

user = input("Enter r (Rock), p (Paper), s (Scissors): ")

print("Computer:", computer)

if user == computer:
    print("Draw!")

elif user == "r" and computer == "s":
    print("Winner!")

elif user == "p" and computer == "r":
    print("Winner!")

elif user == "s" and computer == "p":
    print("Winner!")

else:
    print("Computer is the winner!")
