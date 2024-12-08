print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

q1 = input("You've come to a cross road. Where do you want to go? Left or Right?").lower()

if q1 == "left":
    q2 = int(input("You have come to the shore and see an Island not far off. "
                   "Do you want to swim across or wait? Type 1 for swim or 2 for wait."))

    if q2 == 2:
        q3 = input("You were taken across by a fisherman and arrived at a building with 3 doors. "
                   "Red, Blue, and Yellow. Which color door do you choose to walk through?").lower()
        if q3 == "red":
            print("The door locks behind you and you are incinerated. GAME OVER!")
        elif q3 == "blue":
            print("The door locks behind you and a towering Minotaur rips you in half. GAME OVER!")
        elif q3 == "yellow":
            print("You walk in to find an uncountable amount of riches! Congratulations! YOU WIN!")
        else:
            print("GAME OVER!")
    else:
        print("You were eaten by a shark. GAME OVER!")

else:
    print("You fell into a hole. GAME OVER!")
