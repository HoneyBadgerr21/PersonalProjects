import random 

#create the random number 
Secret_num = random.randint(1,100)
tries = 0
guess = None

print("--------------Welcome to the guessing game!--------------")
print()
print("Here you are going to pick a number between 1 and 100")
print()

while guess != Secret_num:
    try:
        guess = int(input("Guess a number!: "))
        if guess < Secret_num:
            print("Sorry your number is to low")
        elif guess > Secret_num:
            print("Sorry your number is to high")
        else:
            print("You guessed the correct number!")
    except ValueError:
        print("Invalid Input")

#things i want to add 
#Bonus Features to Add (as you go)

    #Guess Limit
    #Add a maximum number of guesses before the game ends.

    #Difficulty Levels
    #Let players choose Easy (1–10), Medium (1–50), Hard (1–100).

    #Play Again Option
    #Ask the user if they want to play again after finishing.

    #Score Tracker or High Score
    #Save the best score across rounds (in memory or a file).

    #Hints
    #Add warmer/colder hints if they're getting closer.
