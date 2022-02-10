from sklearn import metrics 
import numpy as np
metrics.normalized_mutual_info_score
import math

def test1():
    print("test1")
    x, y = (0, 0, 1, 1, 0, 1, 1, 2, 2, 2), (3, 4, 5, 5, 3, 2, 2, 6, 6, 1)
    print("my mi", mi(x, y))
    print("mutual_info_score", metrics.mutual_info_score(x, y))

def test2():
    print("test2")
    x, y = (0, 0,  0), (3, 3,3 )
    print("my mi", mi(x, y))
    print("mutual_info_score", metrics.mutual_info_score(x, y))
def test3():
    print("test3")
    x, y = (0, 0,  0), (0, 0, 0)
    print("my mi", mi(x, y))
    print("mutual_info_score", metrics.mutual_info_score(x, y))



def manual_tests():
    test1()
    test2()
    test3()

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

def cast_check_np_array(x):
    if type(x) != np.ndarray:
        x_n = np.array(x)
    else:
        x_n = x
    assert(len(x_n.shape) ==1), "arrays must be 1d you gave "+x_n.shape
    assert(x_n.shape[0] > 0), "array must not be empty "+x_n.shape
    return x_n

def mi(xlist, ylist):
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
            if pxy > 0:
                total +=pxy * math.log((pxy / (px*py)), math.e)
            if sumbl < 0:
                print("sumbl< 0", sumbl)
    return total

if __name__=="__main__":
    manual_tests()
    test_loop()
    #print("normalized_mutual_info_score", metrics.normalized_mutual_info_score(x, y))
