from sklearn import metrics 
import numpy as np
from typing import List
import math
def print_scores(mymi, npmi):
    print("my mi\t\t", round(mymi,2))
    print("mutual_info_score", round(npmi,2))

TEST_CASES=[
            ((0, 0, 1, 1, 0, 1, 1, 2, 2, 2), (3, 4, 5, 5, 3, 2, 2, 6, 6, 1)),
            ((0, 0,  0), (3, 3,3 )),
            ((0, 0,  0), (0, 0, 0)),
            ((1, 1,  1), (1, 1, 1)),
            ((0, 1,  0), (1, 0, 1)),
            ((1, 1,  0), (1, 1, 1)),
            ((1, 1,  0), (1, 1, 1)),
            ((1), (1)),
            ((0), (0)),
            ]
def manual_tests():
    for x,y in TEST_CASES:
        print()
        print(x,y)
        try:
            mymi =mi(x, y)
            npmi=metrics.mutual_info_score(x, y)
        except Exception as e: 
            print(e)
        print_scores(mymi, npmi)

def test_loop(tests = 20):
    print("automated test")
    succ = 0
    for i in range(tests):
        array_size = np.random.randint(1,30)
        x = np.random.randint(0, 10, size=array_size)
        assert x.shape[0]==array_size
        assert len(x.shape)==1
        y = np.random.randint(0, 10, size=array_size)
        test_succ = ( abs(mi(x, y)- metrics.mutual_info_score(x, y)) < 0.0001)
        succ += test_succ
        if not test_succ:
            print("my mi", mi(x, y))
            print("mutual_info_score", metrics.mutual_info_score(x, y))
    print("auto-generated inputs")
    print("acc %%%.1f" % (succ*100/tests))

def cast_check_np_array(x) -> np.ndarray:
    if type(x) != np.ndarray:
        x_n = np.array(x)
    else:
        x_n = x
    assert(len(x_n.shape) ==1), "arrays must be 1d you gave "+str(x_n.shape)
    assert(x_n.shape[0] > 0), "array must not be empty "+str(x_n.shape)
    return x_n

def mi(xlist: np.ndarray[int], ylist: np.ndarray[int]) -> float:
    total = 0
    xlist = cast_check_np_array(xlist)
    ylist = cast_check_np_array(ylist)
    uniqx = np.unique(xlist)
    uniqy = np.unique(ylist)
    if len(uniqx)==1 and len(uniqx)==1:
        return 0
    size = xlist.shape[0]
    assert xlist.shape[0]== ylist.shape[0], "input arrays must be same size"
    for xi, x in enumerate(uniqx):
        indices_x = np.where(x==xlist)[0]
        px = indices_x.shape[0]/size
        for yi, y in enumerate(uniqy):
            indices_y = np.where(y==ylist)[0]
            py = indices_y.shape[0]/size

            bl = np.isin(indices_x, indices_y)
            sumbl = sum(bl)
            pxy = sumbl/size
            if sumbl < 0:
                print("sumbl< 0", sumbl)
            if pxy > 0:
                total +=pxy * math.log((pxy / (px*py)), math.e)
    return total

if __name__=="__main__":
    manual_tests()
    test_loop()
    #print("normalized_mutual_info_score", metrics.normalized_mutual_info_score(x, y))
