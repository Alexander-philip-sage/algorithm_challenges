challenge_prompt = ("""
Challenge: 
    input: List[char]
            a list of single char strings and a binary number 
            represented as 1s and 0s in a str. the char can be ? or +. 
    algorithm: for every ? count the number of ones in the binary number. The len of the digits in the number must stay constant. 
            It must run quickly. every + means add 1 to the number.
    return: List[int]
            list of ints where each is a response to each ?. The length of the return list will be the same length as the number of ? 
            in the request list, not necessarily the same length of the request list""")
print(challenge_prompt)
import numpy as np

def solve_as_str(request, bin_str):
    print(request, bin_str)

if __name__=="__main__":
    for i in range(10):
        request_size = np.random.randint(1,10)
        binary_size =  np.random.randint(1,10)
        request = []
        bin_str = ['0' for x in range(binary_size)]
        for j in range(binary_size):
            if 0.5 < np.random.rand():
                bin_str[j] = '1'
        for j in range(request_size):
            if 0.5 < np.random.rand():
                request.append('?')
            else:
                request.append('+')

        solve_as_str(request, ''.join(bin_str))





