import random
from os import system
from colorama import Fore

num = random.randrange(10)
Guesses = 5

system('cls')


for i in range(1, Guesses+1):
    try:
        guess = int(input(Fore.GREEN + "Enter your guess: "))
    except ValueError:
		    print(Fore.GREEN + "Couldnt convert input to Integer")
		    continue
    if(guess > 10):
        print(Fore.GREEN + "Enter number between 1 to 10: ")
    elif(guess < 10):
        
        if(guess == num):
            print(Fore.GREEN + "Your guess is correct!")
            break
        elif(guess > num and i < Guesses):
            print(Fore.GREEN + "You are close, keep trying lower")
        elif(guess < num and i < Guesses):
            print(Fore.GREEN + "You are close, keep trying higher")

        if(i == Guesses-1):
            print(Fore.GREEN + "This is your last chance")
        elif(i == Guesses and guess != num):
            print(Fore.GREEN + "You Lost!")
            print(Fore.GREEN + "Correct answer was", num)
