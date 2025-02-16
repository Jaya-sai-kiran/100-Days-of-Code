#Number Guessing game
import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
number=random.randint(1,100)
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts=0
if difficulty == "easy":
    attempts=10
else:
    attempts=5
for i in range(attempts):
    print(f"You have {attempts-i} attempts remaining to guess the number.")
    guess_number=int(input("Make a guess: "))
    if guess_number>number:
        print("To high")
    elif guess_number<number:
        print("To low")
    else:
        print("You win")
        break
    if i<attempts-1:
        print("Guess again")
    else:
        print("You lose")