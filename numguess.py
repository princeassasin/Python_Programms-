#!/usr/bin/env python
"""numguess.py, by Sriram Sountharapandian Mathivanan, 29-06-2016
This program guess random number between 1 to 100."""

import random 
def main():
	print "guess a number between 1 an 100"
	randomNumber = random.randint(1,100)
	found = False          # flag to see if they have guessed it
	while not found:
		userGuess = input("Your guess: ")
		if userGuess == randomNumber:
			print "You got it!!"
			found = True
		elif userGuess > randomNumber:
			print "Guess lower !!"
		else:
			print "Guess higher !!"

	#print Congratulation and goodbye
	print "Congratultion and Thank You for palying our Game !!!!"

if __name__ == "__main__":
	main()
