import numpy as np
def zig_zag(numbers, i):
    if (numbers[0+i]>numbers[1+i]<numbers[2+i]) or (numbers[0+i]<numbers[1+i]>numbers[2+i]):
        return 1
    else:
        return 0
        
def solution(numbers):
    ct = len(numbers)
    assert 3<= ct <=100
    ret = np.zeros(ct-2)
    for i in range(ct-2):
        ret[i] = zig_zag(numbers, i)

    return ret