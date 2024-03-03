print("Welcome")
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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("You need to help Cap.Jack Sparrow to find GOLD\nIn the journey of finding GOLD there are some choices that Jack Sparrow need to make.\nif he makes right choice he will achive a GOLD if he don't make right choice he will die.")
print("Good Luck")

print("Jack is on crossing, there are two direction left and right, help him to go in a correct direction")
choice=input("Enter your choice left or rigth?: ")
choice=choice.lower()

if choice=="left":
    print("Excellent! you have made a correct choice go ahead.")

    print("Now Jack Sparrow has to make choice to enter in to correct door out of three doors, help him")
    choice2=input("Select a door in which you want to go in door1, door2 or door3?: ")
    choice2=choice2.lower()
    if choice2=="door3":
        print("Great job! Door3 was a correct choice.")

        print("Now Jack is only one step far to get GOLD, make sure he makes correct choice.")
        print("There are two goggles, you need to put one of them on your eye.\ncorrect goggles make you see GOLD\nWrong one will take your eye because its highly poisonous.\nMake your last choice carefully.")
        last_choice=input("Enter your goggles choice goggles on left or right?: ")
        last_choice=last_choice.lower()
        
        if last_choice=='left':
            print("Game over, You picked a wrong goggles.")
        else:
            print("Hurrah!💰💰💰 Jack got the GOLD")

    elif choice2=="door2":
        print("Game over!, Jack went to wrong door, inside door2 there was a tiger and tiger got delicious food. ")
    
    else:
        print("Game over!, there is a cobra inside door1 ")
else:
    print("Game Over!, There is a Devil on this path, Devil kiied the Jack Sparrow. ")

print("Thank you for playing!")


