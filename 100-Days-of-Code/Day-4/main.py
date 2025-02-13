#Rock, Paper, Scissors Game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose=int(input("What do you choose? 0 for rock, 1 for paper,2 for scissors\n"))
print("Computer choice:")
num=random.randint(0,2)
if num==0:
    print(rock)
elif num==1:
    print(paper)
else:
    print(scissors)

print("My choice:")
if choose==0:
    print(rock)
elif choose==1:
    print(paper)
else:
    print(scissors)

if num ==0:
    if choose==0:
        print("Tie")
    elif choose==1:
        print("You Win")
    else:
        print("You Lose")
elif num==1:
    if choose==0:
        print("You Win")
    elif choose==1:
        print("Tie")
    else:
        print("You Lose")
else:
    if choose==0:
        print("You win")
    elif choose==1:
        print("You lose")
    else:
        print("Tie")
