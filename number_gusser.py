import random

top_of_range =input("Type a number range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number greater than zero next time.")
        quit()
else:
    print("Please enter a number next time.")
    quit()

random_no = random.randint(0,top_of_range)
guess = 0

while True:
    guess = guess + 1
    user_guess = input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please Enter a number next time.")
        continue

    if user_guess == random_no:
        print("There you are.You guessed it right.")
        break
    elif user_guess > top_of_range:
        print("Out of range!")
    elif user_guess > random_no:
        print("You are above the number!")
    else:
        print("You are below the number!")

print("You got it in %d guesses.\nWell Played:)"%(guess))