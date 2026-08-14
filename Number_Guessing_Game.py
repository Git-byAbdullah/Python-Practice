import random
play = "yes"
while play=="yes":

    n=random.randint(1,100)
    guesses=0
    a=-1
    print("Welcome to Number Guessing Game...\nGuess a number between 1 to 100")
    while (a!=n):
            a=int(input("Guess the number: "))
            guesses+=1
            if(a>n):
             print("Lower Number Please.")
            if(a<n):
             print("Larger Number Please.")
    print(f"Congradulations! \nYou Correctly Guess {n} in {guesses} Attempts ")
    play = input("Do you want to play again? yes/no: ").lower()
print("Thanks for playing!")