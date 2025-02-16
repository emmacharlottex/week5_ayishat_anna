
import random
user = input('Enter your choice of Rock, Paper or Scissors using R, P or S: ').lower()

allowed_letters = ['r', 'p', 's']
while user not in allowed_letters:
        print('Invalid Response! Please use R, P, S to select your tool')

        user = input('Enter your choice of Rock, Paper or Scissors using R, P or S: ').lower()

def user_choice(tool):
   # r = 'Rock'
   # p = 'Paper'
   # s = 'Scissors'
    if tool == 'r':
        print('You have chosen: Rock')
    if tool == 'p':
        print('You have chosen: Paper')
    if tool == 's':
        print('You have chosen: Scissors')
    return tool

user_choice(user)


def computer(number):
    number = random.randint(0, 2)
    if number == 0:
        print("Computer's choice of tool: Rock")
    if number == 1:
        print("Computer's choice of tool: Paper")
    if number == 2:
        print("Computer's choice of tool: Scissors")
    return number

computer(6)

# while loop needs completing to keep game playing

if user_choice == computer:
    print('You have drawn! Try again')
user = input('Enter your choice of Rock, Paper or Scissors using R, P or S: ').lower()









