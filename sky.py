import random

print("Welcome to play sky game!!!")

moon =('''    _.._
       .' .-'`
      /  /
      |  |
      \  \
        '._'-._
          ```''')

sun = ('''  ;   :   ;
   .   \_,!,_/   ,
    `.,'     `.,'
     /         \
~ -- :         : -- ~
     \         /
    ,'`._   _.'`.
   '   / `!` \   `
      ;   :   ;  ''')

star = ('''  ,
__/ \__
\     /
/_   _\
  \ /
   ''')

rainbow = (''' _.-""""
    ,' _-""""
   / ,'.-'"""
  | / / ,'"""
 | | | | ,'"`
 | | | | |''')

game_images = [moon, sun, star, rainbow]
user_choice = int(input("What do you choose? 0 for moon 1 for sun 2 for star 3 for rainbow : \n"))
print(game_images[user_choice])

computer_choice = random.randint(0,3)
print("Computer chose: ")
print(game_images[computer_choice])

if user_choice >= 4 or user_choice < 0:
    print("You lost!!! Invalid number")
elif user_choice == 0 and computer_choice == 2:
    print("You created the night sky!!! You WON!!!")
elif user_choice == 2 and computer_choice == 0:
    print("You created the night sky!!! You WON!!!")
elif user_choice == 1 and computer_choice == 3:
    print("You created the day sky!!! You WON!!! ")
elif user_choice == 3 and computer_choice == 1:
    print("You created the day sky!!! You WON!!! ")
elif user_choice > computer_choice:
    print("You could not create the sky!!! You Lost!!!")
elif user_choice < computer_choice:
    print("You could not create the sky!!! You Lost!!!")
elif user_choice == computer_choice:
    print("Its a DRAW!!!")