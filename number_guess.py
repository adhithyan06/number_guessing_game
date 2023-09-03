# Number guessing game using python

import random
import math

lowernumber = int(input("Enter Lower limit Number: "))
uppernumber = int(input("Enter Upper limit Number: "))

x = random.randint(lowernumber, uppernumber)
print(
    "\n\tYou've only ",
    round(math.log(uppernumber - lowernumber + 1, 2)),
    " chances to guess the Number!\n",
)

count = 0

while count < math.log(uppernumber - lowernumber + 1, 2):
    count += 1

    guess = int(input("Guess the number: "))

    if x == guess:
        print("Congratulations You guessed it in ", count, " tries Hooray!!")
        break
    elif x > guess:
        print("You have guessed a smaller number!")
    elif x < guess:
        print("You have guessed a higher number!")

if count >= math.log(uppernumber - lowernumber + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter luck next time :(")
