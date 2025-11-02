import random

rock='''
 _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors='''
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
gameImages=[rock,scissors,paper]
userChoosed=int(input("what do u chose ? type 0 for Rock, 1 for Paper, 2 for scissors.\n"))

if userChoosed>=0 and userChoosed<=2:
 print(f"you choosed {gameImages[userChoosed]}")
computerChoosed = random.randint(0,2)
print(f"computer chose {gameImages[computerChoosed]}")

if userChoosed > 3 or userChoosed < 0:
    print("invalid input, you loose")
elif userChoosed==0 and computerChoosed==2:
    print("you win")
elif computerChoosed==0 and userChoosed==2:
    print("you loose")
elif computerChoosed > userChoosed:
    print("you lose")
elif userChoosed > computerChoosed:
    print("you win")
elif userChoosed==computerChoosed:
    print("You equal!")


