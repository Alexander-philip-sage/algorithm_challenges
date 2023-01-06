'''You want to create a method that receives a hand of 5 cards and returns the best poker hand you can make with those cards
num_opts = set([x+1 for x in range(10)])
symbol_opts = set(['a', 'b', 'c', 'd']) 

For simplification, we’ll assume cards have a number and a symbol. Numbers go from 1 to 10 and symbols are ‘a’, ‘b’, ‘c’ and ‘d’.

To start off, assume there are only 3 types of poker hands, from better to worse. 
Take into consideration you will have to add the other ones later.

Flush: 5 cards of the same symbol. Example: 10a 4a 2a 7a 9a
Three of a Kind: 3 cards with the same number. Example: 4a 3b 1c 4d 4b
Pair: Two cards with the same number. Example: 3a 2b 8d 1a 8c

Return the best poker hand you have. For example. If you have a pair, return “Pair” or any structure that symbolizes you have a pair.
If you have a three of a kind, return “Three of a Kind” or any structure that represents it.
https://codereview.stackexchange.com/questions/60738/optimizing-poker-hands-challenge-solution
https://leetcode.com/problems/best-poker-hand/
https://www.youtube.com/watch?v=6BijC5dBUOA'''

from typing import List

def read_num(card: str) -> int:
    return int(card.replace(card[-1], ''))
def find_hand(cards: List[str]) -> str:
    num_opts = set([x+1 for x in range(10)])
    symbol_opts = set(['a', 'b', 'c', 'd']) 
    flush = True
    three_of_kind = False
    pair = False
    track = [[] for x in range(10)]
    high_card_i = -1
    high_card_v = 0
    for i, card in enumerate(cards):
        if i<(len(cards)-1):
            if cards[i][-1]!=cards[i+1][-1]:
                flush = False
        card_num = read_num(card)
        if card_num > high_card_v:
            high_card_v = card_num
            high_card_i = i
        track[card_num-1].append(card)
        if len(track[card_num-1])==2:
            if not pair:
                pair = True
                pair_i = card_num-1
            else:
                if card_num> (pair_i+1):
                    pair_i = card_num-1
        elif len(track[card_num-1])==3:
            three_of_kind = True
            three_of_kind_i = card_num-1
    if flush:
        return cards
    elif three_of_kind:
        return track[three_of_kind_i]
    elif pair:
        return track[pair_i]
    else:
        return [cards[high_card_i]]

TEST_CASES = [
            (['1a', '2a', '3a', '4a', '5b'],['5b']),##high card
            (['1b', '2a', '3a', '4a', '5a'],['5a']),##high card
            (['7a', '7b', '2a', '8c', '10d'],['7a', '7b']),##pair
            (['1d', '5d', '3d', '8d', '10d'],['1d', '5d', '3d', '8d', '10d']),##flush random numbers
            (['1a', '2a', '3a', '4a', '5a'],['1a', '2a', '3a', '4a', '5a']),##flush succeeding numbers
            (['6a', '6b', '6d', '1a', '10a'],['6a', '6b', '6d' ]),##three of kind
            (['6a', '6b', '4d', '5a', '5d'],['6a', '6b']),##two pairs
            (['7c', '7a', '7d', '5a', '5d'],['7c', '7a', '7d']),##three of kind and pair
            ]


if __name__=='__main__':
    passed = True
    for test in TEST_CASES:
        res = find_hand(test[0])
        if set(res)!= set(test[1]):
            print("Failed")
            passed = False
            print(test)
            print("result", res)
