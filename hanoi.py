print("The Tower of Hanoi is a famous problem which was posed by a French mathematician in 1883."
        "What you need to do is move all the disks from the left hand post to the right hand post."
        "You can only move the disks one at a time and you can never place a bigger disk on a smaller disk.\n")

def get_end(start, end):
    locations= [0,1,2]
    locations.remove(start)
    locations.remove(end)
    return  locations[0]

def find_biggest(pegs):
    """finds the next big ring to move"""
    if max(pegs[0], default=-1) > max(pegs[1], default=-1):
        return (pegs[0][0], 0, 2)
    elif max(pegs[0], default=-1) < max(pegs[1], default=-1):
        return (pegs[1][0], 1, 2)
    else:
        return (0, -1, -1)

def move_pegs(pegs, ring, start, end, verbose=True):
    limit = [0] 
    while ring>0:
        if verbose:
            print("move pegs: ring", ring, "start", start, "end", end)
        ##0 indicates done moving
        move(pegs, ring, start, end, limit, verbose)
        ring, start, end = find_biggest(pegs)
    if verbose:
        print("moves", limit[0])
    return limit[0]

def move(pegs, ring, start, end, limit, verbose=True):
    if limit[0] >10000:
        print("broken")
        return
    ##check if can move
    if verbose:
        print(f'goal: ring {ring} start {start} end {end}')
    order = pegs[start].index(ring)
    if order < len(pegs[start])-1:
        ##move ones above
        ring_n = pegs[start][order+1]
        start_n = start
        end_n = get_end(start, end)
        move(pegs, ring_n , start_n, end_n, limit, verbose)
        move(pegs, ring, start, end, limit, verbose)
    elif order == len(pegs[start])-1:
        if len(pegs[end])==0 or pegs[end][-1] > ring:
            pegs[end].append(pegs[start].pop())
            limit[0] += 1
            if verbose:
                print("move", limit[0])
        ##check destination
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

def test_one():
    rings = 3
    stack = [rings-x for x in range(rings)]
    pegs = (stack, [], [])
    print(pegs)
    moves = move_pegs(pegs, rings, 0, 2, verbose=False)
    print(pegs)
    if moves != (pow(2,rings)-1):
        print("error")
    print("for rings", rings, "expected", (pow(2,rings)-1), "got", moves)        

def test():
    passed = True
    for rings in range(3,10):
        stack = [rings-x for x in range(rings)]
        pegs = (stack, [], [])
        moves = move_pegs(pegs, rings, 0, 2, verbose=False)        
        if moves != (pow(2,rings)-1):
            print("error for rings", rings, "expected", (pow(2,rings)-1), "got", moves)
            passed = False
    if passed:
        print("all tests passed")
if __name__=='__main__':
    test_one()
    test()