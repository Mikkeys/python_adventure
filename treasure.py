print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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



q1 = input("You have arrived at an crossroad. Do you want to go left or right? type 'left' or 'right'\n").lower()
if q1 == "left":
    q2 = input("You find youself standing on a shore. Do you wait for a boat or try to swim? type 'wait' to wait on a boat, or 'swim' to swim across\n").lower()
    if q2 == "wait":
        q3 = input("You arrive at shore, there you spot a house with 3 doors, one yellow, one blue and one red. Choose what color door you'd like to enter.\n").lower()
        if q3 == "yellow":
                print("You find the treasure, you win!")
        elif q3 == "green":  
                print("The room is filled with poison. \nGame Over")
        elif q3 == "red":  
            print("You fall into a pool of lava. \nGame Over")
        
        else:
                print("You chose a door that does not exist. \nStart again!")
    else:
        print("You get eaten by a trout. \nGame Over")
else:
    print("You fall into a hole. \nGame Over")