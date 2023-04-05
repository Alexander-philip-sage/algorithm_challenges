'''Vowel Square Have the function VowelSquare(strArr) take the strArr parameter being passed 
which will be a 2D matrix of some arbitrary size filled with letters from the alphabet, and 
determine if a 2x2 square composed entirely of vowels exists in the matrix. 
For example: strArr is ["abcd", "eikr", "oufj"] then this matrix looks like the following:
a b c d

e i k r

o u f j
Within this matrix there is a 2x2 square of vowels starting in the second row and first column, 
namely, ei, ou. If a 2x2 square of vowels is found your program should return the top-left 
position (row-column) of the square, so for this example your program should return 1-0. 
If no 2x2 square of vowels exists, then return the string not found. 
If there are multiple squares of vowels, return the one that is at the most top-left position 
in the whole matrix. The input matrix will at least be of size 2x2.
'''
TEST_CASES = [(["aqrst", "ukaei", "ffooo"], (1,2)), (["gg", "ff"], False),
              (["abcd", "eikr", "oufj"],(1,0)),
              (["aead", "sior", "ouij"],(0,1)),

              ]
from typing import List
import numpy as np

def is_vowel(letter):
    return letter in ('a', 'e', 'i', 'o', 'u')

def find_vowel_square(str_arr: List[str]):
    '''takes in a list of strings. each string must be equal size.
    returns either False for no vowel square found or the coordinates of the vowel square'''
    for ri in range(0,len(str_arr)-1):
        for ci in range(0,len(str_arr[0])-1):
            if ((is_vowel(str_arr[ri][ci]) and is_vowel(str_arr[ri+1][ci]))
                and (is_vowel(str_arr[ri][ci+1]) and is_vowel(str_arr[ri+1][ci+1]))):
                return (ri,ci)                    
    return False
if __name__=='__main__':
    for test in TEST_CASES:
        failed = False
        resp = find_vowel_square(test[0])
        if test[1]!=resp:
            failed = True
            print()
            print('wrong')
            print(test[0])
            print("ans",test[1])
            print("mine",resp)
    if not failed:
        print("all test cases passed")    
