from typing import List, MutableSet
PROBLEM = '''Given a number of paranthese pairs. make all the combinations that could be considered valid.
            a valid parantheses pair always has left bracket come before their closing right bracket'''

TEST_CASES = [
        (0,set([''])),
        (1,set(['()'])),
        (2,set(['()()','(())'])),
        (3,set(['((()))', '(()())', '(())()', '()(())', '()()()'])),
        (4,set(['()()()()', '(((())))', '(())(())', '()((()))', '((()))()', 
            '(()())()', '(())()()', '()(())()','()()(())','()(()())', 
            '(()()())', '((())())', '((()()))', '(()(()))'] )),
        ]

def brackets(n_pairs: int, left: int=0, right: int=0, combo: str='', combos: MutableSet[str]=set([])) -> List[str]:
    '''input: number of bracket pairs
    return: a list of strings containing the combinations'''
    if left<n_pairs:
        brackets(n_pairs, left+1, right, combo+'(', combos)
    if right < n_pairs and right<left:
        brackets(n_pairs, left, right+1, combo+')', combos)
    if right==n_pairs and left==n_pairs:
        combos.add(combo)
    return combos

if __name__=='__main__':
    failed = False
    for test in TEST_CASES:
        res = brackets(test[0], combos=set([]))
        if res!=test[1]:
            failed = True
            print()
            print(test)
            print("result", res)
            print("those in result, not in answer", res-test[1])
            print("those in answer, not in result", test[1]-res)
    if not failed:
        print('all tests passed')
        print("example of three pairs")
        print(TEST_CASES[3])