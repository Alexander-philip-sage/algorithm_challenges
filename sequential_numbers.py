'''find the list of sequential numbers in a list of unordered numbers'''
#%%
import numpy as np
import datetime
import matplotlib.pyplot as plt
from typing import List
def seq_numbers(arr: List[int]):
    '''arr: unordered list'''
    if len(arr)<=1:
        return False
    ##O(n)
    track = {x:0 for x in arr}
    final_left=0
    final_right=0
    ##O(n)

    for num in list(track.keys()):
        if track[num]==0:
            track[num]=1
            left  = num
            right = num
            while (left-1) in track.keys():
                left -=1
                track[left]=1
            while (right+1) in track.keys():
                right +=1
                track[right]=1
        if (right -left)>(final_right-final_left):
            final_left=left
            final_right=right

    if final_left==final_right:
        return False
    else:
        return final_right - final_left+1

def sort_seq_numbers(arr: List[int]):
    '''arr: unordered list'''
    if len(arr)<=1:
        return False
    ##O(nlog(n))
    arr.sort()
    seq =0
    tmp_seq = 0
    in_seq = False
    ##O(n)
    for i, val in enumerate(arr):
        if i==0:
            continue
        if arr[i-1]==val-1:
            tmp_seq +=1
        elif arr[i-1]==val:
            continue
        else:
            if tmp_seq>seq:
                seq = tmp_seq
            tmp_seq=0
    if tmp_seq>seq:
        seq = tmp_seq
    if seq >0:
        return seq +1
    else:
        return False

tests = [([1, 3,4,5,6, 9],4),
        ([x for x in range(3,7)],4),
        ([9,3,1,4,8,5],3),
        ([-1,0,1,2],4),
        ([2,-1,1,0],4),
        ([0,9,-3,1,-3,5,-2,-75,4],2),
        ([1, 3,4,5,6, 9,10,11,12,13],5),
        ([-6 ,-1  ,0  ,2  ,4  ,4  ,4  ,6  ,7],2),
        ([-2 ,-1, -9, -6,  9],2),
        ([7,6],2),
        ([ 6  ,7 , 4,  5, -2 , 4],4),
        ([6,-10,-7,-1,-5,-4,-3,5,3,3,7,3,9,2,-9,-3,-5,-1,-1,5,-10,-4,0,-8,7,2,7,8,8,7,0,5,5,-1,-8,-8,0,-4,5,9,0,-8,-8,8,8,4,3,-3,-4,-10,-4,-5,-9,-6,-9,-5,-1,-7,4,6,0,7,-3,5,-1,-7,-5],8)
        ]

def manual_test(func):
    print("testing", print(func.__name__))
    for inp, ans in tests:
        res = func(inp)
 
        if res!=ans:
            print("**********")
            print(func.__name__)
            print("incorrect")
            print(inp)
            print("answer", ans)
            print("result", res)    

def scaling_tests(ct_tests, max_size):
    x = []
    n_logn_p_n = []
    hash_sol = []
    sort_sol = []
    n_p_n=[]
    for i in range(ct_tests):
        arr_size = np.random.randint(0,max_size)
        inp = np.random.randint(-10,10,size=arr_size)
        start = datetime.datetime.now()
        res = seq_numbers(inp.copy())
        total_s = (datetime.datetime.now() - start).microseconds
        hash_sol.append(total_s)
        start = datetime.datetime.now()
        res2 = sort_seq_numbers(inp.copy())
        total_s = (datetime.datetime.now() - start).microseconds
        sort_sol.append(total_s)
        if res !=res2:
            print("mismatch answers")
            print("\t", inp)
            print("\tsort_seq_numbers:", res2)
            print("\tseq_numbers:", res)
        x.append(arr_size)
        if arr_size!=0:
            n_logn_p_n.append(arr_size*np.log10(arr_size)+arr_size)
        else:  
            n_logn_p_n.append(0)
        n_p_n.append(2*arr_size)
    plt.scatter(x=x, y=hash_sol, label="hash_sol")
    plt.scatter(x=x, y=n_logn_p_n, label="O(nlogn plus n)")
    plt.scatter(x=x, y=n_p_n, label="O(2n)")
    plt.scatter(x=x, y=sort_sol, label="sort_sol")
    plt.ylabel('.microseconds')
    plt.xlabel("array_size")
    ax=plt.gca()
    ax.legend()
    

if __name__=='__main__':

    #manual_test(seq_numbers)
    #manual_test(sort_seq_numbers)
    scaling_tests(50,100000)
# %%
test = [-10, -10, -10, -9, -9, -9, -8, -8, -8, -8, -8, -7, -7, -7, -6, -5, -5, -5, -5, -5, -4, -4, -4, -4, -4, -3, -3, -3, -3, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9]
test.sort()
#print(list(set(test)))