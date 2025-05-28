import random 

#create the random number 
Secret_num = random.randint(1,100)
tries = 0
guess = None

print("--------------Welcome to the guessing game!--------------")
print()
print("Here you are going to pick a number between 1 and 100")
print

while guess != Secret_num:
    try:
        guess = int(input("Guess a number!: "))
        if guess < Secret_num:
            print("Sorry your number is to low")
        elif guess > Secret_num:
            print("Sorry your number is to high")
        elif guess == Secret_num:
            print("You guessed the correct number!")
    except ValueError:
        print("Invalid Input")