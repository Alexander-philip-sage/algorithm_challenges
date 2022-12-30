from typing import List
'''Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.'''

'is it always lower case? is a solution case sensitive?'

def checks(primary: str, words: List[str]):
    if not primary:
        return False, False, False
    if not words:
        return False, False, False      
    primary = primary.lower()
    words = [w.lower() for w in words]
    return True, primary, words
def sub_string2(primary: str, words: List[str]):
    '''second try caching values'''
    check_rs, primary, words=checks(primary, words)
    if not check_rs:
        return False
    primary_leters = {}
    for i, letter in enumerate(primary):
        if letter not in primary_leters.keys():
            primary_leters[letter]=[i]
        else:
            primary_leters[letter].append(i)
    max_word = ''
    for wrd in words:
        prev = -1
        found = True
        for letter in wrd:
            if letter not in primary_leters.keys():
                found = False
                break
            elif max(primary_leters[letter])>prev:
                for index in primary_leters[letter]:
                    if index > prev:
                        prev = index
                        break
            else:
                found = False
                break
        if found and (len(wrd) > len(max_word)):
            max_word = wrd
    return max_word if len(max_word)>0 else False
def sub_string(primary: str, words: List[str]):
    '''first try. naive with for loops
    returns either a string if the sub_words was found, or False if no sub_words were found'''
    check_rs, primary, words=checks(primary, words)
    if not check_rs:
        return False
    found = []
    for w in words:
        ind = 0 
        if len(primary) < len(w):
            continue
        if len(w) >0:
            for letter in primary:
                if letter ==w[ind]:
                    ind+=1
                    if ind==len(w):
                        found.append((w,len(w)))
                        break
    if len(found)==0:
        return False

    max_len = 0
    max_word = ''
    for tup in found:
        if tup[1]>max_len:
            max_word = tup[0]
            max_len = tup[1]
    return max_word
import collections
def g_sub_string(primary: str, words: List[str]):
    '''a recommended approach by google that I modified to cut a for loop sooner
    and to accomodate edge cases'''
    letter_positions = collections.defaultdict(list)
    for index, letter in enumerate(primary):
        letter_positions[letter].append(index)    
    if not words:
        return False
    for word in sorted(words, key=lambda w: len(w), reverse=True):
        pos =0 
        for i,letter in enumerate(word):
            if letter not in letter_positions:
                break    
            found_letter = False
            for new_pos in letter_positions[letter]:
                if new_pos>=pos:
                    pos = new_pos+1
                    found_letter =True
                    break
            if not found_letter:
                break
            if i==(len(word)-1):
                return word
    return False

'for cases of long primary words, and smaller dictionary words, it helps to create sets of all the letters in each, '
'then compare sets to avoid looping through the whole primary word each time'
import datetime
test_cases = [("abppplee" ,["able", "ale", "apple", "bale", "kangaroo"],'apple'),
                ("" ,["able", "a", "apple", "bale", "kangaroo"],False),
                ("adkjkld" ,[],False),
                ("potato" ,["able", "ale", "apple", "bale", "kangaroo"],False),
                ("potato" ,["qqqqqqqq", "qqqqqqqqqqqq", "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu","eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", "kangaroo"],False),
                ("potatopotatopotatopotatopotatopotatopotatopotatopotatopotatopotatopotatopotatopotato" ,["able", "ale", "potato", "bale", "kangaroo"],'potato'),
                ("potato" ,["able", "a", "apple", "bale", "kangaroo"],'a'),
                ("dkjacoiupdnm,pwuipcipulsoiue" ,["able", "ale", "apple", "bale", "kangaroo"],'apple'),
                ("dkjacoiupdnm,pwuipcipulsoiue"+"".join(['a' for i in range(1000)]) ,["able", "ale", "apple", "bale", "kangaroo"],'apple'),
                ("dkjacoiupdnm,pwuipcipulsoiue" ,["able", "ale", "apple", "bale", "kangaroo"]+['a' for i in range(1000)],'apple'),
                ("pzoztatzo" ,["able","".join(['a' for i in range(1000)]), "ale", "apple", "zzz", "kangaroo"],'zzz'),
                ("pzoztatzo" ,["able", "ale", "apple", "zzz", "kangaroo"],'zzz'),
                ("pzoztato" ,["able", "ale", "apple", "zzz", "kangaroo"],False),
                ("pzoztato" +"".join(['z' for i in range(1000)]) ,["able", "ale", "apple", "zzz", "kangaroo"],'zzz'),
            ]

def test_manual(test_func):
    '''takes in the function to test and tests both accuracy and speed'''
    print("\ntesting", test_func.__name__)
    print("speed testing")
    iterations = 100000
    test = test_cases[0]
    start = datetime.datetime.now()
    for i in range(iterations):
        resp = test_func(test[0], test[1])
    print("processing time", (datetime.datetime.now()-start).total_seconds()/iterations)
    failed = False

    for j, test in enumerate(test_cases):
        resp = test_func(test[0], test[1])
        if resp!=test[2]:
            failed = True
            print("\ntest", j,test_func.__name__ )
            print("Failed")
            print("result", resp)
            print("answer ", test[2])
            print(str(test)[:100])
    if not failed:
        print("all tests passed")

if __name__=='__main__':
    test_manual(g_sub_string)
    test_manual(sub_string)
    test_manual(sub_string2)