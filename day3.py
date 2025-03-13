#Jogo de achar o tesouro perdido usando if e else
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

choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake.\n'
                    'Type "wait" to wait for a boat.\n'
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
              "There is house with 3 doors. One red, "
              "one yellow and one blue.\n"
              "Which colour do you chose?\n").lower()
        if choice3 == "red":
            print("You fall into a deep abyss, darkness swallowing you as the air rushes past. Game Over.")
        elif choice3 == "yellow":
            print("A giant tiger eats your head. Game over.")
        elif choice3 == "green":
            print("You found a secret door. Who is that at the back of the room? A wish fairy!✨"
                  "Congratulations! You have earned 3 wishes for anything you desire. Secret good ending.")
        elif choice3 == "blue":
            print('Congratulations! You found the treasure. Wait...\n'
                  'You open the chest and... is that Quico\'s hat?\n'
                  'There\'s a note inside: "The real treasure is the friends we make along the way.\n'
                  'You didn’t make any friends, and apparently, you didn’t get any money either.\n'
                  'Good ending... I guess?🤷‍♂️')
        else:
            print("You tripped and hurt your little toe, and now you can't walk anymore. Game Over.")

    else:
        print("You got attacked by an angry trout. Game Over.")
elif choice1 == "right":
    choice2_1 = input('You got lost in a mysterious forest. '
                      'What do you do? \n'
                      'Type "explore" to explore the forest and find a way out.\n'
                      'Type "climb" to climb a tree for a better view.\n')
    if choice2_1 == "explore":
        print("You wander lost in the forest until a mysterious man appears. Wait... he's a wizard 🧙‍♂️\n"
              "He gets angry at you for not wearing a stylish hat, in fact, you're not wearing any hat at all!\n"
              "How embarrassing 😳\n"
              "The wizard, no longer wanting to look at you, teleports you to a prison 🏰\n"
              "where you find other people who were imprisoned for the same reason.\n"
              "At least you're not alone anymore 🤷‍♂️. "
              "No Hat Ending 🎩👎")
    elif choice2_1 == "climb":
        print("You climb a tree to get a better view of where you are.\n"
              "Suddenly, you feel a sting on your arm... "
              "It was a peculiar spider 🕷️\n"
              "It doesn't take long before you feel your body changing...\n"
              "You've become Spider-Man 🕸️, and now it's your duty to protect the city!\n"
              "You leave the forest behind and forget about the treasure,\n"
              "because now you're the friendly neighborhood Spider-Man! 🏙️💪\n"
              "Friendly Spider-Man Ending. 🕷️🎉")
    else:
        print("You pooped your pants and left with embarrassment 😳💩. Game Over.")
else:
    print("You got lost in the dark. Game Over.")



