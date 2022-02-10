from random import random
import sys, getopt

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
	
def main(argv):
	
	char_to_word = {'r':"rock", 's':'scissors', 'p':'paper'}
	word_to_char = {}
	for k in char_to_word.keys():
		word_to_char[char_to_word[k]] = k
	atom_to_paper={'cockroach':'paper', 'nuke':'rock', 'shoe':'scissors'}
	paper_to_atom = {}
	for k in atom_to_paper.keys():
		paper_to_atom[atom_to_paper[k]] = k
	
	
	try:
		opts, args = getopt.getopt(argv,"hi:t",["input=", "help", "test"])
	except getopt.GetoptError:
		print('file: rock_paper_scissors.py')
		print("for help run \npython rock_paper_scissors.py -h")
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-h', "--help"):
			print ('file: rock_paper_scissors.py')
			print("Arguments:")
			print("short\tlong\t\tdescription")
			print("-h\t--help\t\tdisplay this help message")
			print("-i\t--input\t\tinput must be of either rock, paper, or scissors")
			print("\t\t\tdo not put ' or \" around the input word")
			print("\t\t\taccepts alternate game of cockroach, shoe, nuke")
			print("-t\t--testing\truns trials of the game to see how it performs")
			sys.exit()
		elif opt in ("-i", "--input"):
			if arg in word_to_char.keys():
				user = word_to_char[arg]
				mode='single'
			elif arg in atom_to_paper.keys():
				mode ='atomic'
				atom_user = arg
			else:
				raise Exception("option must be either rock, paper, or scissors")
		elif opt in ("-t", "--test"):
			print("Running tests on game")
			mode = 'test'
		else:
			print("incorrect input")
			print("expected rock, paper or scissors")
			print("use -h for guidance")
			sys.exit()
			
	if mode=='single':
		res = rps_trial(user)
		print_play(user,res,  char_to_word)
		display_result(res)
	elif mode=='atomic':
		paper_user = atom_to_paper[atom_user]
		res = rps_trial(word_to_char[paper_user])
		print_play_atom(atom_user, res,char_to_word, paper_to_atom )
		display_result(res)
	elif mode=='test':
		for i in range(10):
			user = random_choice()
			res = rps_trial(user)
			print_play(user,res,  char_to_word)
			display_result( res)

if __name__ == "__main__":
	main(sys.argv[1:])





