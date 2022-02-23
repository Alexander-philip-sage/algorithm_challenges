from typing import List
challenge_prompt = """
input: List[str]
    list of strings. the list length varies. the length of each string varies inside the list

algorithm: 
    create a new string that combines all the letters from the strings in the input. the first letter will be the first letter of the first string. second letter, the first letter of the second string - and so on through the list until going back up to the top of the list to loop through the second letters. if a string doesn't have a letter, then it will be skipped in each succeeding loop.

return: str"""

def solution(arr: List[str]):
    longest = 0
    for wrd in arr:
        if len(wrd) > longest:
            longest = len(wrd)
    ret = ''
    for i in range(longest):
        for wrd in arr:
            if len(wrd) >i:
                ret += wrd[i]
    return ret

def tests():
    arr = ["this", "is", "a", "potato"]
    print(arr)
    assert solution(arr) == "tiaphsoitsato"
    print("test passed")

    arr = ['this', 'hat', 'a']
    print(arr)
    assert solution(arr) == "thahaits"
    print("test passed")

    arr = ['c', 't', 'a']
    print(arr)
    assert solution(arr) == "cta"
    print("test passed")

    arr = ['fox', 'dog', 'cat']
    print(arr)
    assert solution(arr) == "fdcooaxgt"
    print("test passed")

    arr = ['fox', 'dog', 'labrador']
    print(arr)
    assert solution(arr) == "fdlooaxgbrador"    
    print("test passed")

    arr = ['fox']
    print(arr)
    assert solution(arr) == "fox"    
    print("test passed")

    arr = ['f']
    print(arr)
    assert solution(arr) == "f"    
    print("test passed")

    arr = ['']
    print(arr)
    assert solution(arr) == ""    
    print("test passed")

tests()