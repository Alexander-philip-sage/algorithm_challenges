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


def mydecompress(pattern):
    #print("input",pattern)
    decomp = ''
    digit_str = ''
    subpat = ''
    left = 0
    right = 0
    left_ind = -1
    for ind, letter in enumerate(pattern):
        if left==0:
            if letter.isdigit():
                digit_str+=letter
        if letter=='[':
            if digit_str:
                digit = int(digit_str)
                digit_str=''
            left +=1
            if left==1:
                left_ind=ind
        if letter.isalpha():
            if left==0:
                decomp+=letter
            else:
                subpat += letter
        if letter==']':
            right+=1
            if left==right:
                if left>1:
                    subpat=mydecompress(pattern[left_ind+1:ind])
                    decomp += ''.join([subpat for i in range(digit)])
                    subpat=''
                elif left==1:
                    decomp += ''.join([subpat for i in range(digit)])
                    subpat=''
                left_ind=-1
                left=0
                right=0


    return decomp+subpat

test_cases = [('3[abc]4[ab]c','abcabcabcababababc'), ('2[3[a]b]','aaabaaab'), ('10[a]','aaaaaaaaaa'),
            ('c4[a]','caaaa'), ('c2[a]c2[a]','caacaa')]
for test in test_cases:
    print()
    resp = mydecompress(test[0])
    print(test[0])
    if test[1]==resp:
        print("correct")
    else:
        print('wrong')
        print("ans",test[1])
        print("mine",resp)
