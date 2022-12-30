from typing import List, Tuple
print("The Tower of Hanoi is a famous problem which was posed by a French mathematician in 1883."
        "What you need to do is move all the disks from the left hand post to the right hand post."
        "You can only move the disks one at a time and you can never place a bigger disk on a smaller disk.\n")
MOVE_LIMIT = 10000

def get_end(start: int, end: int):
    locations= [0,1,2]
    locations.remove(start)
    if start!=end:
        locations.remove(end)
    return  locations[0]

def find_biggest(pegs: List[List[int]], start: int, end: int) -> Tuple[int]:
    """finds the next big ring to move. compares the largest rings on the non-ending pegs"""
    tmp_peg = get_end(start, end)
    if max(pegs[start], default=-1) > max(pegs[tmp_peg], default=-1):
        return (pegs[start][0], start, end)
    elif max(pegs[start], default=-1) < max(pegs[tmp_peg], default=-1):
        return (pegs[tmp_peg][0], tmp_peg, end)
    else:
        ##return invalid values to indicate the two pegs are empty and we're done
        return (0, -1, -1)

def move_pegs(pegs: List[List[int]], ring: int, start: int, end: int, verbose: bool = True) -> int:
    '''input:
    pegs: list of lists of ints. each inner list represents a peg. the ints are the size rings on the peg.
    ring: which ring to move
    start: peg ring is starting on
    end:   peg ring is ending on
    return: the number of moves'''
    ##track the number of moves as a single int in an array so that its an object and python will do pass by object.
    assert start!=end, "not setup for start peg equaling ending peg"
    assert min(pegs[start])>0, "ring ints are sizes and thus > 0"
    limit = [0] 
    while ring>0:
        if verbose:
            print("move pegs: ring", ring, "start", start, "end", end)
        ##0 indicates done moving
        move(pegs, ring, start, end, limit, verbose)
        ring, start, end = find_biggest(pegs, start, end)
    if verbose:
        print("moves", limit[0])
    return limit[0]


def move(pegs: List[List[int]], ring: int, start: int, end: int, limit: List[int], verbose: bool = True) -> None:
    '''input:
    pegs: list of lists of ints. each inner list represents a peg. the ints are the size rings on the peg.
    ring: which ring to move
    start: peg ring is starting on
    end:   peg ring is ending on'''
    if limit[0] >MOVE_LIMIT:
        print("Error: Could not be solved in less than ", MOVE_LIMIT,"moves")
        return
    if verbose:
        print(f'goal: ring {ring} start {start} end {end}')
    ring_index = pegs[start].index(ring)
    ##there are rings above it, move them out of the way
    if ring_index < len(pegs[start])-1:
        ring_n = pegs[start][ring_index+1]
        start_n = start
        end_n = get_end(start, end)
        move(pegs, ring_n , start_n, end_n, limit, verbose)
        move(pegs, ring, start, end, limit, verbose)
    ##there are no rings above it
    elif ring_index == len(pegs[start])-1:
        ##sinlge move from start to end is valid
        if len(pegs[end])==0 or pegs[end][-1] > ring:
            pegs[end].append(pegs[start].pop())
            limit[0] += 1
            if verbose:
                print("move", limit[0])
        ##destination has a smaller disk already there
        elif pegs[end][-1] < ring:
            ##you can never place a bigger disk on a smaller disk
            ind = 0
            while pegs[end][ind] > ring:
                ind +=1
            ring_n = pegs[end][ind]
            start_n = end
            end_n = get_end(start, end)
            move(pegs, ring_n , start_n, end_n, limit, verbose)
            move(pegs, ring, start, end, limit, verbose)
        else:
            raise Exception("two peg values are the same", pegs)

    else:
        a = "the position in the list cannot be greater than indices in list\n"
        raise Exception('{a}pegs {pegs} ring {ring} start {start} end {end}')

def check_descending(peg:List[int]) -> bool:
    '''checks if the pegs are stacked correctly'''
    if not peg:
        return False
    for i in range(len(peg)-1):
        if peg[i]<peg[i+1]:
            return False
    return True

def test_one(verbose: bool = True):
    '''manually defining a test'''
    test_cases = [[[3,2,1], 0, 2],
                    [[3,2,1], 2, 0],
                    [[3,2,1], 1, 2],
                    [[3,2,1], 2, 1],
                    [[3,2,1], 0, 1],
                    [[3,2,1], 1, 0],
                    [[1,2,3], 1, 0],
                    [[2,1,3], 1, 0],
                    [[3,1,2], 1, 0],
                    [[6,5,4], 0, 1],
                    ]
    rings = 3
    failed=False
    for test in test_cases:
        stack = test[0]
        pegs = [[], [], []]
        end = test[2]
        start=test[1]
        pegs[start] = stack
        moves = move_pegs(pegs, max(pegs[start]), start, end, verbose=False)
        if not check_descending(pegs[end]):
            print()
            print("start", start, "end", end)
            print(test)
            print("pegs after",pegs)
            print("Error: rings stacked incorrectly\n", pegs)
            failed=True
        if moves > (pow(2,rings)-1):
            print()
            print("start", start, "end", end)
            print(test)
            print("pegs after",pegs)
            print("Error: sequence of moves took too long")
            print("moves for",rings," rings" , "expected", (pow(2,rings)-1), "got", moves)        
    if not failed:
        print("\nall tests produced correct outcome")

def test():
    '''automatically generating tests'''
    passed = True
    for rings in range(3,10):
        stack = [rings-x for x in range(rings)]
        pegs = (stack, [], [])
        end = 2
        start =0 
        moves = move_pegs(pegs, rings, start, end, verbose=False)        
        if moves != (pow(2,rings)-1):
            print("error: moves for rings", rings, "expected", (pow(2,rings)-1), "got", moves)
            passed = False
        if not check_descending(pegs[end]):
            print("error: incorrect stack result", pegs)
            passed = False
            
    if passed:
        print("\nall automated tests passed")
if __name__=='__main__':
    test_one()
    test()