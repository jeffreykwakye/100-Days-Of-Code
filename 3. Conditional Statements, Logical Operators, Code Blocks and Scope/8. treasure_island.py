"""
Let's go treasure hunting (Like in Treasure Island). 
What more can I say. Let's Go!!!
"""
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

start_point = input('You are at a crossroad. Turn left or right to begin your journey. Type "left" to turn left or "right" to turn right: ').lower()

if start_point == "left":
    print('There is a river ahead. There is a castle at the other side of it. Will you "wait" for a boat to carry you across or "swim" across?')
    river_crossing = input('Enter "wait" to wait for boat or "swim" to swim across: ').lower()

    if river_crossing == "wait":
        print("A boat arrives to carry you across safely. You enter the castle.")
        print("You come to a hallway with three (3) doors.")
        print('The doors are "Red", "Blue" and "Yellow" in colour. Which door will you open to enter?') 

        select_door = input('Enter "Red" to select the Red Door, "Blue" to select the Blue Door and "Yellow" to select the Yellow Door: ').lower()

        if select_door == "red":
            print("You walk into a room as hot as hell fire and you melt away. Game Over") 
        elif select_door == "blue":
            print("You enter a room that leads to the depths of the ocean and you drown. Game Over.")
        elif select_door == 'yellow':
            print("You enter a room with gold and other treasures as far as the eyes can see.")
            print("Congratulations. You Won!!!")
        else:
            print("A giant pillar falls on you. You are squished to bits. Game Over.")
    else:
        print("You are violently eaten by crocodiles. Game Over.")
else: 
    print("You come to a cliff and fall off it. Game Over")
    




