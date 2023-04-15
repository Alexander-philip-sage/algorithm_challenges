'''Alan just had his first cryptography class in school today. He decided to apply what he learned and come up with his own cipher. He will map each English letter from A to Z to a decimal digit 0
 through 9
. He will then try to encode each word to a string consisting of decimal digits by replacing each letter in the word with its mapped digit.

In his excitement, Alan failed to notice that there are 26
 letters in the English alphabet and only 10
 decimal digits. As a result, there might be collisions, that is, pairs of different words whose encoding is the same.

Given a list of N
 words that Alan wants to encode and the mapping that he uses, can you find out if there would be any collisions between words on the list?

Input
The first line of the input gives the number of test cases, T. T test cases follow. The first line of each test case contains 26 decimal digits (integers between 0
 and 9, inclusve) DA,DB,…,DZ, representing the mapping that Alan uses. A letter α is mapped to digit Dα.The second line of each test case contains N, the number of words Alan will encode.
The i-th of the last N lines contains a string Si, representing the i-th word Alan will encode.
Output For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y
 is either YES, if there is at least one pair of different words from the list whose encoding coincides, and NO otherwise.

Limits
Time limit: 20 seconds.
Memory limit: 2 GB.
1≤T≤100
.
0≤Dα≤9
, for all α
.
1≤
 the length of Si≤10
, for all i
.
Each character of Si
 is an uppercase English letter A through Z, for all i
.
Si≠Sj
, for all i≠j
.'''
TEST_CASES = [[
'''2
0 1 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
4
ABC
BC
BCD
CDE
0 1 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
3
CDE
DEF
EFG''',
'''Case #1: NO
Case #2: YES''']
]
from typing import List
LIST_LETTERS = [chr(65+ind) for ind in range(26)]
class Challenge():
    def __init__(self, digit_list:List[int], ct_words:int, words:List[str]):
        self.digit_list = digit_list
        self.cipher = {LIST_LETTERS[ind]:digit_list[ind] for ind in range(26)}
        self.ct_words = ct_words
        self.words = words
        self.collision = False
        self.ciphered_words = set()
    def __str__(self):
        return f"cipher: {self.cipher}\nct_words: {self.ct_words}\nwords: {self.words}"
    def cipher_wrd(self,word:str)->str:
        ciphered_word =''
        for ch in word:
            ciphered_word+=str(self.cipher[ch]) 
        if ciphered_word in self.ciphered_words:
            self.collision=True
            return True
        self.ciphered_words.add(ciphered_word)
        return False
    def cipher_words(self):
        for wrd in self.words:
            if self.cipher_wrd(wrd):
                return True
        return False

def check_collisions(challenges:str)->str:
    ct_challenges = int(challenges.split("\n")[0])    
    stage = ''
    cipher = []
    word_i = 0
    words=[]
    challenge_list = []
    for i, line in enumerate(challenges.splitlines()):
        if i==0:
            ct_challenges = int(line)
        else:
            if stage=='':
                cipher = [int(x) for x in line.split()]
                stage='ct_words'
            elif stage=='ct_words':
                ct_words = int(line)
                word_i = 0
                stage='words'
            elif stage=='words':
                if word_i<ct_words:
                    words.append(line.strip())
                    word_i+=1
                if word_i==(ct_words):
                    ##save results
                    challenge_list.append(Challenge(cipher, ct_words, words))
                    cipher = []
                    word_i = 0
                    words=[]   
                    stage=''
    assert len(challenge_list)==ct_challenges             
    result = ''
    for i, challenge in enumerate(challenge_list):
        #print(challenge)
        result += f"Case #{i+1}: "
        if challenge.cipher_words():
            result+= "YES"
        else:
            result+= "NO"
        if i<(len(challenge_list)-1):
            result+="\n"

    return result

def test_once():
    challenges = TEST_CASES[0][0]
    ans = TEST_CASES[0][1]
    result = check_collisions(challenges)
    if result==ans:
        print('passed')
    else:
        print(result)
        print(ans)

import argparse
if __name__=='__main__':
    ##take the string including quotes in cipher_test.txt 
    ##copy to clipboard. and past it as the required input to this on command line
    parser = argparse.ArgumentParser(
                                    prog = 'cipher_check_collisions',
                                    description = ('Input: The first line of the input gives the number of test cases, T. T test cases follow. \n'
                                    'The first line of each test case contains 26 decimal digits (integers between 0'
                                    ' and 9, inclusve) DA,DB,…,DZ, representing the mapping that Alan uses. \nA letter α is mapped '
                                    'to digit Dα.The second line of each test case contains N, the number of words Alan will encode.\n'
                                    'The i-th of the last N lines contains a string Si, representing the i-th word Alan will encode.\n'
                                    'Output For each test case, output one line containing Case #x: y, where x is the test case number '
                                    '(starting from 1) \nand y is either YES, if there is at least one pair of different '
                                    'words from the list whose encoding coincides, and NO otherwise.\n'
                                    'Interact with the program by passing an input or simulate a game by running test')
                                    )
    parser.add_argument('challenges') 
    args = parser.parse_args()
    print(check_collisions(args.challenges))

