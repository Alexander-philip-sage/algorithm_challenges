'''Take an input string parameter and determine if exactly 3 question marks exist between every pair of numbers 
that add up to 10. If so, return True, otherwise return False. Some examples test cases are below'''
'''its unclear if negative numbers or floats are allowed inputs. assume not
assuming only single digits are considered'''
test_cases = [("arrb6???4xxbl5???eee5",True),
            ("acc?7??sss?3rr1??????5", True),
            ("5??aaaaaaaaaaaaaaaaaaa?5?5", False),
            ("9???1???9???1???9" , True),
            ("???30?10?0?07" , True),
            ("???30?10?0?07???3???" , True),
            ("aa6?9", False)]

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
for test in test_cases:
    resp=question_mark(test[0])
    print(test[0])
    if resp ==test[1]:
        print("correct\n")
    else:
        print("wrong")
        print("expected", test[1])
        print("returned", resp)
        print()

'''the question is extremely poorly stated for a written question where the user can't ask questions. 
it says every pair of numbers that add up to 10, but that isn't correct. It means to say count all the
question marks between a digit and its closest digit that sums to equal 10. 
the instruction is also unclear about what to do in the edge case of zero pairs found. these details have to be 
gleaned from the test cases.
this could probably be done faster by storing the numbers in a dict instead of an array where every key was the digit and 
value was the list of indices where that showed up. you would then take the biggest index as the j and count the question marks 
between j and the index you're at (i). 
'''