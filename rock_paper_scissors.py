
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

userchoice = user_choice(user)


def computer():
    number = random.randint(0, 2)
    if number == 0:
        print("Computer's choice of tool: Rock")
        return 'r'
    elif number == 1:
        print("Computer's choice of tool: Paper")
        return 'p'
    elif number == 2:
        print("Computer's choice of tool: Scissors")
        return 's'

computer_choice = computer()

# while loop needs completing to keep game playing
#score =0
winning_cases = {"r":"s", "p":"r", "s":"p"}

if userchoice == computer_choice:
    print('You have drawn! Try again')
#winning_cases["r"]
elif winning_cases[computer_choice] == userchoice:
    print("The computer has won!")
else:
    print('You have won!')

#user = input('Enter your choice of Rock, Paper or Scissors using R, P or S: ').lower()










