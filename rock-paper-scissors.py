#/usr/bin/python

# Date created: 230408
# Date modified: 230410
# Author: n-anselm
# Description: Simple CLI rock paper scissors game

import random

player_score = 0
program_score = 0
playing_round = 0

print("Welcome to Rock Paper Scissors!")

while True:
	max_points = input("Up to how many points do you want to play? ")
	if max_points.isdigit() and max_points != "0":
		max_points = int(max_points)
		break
	else:
		print("Your response is not valid. Please enter any number greater than 0.")

# Generate a random choice
def gen_choice():
	list = ["rock", "paper", "scissors"]
	return list[random.randint(0, 2)]

# Get the player's choice and check that it's valid
def player_choice():
	choice = ""
	while True:
		choice = input("Enter your choice (rock/paper/scissors): ").lower()
		
		if choice == "rock" or choice == "paper" or choice == "scissors":
			return choice
		else:
			print("Your choice is not valid.")


while True:
	
	program = gen_choice()
	player = player_choice()
	
	playing_round += 1
	
	if program == player:
		print("\nTie!")
	elif program == "rock" and player == "paper" or program == "paper" and player == "scissors" or program == "scissors" and player == "rock":
		print("\nYou scored a point!")
		player_score += 1
	elif program == "rock" and player == "scissors" or program == "paper" and player == "rock" or program == "scissors" and player == "paper":
		print("\nThe program scored a point!")
		program_score += 1
	# Print choices
	print("Program:", program, "\nYou:    ", player, "\n")
	# Print scores
	print("Program:", program_score, "\nYou:    ", player_score, "\n")
	print("Round:", playing_round, "\n")

	if program_score == max_points:
		print("You lost!")
		break
	elif player_score == max_points:
		print("You won!")
		break

# TODO: If "q" or "quit" is entered, quit the program

'''
CASE SCENARIOS

rock rock - tie
rock paper - win
rock scissors - lose

paper paper - tie
paper rock - lose
paper scissors - win

scissors scissors - tie
scissors rock - win
scissors paper - lose
'''

