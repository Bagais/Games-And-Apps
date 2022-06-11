#Create list to store options: (R, P, S)
#ask user to pick an option
#return invalid for wrong selection (loop)
#use choice and random functions for CPU
#print both player selections
#Check moves
#print winner and break
#if tie, restart game from option selection

import random

available_opt = ['r', 'p', 's']
print(' ***RULES OF THE GAME*** \n rock vs paper -> paper wins \n rock vs scissors -> rock wins \n paper vs scissors -> scissors wins')

while True:
	print('\n***PICK ONE*** \n R for Rock, \n P for Paper, and \n S for Scissors \n')

	while True:
		user_selection = str.lower(input('***Please input your selection: \n'))

		if user_selection == 'r':
			user_pick='Rock'
			break
		elif user_selection == 'p':
			user_pick = 'Paper'
			break
		elif user_selection == 's':
			user_pick = 'Scissors'
			break
		else:
			print('\nInvalid Selection! Try Again')
			continue

	print('Player selection: ' + user_pick)
	print("\nComputer's turn....\n")

	comp_selection = random.choice(available_opt)
	if comp_selection == 'r':
		comp_pick = 'Rock'
	elif comp_selection == 'p':
		comp_pick = 'Paper'
	elif comp_selection == 's':
		comp_pick = 'Scissors'

	print('Computer selection: ' + comp_pick)
	print('player(', user_pick,' ) : CPU (', comp_pick,')\n')

	if user_selection == comp_selection:
		print('IT IS A TIE! try again')
		continue
	elif (user_selection =='r' and comp_selection =='p'):
		print('CPU Won!')
	elif (user_selection =='r' and comp_selection =='s'):
		print('You Won!')
	elif (user_selection =='s' and comp_selection =='p'):
		print('You Won!')
	elif (user_selection =='p' and comp_selection =='r'):
		print('You Won!')
	elif (user_selection =='s' and comp_selection =='r'):
		print('CPU Won!')
	elif (user_selection =='p' and comp_selection =='s'):
		print('CPU Won!')

	again = input('\nPlay Again? (y/n): ')
	if again.lower() != 'y':
		break
