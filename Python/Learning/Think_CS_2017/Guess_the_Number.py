import random
x = ""
while x == "":
    number = random.randrange(0, 101)
    print("Try to guess a number between 0 and 100!")
    guess = int(input("Enter your first guess:"))
    while guess != number:
        if guess > number:
            print("Too high!!!")
        if guess < number:
            print("Too low!!!")
        guess = int(input("Good guess... but try again:"))
    x = str(input("Good game! Press enter to play again\n or anything else to quit:"))
