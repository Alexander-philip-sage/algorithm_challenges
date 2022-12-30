from typing import List
def rec(one: List[int], two: List[int]) -> List[int]:
    three = []
    if len(one) >=2 or len(two)>=2:
        split = len(one)//2
        one = rec(one[:split], one[split:])
        split = len(two)//2
        two = rec(two[:split], two[split:])        
    e =0
    w = 0
    while len(one)>e or len(two)>w:
        if len(one)==e:
            three.append(two[w])
            w+=1
        elif len(two)==w:
            three.append(one[e])
            e+=1
        elif one[e]<two[w]:
            three.append(one[e])
            e+=1
        elif one[e]>two[w]:
            three.append(two[w])
            w+=1
        elif one[e]==two[w]:
            three.extend([one[e],two[w]])
            w+=1
            e+=1
    return three
    
def merge_sort(var: List[int]) -> List[int]:
    '''implementing the merge sort algorithm
    https://en.wikipedia.org/wiki/Merge_sort'''
    if len(var) <=1:
        return var
    split = len(var)//2
    sorted = rec(var[split:], var[:split])
    return sorted


import numpy as np
ct_tests = 1000
failed = False
for i in range(ct_tests):
    test = list(np.random.randint(-10,10,np.random.randint(0,10)))
    #test = [0, 7, 2, 4, 8, 0, 5]
    answer = test.copy()
    answer.sort()
    #print("input", test)
    #print("answer", answer)
    resp = merge_sort(test)

    if resp!=answer:
        failed=True
        print("----------")
        print("test", i, "false")
        print("input", test)
        print("answer", answer)
        print("result", resp)
        print("----------")
if not failed:
    print("all test cases passed")