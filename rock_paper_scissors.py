from random import random
import sys, getopt
import argparse

def print_play(user,res,  char_to_word):
	print("\nyou played:", char_to_word[user], '\ncomputer played:', char_to_word[res[1]])
def print_play_atom(atom_user, res,char_to_word, paper_to_atom ):
	print("\nyou played:", atom_user, '\ncomputer played:',  paper_to_atom[char_to_word[res[1]]])

def display_result(res):
	if res[0]==0:
		print("You Won!")
	elif res[0]==1:
		print("You Lost... : (")
	elif res[0]==2:
		print("You tied with the computer")
		
def random_choice():
	rand = random()
	if rand <1/3:
		return'r'
	elif rand <2/3:
		return'p'
	else:
		return 's'

def rps_trial(user):
	'''user is a single letter input of the user's choice
	either 'r' 'p' or 's'
	returns 0-true or 1-false or 2-tie for victory or loss respectively
	in addition to the choice from the computer'''
	
	assert user in 'rsp', "ValueError: value must be either r, s, p"
	assert len(user)==1, "ValueError: value must be single letter"
	
	op= random_choice()
	if user ==op:
		return 2, op
	elif user in 'rs' and op in 'rs':
		if user=='r':
			return 0, op
		else:
			return 1, op
	elif user in 'rp' and op in 'rp':
		if user=='r':
			return 1, op
		else:
			return 0, op
	elif user in 'sp' and op in 'sp':
		if user=='s':
			return 0, op
		else:
			return 1, op
	else:
		raise Exception("unknown result of options")


if __name__ == "__main__":
	parser = argparse.ArgumentParser(
                    prog = 'Rock_Paper_Scissors',
                    description = ('Run the program with your action and it will try to defeat you.\n\n'
									'Interact with the program by passing an input or simulate a game by running test')
                    #epilog = '', ##'Text at the bottom of help'
					)
	parser.add_argument("-i", "--input", type=str, help=('must be of either rock, paper, or scissors. ' 
									'do not put \' or " around the input word. ' 
									'accepts alternate game of cockroach, shoe, nuke'))
	parser.add_argument("-t", "--test", action='store_true', help="runs trials of the game to see how it performs")

	args = parser.parse_args()
	if not args.input and not args.test:
		parser.print_help()
	if args.input and args.test:
		parser.print_help()
		print("\nError: cannot call both input and test simultaneously")
		sys.exit()

	##setup maps that are needed to interpret inputs
	char_to_word = {'r':"rock", 's':'scissors', 'p':'paper'}
	word_to_char = {}
	for k in char_to_word.keys():
		word_to_char[char_to_word[k]] = k
	atom_to_paper={'cockroach':'paper', 'nuke':'rock', 'shoe':'scissors'}
	paper_to_atom = {}
	for k in atom_to_paper.keys():
		paper_to_atom[atom_to_paper[k]] = k

	if args.input:
		if args.input in word_to_char.keys():
			user = word_to_char[args.input]
			res = rps_trial(user)
			print_play(user,res,  char_to_word)
			display_result(res)
		elif args.input in atom_to_paper.keys():
			paper_user = atom_to_paper[args.input]
			res = rps_trial(word_to_char[paper_user])
			print_play_atom(args.input, res,char_to_word, paper_to_atom )
			display_result(res)
		else:
			print("Error: input", args.input," not recognized\n")
			parser.print_help()
			sys.exit()
	elif args.test:
		for i in range(10):
			user = random_choice()
			res = rps_trial(user)
			print_play(user,res,  char_to_word)
			display_result( res)