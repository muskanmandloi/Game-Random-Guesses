# GAME--Random Number Guess 

import random
randNumber = random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("enter your guess:"))
    guesses += 1
    if(userGuess == randNumber):
        print("You guessed right!!!!!")
    else:
         if(userGuess > randNumber):
             print("you guessed it wrong! enter smaller number")
         else:
                print("you guessed  wrong! enter larger number")

print(f"you guessed the number {guesses} guesses")
with open ("hiscore.txt","r") as f:
                     hiscore=int(f.read())

if(guesses<hiscore):
   print("you have just broken the high score!!!!!!!!")
with open("hiscore.txt","w") as f:
                        f.write(str(guesses))