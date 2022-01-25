import random
user_num = input("Enter a number between 0-30!")
guess = random.randint(0,30)

print("The computer guesses....")

while user_num == guess:
 	print("You guessed right!!!")
 
if user_num != guess:
		print( "You lost this round!!!!!", "The computer guessed", guess)
	
	

	
