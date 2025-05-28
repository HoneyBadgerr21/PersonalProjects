import random

print("------------Welcome to Rock Paper Scissor------------")
print("")

print("Below are the options for this game!")
print("1. Rock")
print("2. Paper")
print("3. Scissor")
print("")

UserInput = int(input("Please pick a number: "))

random_num = random.randint(1, 3)

if UserInput == 1 and random_num == 1:
    print("Its a draw! Opponent selected Rock")
elif UserInput == 1 and random_num == 2:
    print("You lose. Opponent selected Paper")
elif UserInput == 1 and random_num == 3:
    print("You win! Opponent selected Scissors")
elif UserInput == 2 and random_num == 1:
    print("You win! Opponent selected Rock")
elif UserInput == 2 and random_num == 2:
    print("Its a draw. Opponent selected Paper")
elif UserInput == 2 and random_num == 3:
    print("You lose. Opponent selected Scissors")
elif UserInput == 3 and random_num == 1:
    print("You lose. Opponent selected Rock")
elif UserInput == 3 and random_num == 2:
    print("You win! Opponent selected Paper")
elif UserInput == 3 and random_num == 3:
    print("Its a draw. Opponent selected Scissors")
else:
    print("Please select a number from the menu (1-3)")

#just testing  to see if its uploading to github
# This is a simple Rock Paper Scissor game in Python and seems to be working fine.