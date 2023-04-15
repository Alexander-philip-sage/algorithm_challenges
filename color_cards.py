"""Your friend Charles gives you a challenge. He puts N
 cards on a table and arranges them in a line in an order that he chooses. Each card has a single color, and each color can be on one or more cards.

Charles then asks you to write a positive integer on each card without altering his chosen order such that:

The integers you write appear in non-decreasing order when cards are read from left to right.
Cards of the same color have the same integer written on them.
Cards of different colors have different integers written on them.
Finally, Charles wants you to order the colors in increasing order of written integer. For example, if blue cards have a 2
, red cards have a 5
, and green cards have a 3
, the color order would be blue, green, red.

Input
The first line of the input gives the number of test cases, T. T test cases follow.
Each test case begins with a line containing the integer N. The next line contains N
 integers, S1, S2, …, SN, where Si represents the color of the i-th card from the left"""
"""2
4
3 8 8 2
5
3 8 2 2 8"""

import argparse
from typing import List
def order_colors(challenge:List[str])->str:
    colors_seen = set()
    result = ''
    for i in range(len(challenge)):
        if i==0:
            colors_seen.add(challenge[i])
            result = challenge[i]
        else:
            if challenge[i]!=challenge[i-1]:

                if  challenge[i] in colors_seen:

                    return 'IMPOSSIBLE'
                else:
                    result += ' '+challenge[i]
                    colors_seen.add(challenge[i])
    return result

def process_challenges(challenges:str):
    result=''
    challeng_ind = 0
    for i, line in enumerate(challenges.splitlines()):
        if i==0:
            ct_challenges = int(line)
        elif (i-1)%2==1:
            order = order_colors([x for x in line.split()])
            result += f"Case #{challeng_ind+1}: "+order
            challeng_ind+=1
            if challeng_ind!=ct_challenges:
                result+='\n'
    return result

if __name__=='__main__':
    parser = argparse.ArgumentParser(
                                    prog = 'card order',
                                    description = ("""Input
The first line of the input gives the number of test cases, T. T test cases follow.
Each test case begins with a line containing the integer N. The next line contains N
 integers, S1, S2, …, SN, where Si represents the color of the i-th card from the left""")
                                    )
    parser.add_argument('test_cases') 
    args = parser.parse_args()
    print(process_challenges(args.test_cases))