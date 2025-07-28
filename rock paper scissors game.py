import random
# Rock
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]
print("lets play rock paper scissors game!!!")
user_choice=int(input("enter your choice 0 for rock, 1 for paper, 2 for scissors: \n"))
if user_choice>=0 and user_choice<=2:
 print("you chose:")
 print(game_images[user_choice])
computer_choice=random.randint(0,2)
print("computer chose:")
print(game_images[computer_choice])

if user_choice>=3 or user_choice<0:
    print("invalid number")
elif user_choice==0 and computer_choice==2:
    print("you win!!!")
elif computer_choice==0 and user_choice==2:
    print("you lose!!!")
elif computer_choice>user_choice:
    print("you lose!!!")
elif user_choice>computer_choice:
    print("you win!!!")
elif computer_choice==user_choice:
    print("Draw!!!")
