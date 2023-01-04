'''In this exercise, you're going to decompress a compressed string.

Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. For example:

The input

3[abc]4[ab]c

Would be output as

abcabcabcababababc

Other rules
Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa

One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab

Characters allowed as input include digits, small English letters and brackets [ ].

Digits are only to represent amount of repetitions.

Letters are just letters.

Brackets are only part of syntax of writing repeated substring.

Input is always valid, so no need to check its validity'''


def mydecompress(pattern: str) -> str:
    '''takes in a string in compressed format and returns the expanded version
    algorithm: if its outside brackets, it adds the char to the decomp string. 
                if its inside one set of brackets, then it adds the chars to a subpat.
                if there is a set of brackets inside a set of brackets, then it calls 
                itself recursively to expand the inner set'''
    #print("input",pattern)
    decomp = ''
    digit_str = ''
    subpat = ''
    left_brackets = 0
    right_brackets = 0
    left_ind = -1
    ##left_brackets==0 indicates that you are not inside a subpattern
    ##   left_brackets is the count of left brackets. right_brackets is the count of right brackets
    ##left_ind is the left opening bracket of the subpattern
    for ind, letter in enumerate(pattern):
        if left_brackets==0:
            if letter.isdigit():
                digit_str+=letter
        if letter=='[':
            if digit_str:
                digit = int(digit_str)
                digit_str=''
            left_brackets +=1
            if left_brackets==1:
                left_ind=ind
        elif letter.isalpha():
            if left_brackets==0:
                decomp+=letter
            elif left_brackets==1:
                subpat += letter
        elif letter==']':
            right_brackets+=1
            ##if opened and closed all the brackets
            if left_brackets==right_brackets:
                if left_brackets>1:
                    subpat=mydecompress(pattern[left_ind+1:ind])
                decomp += ''.join([subpat for i in range(digit)])
                subpat=''
                left_ind=-1
                left_brackets=0
                right_brackets=0
    return decomp+subpat

TEST_CASES = [('3[abc]4[ab]c','abcabcabcababababc'), ('2[3[a]b]','aaabaaab'), ('10[a]','aaaaaaaaaa'),
            ('c4[a]','caaaa'), ('c2[a]c2[a]','caacaa'), ('2[2[1[t]a]b]c', 'tatabtatabc'),
            ('2[c3[a]b]','caaabcaaab'),]

if __name__=='__main__':
    for test in TEST_CASES:
        failed = False
        resp = mydecompress(test[0])
        if test[1]!=resp:
            failed = True
            print()
            print('wrong')
            print(test[0])
            print("ans",test[1])
            print("mine",resp)
    if not failed:
        print("all test cases passed")