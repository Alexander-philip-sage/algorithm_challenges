'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''
from typing import List

def parity(nums: List[int]):
    i = 0
    j = len(nums)-1
    odd_found = -1
    while i<j:
        if nums[i]%2==0:
            i+=1
        elif not nums[j]%2==0:
            j-=1
        elif not nums[i]%2==0 and nums[j]%2==0:
            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp
            i+=1 
        #print("i", i,"nums", nums[i],  "j","nums", nums[j], nums )
    return nums
def test_parity(nums: List[int]):
    odd = 0 
    for var in nums:
        if (var%2==0) and odd:
            return False
        if not (var%2==0) and (not odd):
            odd=1

    return True
TEST_CASES = [
                [3,1,2,1,3],
                [3,1,2,4],
                ]

TEST_PARITY_TEST = [
                ([1,3,5,7,9], True),
                ([0,2,4,6], True),
                ([2,1], True),
                ([0], True),
                ([1], True),
                ([2], True),
                ([1,2], False),
                ([2,1,6], False),
                ([1,2,3], False)
                ]
TEST_CASES.extend([x[0] for x in TEST_PARITY_TEST])


def test_algorithm(alg):
    '''input: a function that takes in a list of heights'''
    failed = False
    for test in TEST_CASES:
        nums_parity = alg(test)
        resp = test_parity(nums_parity)
        if not resp:
            failed=True
            print("----------")
            print('wrong')
            print("test case", test)
            print(alg.__name__,nums_parity)
            print("----------")
        else:
            print("test case", test)
    if not failed:
        print()
        print(alg.__name__,"all test cases passed")

test_algorithm(parity)
