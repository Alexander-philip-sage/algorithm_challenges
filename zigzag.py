from typing import List

challenge_prompt = """
input: List[int] 
    variable length list of integers

Algorithm:
    a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.
    pass a window of length 3 over the input list. at each stop for the window, if you hit a zigzag, save 1 to the return array, 0 otherwise.

return: 
    List[int]
    the return list will include only numbers 0 or 1"""
    
def zig_zag(arr: List[int], i: int) -> int:
    if (arr[0+i]>arr[1+i]<arr[2+i]) or (arr[0+i]<arr[1+i]>arr[2+i]):
        return 1
    else:
        return 0
        
def find_zig_zags(arr: List[int]):
    ct = len(arr)
    assert 3<= ct <=100
    ret = [0 for x in range(ct-2)]
    for i in range(ct-2):
        ret[i] = zig_zag(arr, i)
    return ret

def check_rets(a, b):
    if len(a)!= len(b):
        print("answer wrong length")
        return False
    for i, val in enumerate(a):
        if val!= b[i]:
            print("values don't equal")
            return False
    return True

def test_cases():
    cases = [
        ([33, 22, 33], [1]),
        ([33, 22, 36], [1]),
        ([33, 82, 36], [1]),
        ([33, 22, 6], [0]),
        ([33, 22, 6, 13, 44, 27], [0, 1, 0, 1]),
        ([3, 3, 3, 3, 3, 3], [0, 0, 0, 0]),
        ([33, 22, 6, 33, 22, 6], [0, 1, 1, 0]),
    ]
    passed = True
    for case in cases:
        arr = case[0]
        a = case[1]
        b = find_zig_zags(arr)
        if not check_rets(a, b):
            passed = False
            print("\nfailed")
            print(arr)
            print("true", a)
            print("algo", b)
    if passed: 
        print("all tests passed")
if __name__=="__main__":
    test_cases()