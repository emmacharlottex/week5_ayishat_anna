# imported random module for random.randint to be applied
import random
# created user variable to add input function for user to be able to enter their choice, added .lower() method to make it case insensitive
user = input('Enter your choice of Rock, Paper or Scissors using R, P or S: ').lower()
# defined the letters which will be recognised as rock, paper, scissors, created them in a list to be able to have them as separate items

allowed_letters = ['r', 'p', 's']

# defined function called user_choice with parameter 'tool'
def user_choice(tool):
# created an if statement to determine which output is shown to the user dependant on which tool they picked
    if tool == 'r':
        print('You have chosen: Rock')
    if tool == 'p':
        print('You have chosen: Paper')
    if tool == 's':
        print('You have chosen: Scissors')
    # returning the value back to the function to use again
    return tool
# created another variable called userchoice to store the result of the function
#userchoice = user_choice(user)

# defined function called computer
def computer():
    # created number variable to use randint method from random module to determine a random integer
    number = random.randint(0, 2)
    # used if statement to determine which number links to which tool, this will print the output to the user showing what the computer has picked
    if number == 0:
        print("Computer's choice of tool: Rock")
        return 'r'
    elif number == 1:
        print("Computer's choice of tool: Paper")
        return 'p'
    elif number == 2:
        print("Computer's choice of tool: Scissors")
        return 's'
# created computer_choice variable to store the result of the computer
#computer_choice = computer()

# created a dictionary of winning outcomes
winning_cases = {"r":"s", "p":"r", "s":"p"}
# created an if statement to state if both user and computer have the same outcome, it will be a draw
# if userchoice == computer_choice:
#     print('You have drawn! Try again')
# # used elif statement that compares the key of the dictionary with the value of the computer choice which has been determined
# #winning_cases["r"]
# elif winning_cases[userchoice] == computer_choice:
#     print('You have won!')
# # if other conditions aren't met, this means the computer has won so else statement is inputted
# else:
#     print("The computer has won!")


score = 0
user_score = 0
computer_score = 0
while score < 5:
# created a while loop to ensure correct letters are used
    while user not in allowed_letters:
        print('Invalid Response! Please use R, P, S to select your tool')
        # gave input again to allow the user to try again if they input wrong letter
        user = input('Enter your choice of Rock, Paper or Scissors using R, P or S: ').lower()
    userchoice = user_choice(user)
    computer_choice = computer()
    if userchoice == computer_choice:
        print('You have drawn! Try again')
# used elif statement that compares the key of the dictionary with the value of the computer choice which has been determined
# winning_cases["r"]
    elif winning_cases[userchoice] == computer_choice:
        user_score += 1
        score = user_score
        print('You have won!')
# if other conditions aren't met, this means the computer has won so else statement is inputted
    else:
        computer_score += 1
        score = computer_score
        print("The computer has won!")
    print(f'User Score: {user_score}')
    print(f'Computer Score: {computer_score}')
    user = input('Enter your choice of Rock, Paper or Scissors using R, P or S: ').lower()


print(f'User Score: {user_score}')
print(f'Computer Score: {computer_score}')
