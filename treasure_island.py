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

#first decision
print("You have come to a fork in the road. \n You can take the shadowy unpaved path to the left or the windy paved path to the right.")
first_adventure = input("Do you want to go left or right?: ").lower().strip()

if first_adventure == "left":
    second_adventure = input("After many hours and miles of walking, you come to a gentle flowing river. \n You can see the Cave of Wonders just beyond the river. \n You are almost to the treasure! \n Do you want to swim or wait?: ").lower().strip()
    if second_adventure == "wait":
        third_adventure = input("Your patience has paid off! A giant flamingo has come to give you a lift to the other side. \n You have finally made it to the Cave of Wonders where you gaze upon three doors. \n Which color door do you want to chance your life on? Red, yellow, or blue?: ").lower().strip()
        if third_adventure == "yellow":
            print("You've won the treasure! Quality time with your family!")
        elif third_adventure == "blue":
            print("Wrong door. You have been eaten by a pack of very adorable, but hungry beasts. GAME OVER.")
        elif third_adventure =="red":
            print("You have been vaporized by a dragon who sneezed. GAME OVER!")
        else:
            print("That's not a door, you immediately implode. GAME OVER!")
    else:
        print("Unfortunately it is Kraken mating season and the sight is so terrible you have a heart attack. GAME OVER!")
else:
    print("You are swept away by a giant sharknado. GAME OVER!")
    
    
                        
