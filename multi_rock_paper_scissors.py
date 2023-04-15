'''A group of people are sitting in a circle, playing a special version of rock, paper, scissors. In this game, each person chooses rock, paper, or scissors in secret and then everyone reveals their choice to everyone else. Each person then compares their selection to their two neighbors, and can win, lose, or tie against each of them independently. The only way to tie is when both people make the same choice.

You want to make it so that no game is a tie. For each player, you can let them keep their choice, or you can ask them to change to any of the other two options (you choose to which one). What is the minimum number of people you need to request a change from to ensure that there are no ties between neighbors after those changes are made?

Input
The first line of the input gives the number of test cases, T. T
 lines follow. Each line represents a test case and contains a string C. The i-th character of C
 represents the original choice of the i-th person in clockwise order using an uppercase R to mean rock, an uppercase P to mean paper, and an uppercase S to mean scissors.

Output
For each test case, output one line containing Case #x : y, where x is the test case number (starting from 1) and y is the minimum number of changes that are required such that no two neighbors end up with the same choice'''


"""7
PRSSP
RR
RRR
RRRR
RRRRR
RRRRRRR
RSPRPSPRS"""
"""
2
1
2
2
3
4
0"""

import argparse

def recommend(game:str):
    needs_changing = 0
    ind = 0 
    while ind <len(game):
        if ind==len(game)-1:
            if game[ind]==game[0]:
                needs_changing+=1
            break
        else:
            if game[ind]==game[ind+1]:
                needs_changing+=1
                ind +=2
            else:
                ind +=1
    return needs_changing

def stop_ties(test_cases:str)->str:
    challenge_list = []
    for i, line in enumerate(test_cases.splitlines()):
        if i==0:
            ct_challenges = int(line)
        else:
            challenge_list.append(line)
    assert len(challenge_list)==ct_challenges 
    result = ''
    for i, game in enumerate(challenge_list):
        result += f"Case #{i+1}: "
        result +=str(recommend(game))
        if i<(len(challenge_list)-1):
            result+="\n"
    return result

if __name__=='__main__':
    parser = argparse.ArgumentParser(
                                    prog = 'multi_player_rock_paper_scissors',
                                    description = ("""Input
The first line of the input gives the number of test cases, T. T
 lines follow. Each line represents a test case and contains a string C. The i-th character of C
 represents the original choice of the i-th person in clockwise order using an uppercase R to mean rock, an uppercase P to mean paper, and an uppercase S to mean scissors.
""")
                                    )
    parser.add_argument('test_cases') 
    args = parser.parse_args()
    print(stop_ties(args.test_cases))
