import datetime
'''Take an input string parameter and determine if exactly 3 question marks exist between every pair of numbers 
that add up to 10. If so, return True, otherwise return False. Some examples test cases are below'''
'''its unclear if negative numbers or floats are allowed inputs. assume not
assuming only single digits are considered'''
test_cases = [("arrb6???4xxbl5???eee5",True),
            ("acc?7??sss?3rr1??????5", True),
            ("5??aaaaaaaaaaaaaaaaaaa?5?5", False),
            ("5??aaaaaaaaaaaaaaaaaaa?55", False),
            ("7??aaaaaaaaaaaaaaaaaaa?33", True),
            ("9???1???9???1???9" , True),
            ("???30?10?0?07" , True),
            ("???30?10?0?07???3???" , True),
            ("aa6?9", False),
            ("aa6??7?4??39", True),
            ("aa69", False),
            ("1937", False),
            ("???", False),
            ("aa", False),
            ("".join(['5a?' for x in range(100000000)]),False)                        
            ]

def question_mark2(var: str) -> bool:
    '''input: var : a string with some number of question marks, letters and numbers
    return: a boolean indicating if there are three question marks between every 
    adjacent pair of digits that add to 10
    algorithm: this is the second version. it runs in O(n) time'''
    digit_lookup = {}
    ct_qs = 0
    res = False
    for chr in var:
        if chr=='?':
            ct_qs+=1
        elif chr.isdigit():
            dchr = int(chr)
            compl = 10-dchr
            if compl in digit_lookup.keys():
                if (ct_qs-digit_lookup[compl])==3:
                    res = True
                else:
                    return False
            digit_lookup[dchr] = ct_qs
    return res
def question_mark(var):
    questions = []
    numbers = []
    pair_found = False
    for i,letter in enumerate(var):
        if letter=='?':
            questions.append(1)
        else:
            questions.append(0)
        if letter.isdigit():
            num = int(letter)
            if i>0:
                if (num+numbers[-1])==10:
                    return False
                compliment = 10 - num
                for j in reversed(range(len(numbers))):
                    tmp = numbers[j]
                    if tmp == compliment:
                        ct_questions = sum(questions[j:i+1])
                        if ct_questions!=3:
                            return False
                        else:
                            pair_found=True
                            break
            numbers.append(num)
        else:
            numbers.append(0)
    if pair_found:
        return True
    else:
        return False
def test_func(func):
    print()
    print("testing", func.__name__)
    start = datetime.datetime.now()
    failed = False
    for i in range(1000000):
        func(test_cases[-1][0])
    for test in test_cases:
        resp=func(test[0])
        if resp!=test[1]:
            failed = True
            print()
            print(test[0])
            print("Failed")
            print("expected", test[1])
            print("returned", resp)
    if not failed:
        print("all tests passed")
    print("processing time", (datetime.datetime.now()-start).total_seconds())
test_func(question_mark)
test_func(question_mark2)
'''the question is extremely poorly stated for a written question where the user can't ask questions. 
it says every pair of numbers that add up to 10, but that isn't correct. It means to say count all the
question marks between a digit and its closest digit that sums to equal 10. this sum of question marks should equal 3.
if it were every pair that added to 10 then you couldn't have more than two fives in the same string.
the instruction is also unclear about what to do in the edge case of zero pairs found. these details have to be 
gleaned from the test cases.
this could probably be done faster by storing the numbers in a dict instead of an array where every key was the digit and 
value was the list of indices where that showed up. you would then take the biggest index as the j and count the question marks 
between j and the index you're at (i). 
'''