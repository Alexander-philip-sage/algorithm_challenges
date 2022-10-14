'''Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.'''

'is it always lower case? is a solution case sensitive?'

def sub_string(primary, words):
    '''apparently len is O(1) in python. its a simple lookup, not a for loop like I expected so that would change this answer a bit'''
    if not primary:
        return False
    if not words:
        return False        
    primary = primary.lower()
    words = [w.lower() for w in words]
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
def g_sub_string(primary, words):
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

for j, test in enumerate(test_cases):
    print("-------------------------")
    start = datetime.datetime.now()
    iterations = 100000
    for i in range(iterations):
        resp = sub_string(test[0], test[1])
    print("test", j)
    if resp==test[2]:
        print("my code correct")
    else:
        print("my code wrong")
        print("my code", resp)
        print("answer ", test[2])
        print("!!!!!!!!!!!!!!!!!!!1")
        print(test)
    print("processing time", (datetime.datetime.now()-start)/iterations)

    print()

    start = datetime.datetime.now()
    for i in range(iterations):
        resp = g_sub_string(test[0], test[1])
    if resp==test[2]:
        print("their code correct")
    else:
        print("their code wrong")    
        print("their code modified\t", resp)
        print("answer\t\t\t", test[2])
        print("!!!!!!!!!!!!!!!!!!!1")    
    print("processing time", (datetime.datetime.now()-start)/iterations)
    print()

