from typing import List
import numpy as np
import time
##/home/sage/Documents/little_projects/pyplay/bin/python3 -m cProfile  -s tottime binary_count.py > binary_profile.txt

ADD = 'ADD'
COUNT = 'COUNT'
challenge_prompt = ("""
Challenge: 
    input: List[char]
            a list of single char strings and a binary number 
            represented as 1s and 0s in a str. the char can be 'COUNT' or 'ADD'. 
    algorithm: for every 'COUNT' COUNT the number of ones in the binary number. The len of the digits in the number must stay constant. 
            It must run quickly. every 'ADD' means ADD 1 to the number.
    return: List[int]
            list of ints where each is a response to each 'COUNT'. The length of the return list will be the same length as the number of 'COUNT'
            in the request list, not necessarily the same length of the request list\n""")

print(challenge_prompt)


def count_ones_loop(bin_str: str) -> int:
    ct = 0
    for val in bin_str:
        if val=='1':
            ct +=1
    return ct
def count_ones_method(bin_str: str) -> int:
    return bin_str.count('1')

def add_str(bin_str: str, verbose: bool):
    bits = list(bin_str)
    if verbose:
        print("add")
        print(bin_str)
    set_one = False
    for i in range(len(bits)):
        if bits[-i-1] =='1':
            bits[-i-1] = '0'
        elif bits[-i-1] =='0':
            bits[-i-1] = '1'
            set_one = True
            break
        else:
            raise ValueError("only allows values 0 or 1 in binary")
    if not set_one:
        bits[-1] = '1'
    bin_str = ''.join(bits)
    if verbose:
        print(bin_str, "\n")
    return bin_str

def add_bin(bin_str: str, verbose: bool, modu: int, len_str: int):
    dec = int(bin_str, 2)
    if verbose:
        print("add")
        print(bin_str, dec)
    bin_str = format((dec+1)%modu, 'b').zfill(len_str)
    return bin_str

def solve_as_bin(requests: List[str], bin_str: str, verbose=False) -> List[int]:
    bin_str_orig = bin_str
    ret = []
    len_str = len(bin_str)
    modu = pow(2,len_str)
    for req in requests:
        if req==ADD:
            bin_str = add_bin(bin_str, verbose, modu, len_str)
            if verbose:
                print(bin_str)

        elif req==COUNT:
            ct = count_ones_method(bin_str)
            if verbose:
                print(bin_str, 'count', ct)
            ret.append(ct)
        else:
            raise ValueError("only ADD and COUNT are acceptable request types")
    assert len(bin_str) == len(bin_str_orig), "size of binary cannot change"
    return ret

def solve_as_str(requests: List[str], bin_str: str, verbose=False) -> List[int]:
    bin_str_orig = bin_str
    ret = []
    for req in requests:
        if req==ADD:
            bin_str = add_str(bin_str, verbose)
        elif req==COUNT:
            ct = count_ones_loop(bin_str)
            if verbose:
                print(bin_str, 'count', ct)

            ret.append(ct)
        else:
            raise ValueError("only ADD and COUNT are acceptable request types")
    assert len(bin_str) == len(bin_str_orig), "size of binary cannot change"
    return ret

def random_data():
    request_size = np.random.randint(1,700)
    binary_size =  np.random.randint(1,700)
    requests = []
    bits = ['0' for x in range(binary_size)]
    for j in range(binary_size):
        if 0.5 < np.random.rand():
            bits[j] = '1'
    for j in range(request_size):
        if 0.5 < np.random.rand():
            requests.append(COUNT)
        else:
            requests.append(ADD)
    return requests, ''.join(bits)


if __name__=="__main__":
    test_dataset = []
    for i in range(100):
        test_dataset.append( random_data())
    start = time.perf_counter()
    for requests, bin_str in test_dataset:
        solve_as_str(requests, bin_str, verbose=False)
    end = time.perf_counter()
    print("time to run solve as str", (end - start))

    start = time.perf_counter()
    for requests, bin_str in test_dataset:
        solve_as_bin(requests, bin_str, verbose=False)
    end = time.perf_counter()
    print("time to run solve as bin", (end - start))





