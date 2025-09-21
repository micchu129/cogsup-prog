"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

from random import randint
import time

def check_int(s):
    """ Check if string 's' represents an integer. """
    # Convert s to string
    s = str(s) 

    # If first character of the string s is - or +, ignore it when checking
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    
    # Otherwise, check the entire string
    return s.isdigit()

#target guess inverted from original code
def input_integer(prompt): 
    """ Asks user for an integer input. If valid, the string input is returned as an integer. """
    target = input(prompt) # Ask the user for the target number in their mind
    while not (check_int(target) and 1 <= int(target) <= 100): # Repeat until the user inputs a valid integer in valid number ranges
        print('Please, enter a n integer number between 1-100') #also prompting the user a valid number range
        target = input(prompt)  
    return int(target)

# begin guessing game
print("Let's Play a Game! Please think of a number between 1 and 100 and input it below... I will try to guess it!")

#asks user for a number between 1-100
target = input_integer("Pick a number... any number (as long as its between 1 and 100): ")

low, high = 1, 100 #adding upper and lower bounds for some rudimentary logic
guess = randint(low, high) #computer genenrates random number as guess

print("Ready? All right let us begin!")
time.sleep(1) #slow the program a little so it doesn't seem as fast..
print(".....")
time.sleep(1)

while guess != target: #repeat until correct
    time.sleep(1)
    print("I guess the number is...") #hard coding some 'thinking time'
    print(str(guess) + "!")
    time.sleep(1)
    if guess < target:
        print("Hmm... something tells me your number is bigger...")
        low = guess + 1 #narrows lower range
        guess = randint(low,high) #computer genenrates random number, but now with a new minimum
    else:
        print("A fairy told me your number is smaller")
        high = guess - 1 #narrows upper range
        guess = randint(low,high) #computer genenrates random number, but now with a new minimum
    time.sleep(1)
    print("Lets try again...")
    print("------------")
    print("")
    time.sleep(0.5) #slow the program a little so it doesn't seem as fast..

print("I guess the number is " + str(guess) + "!")
time.sleep(1)
print("DIING DING, I knew it your nunber is " + str(target) +'!')