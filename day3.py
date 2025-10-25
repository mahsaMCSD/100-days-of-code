print('''   *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
                     ''')

print("welcome to Island")
print("your mission is to find the treasure")
choice1=input('you are in cross road where do u want to go?"left" or right\n').lower()
print(choice1)
if choice1=="left":
 choice2=  input('"there is an island in the middle of the lake type "wait" to wait for boat'
         ' type "swim" to swim the cross"\n').lower()
 if choice2=="wait":
    choice3=input("you arrived at the island unharmed there is a hause with 3 doors. one Red, one Yellow, one blue "
      "which one u wanna choose\n").lower()
    if choice3=="red":
        print("its room full of fire.game over")
    elif choice3=="yellow":
        print("you found the treasure u win")
    elif choice3=="blue":
        print("you entered depressed room. game over")
    else:
        print("you chose a door that doesnt exist. game over")
 else :
    print("you got attacked buy angry fish. game over")
else :
    print("you fell into the hole game over")
