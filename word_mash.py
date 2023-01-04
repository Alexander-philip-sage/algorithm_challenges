from typing import List
challenge_prompt = """
input: List[str]
    list of strings. the list length varies. the length of each string varies inside the list

algorithm: 
    create a new string that combines all the letters from the strings in the input. the first 
    letter will be the first letter of the first string. second letter, the first letter of the 
    second string - and so on through the list until going back up to the top of the list to 
    loop through the second letters. if a string doesn't have a letter, then it will be skipped 
    in each succeeding loop.

return: str"""

def solution2(arr: List[str]) -> str:
    '''this one is slightly faster since it doesn't run the first 
    for loop to check what the longest string size is'''
    index = 0 
    wrd_ind =0 
    result = ''
    still_adding = True
    ##longest==length of longest string
    ##O(longest*len(arr))
    while still_adding:
        still_adding = False
        for wrd in arr:
            if index < (len(wrd)):
                result+=wrd[index]
            if index < (len(wrd)-1):
                still_adding=True
        index +=1
    return result

def solution(arr: List[str]) -> str:
    longest = 0
    ##O(len(arr))
    for wrd in arr:
        if len(wrd) > longest:
            longest = len(wrd)
    ret = ''
    ##O(longest*len(arr))
    for i in range(longest):
        for wrd in arr:
            if len(wrd) >i:
                ret += wrd[i]
    return ret

TEST_CASES = [  
                (["this", "is", "a", "potato"],"tiaphsoitsato"),
                (['this', 'hat', 'a'],"thahaits"),
                (['c', 't', 'a'],"cta"),
                (['fox', 'dog', 'cat'],"fdcooaxgt"),
                (['fox', 'dog', 'labrador'],"fdlooaxgbrador"  ),
                (['fox'],'fox'),
                (['G'],'G'),
                ([''],''),
                ]

def run_tests(func):
    print("testing", func.__name__)
    for test in TEST_CASES:
        failed = False
        resp = func(test[0])
        if test[1]!=resp:
            failed = True
            print()
            print('Failed')
            print(test[0])
            print("answer",test[1])
            print("result",resp)
    if not failed:
        print("all test cases passed")
if __name__=='__main__':
    run_tests(solution)
    run_tests(solution2)