'''You must create a function that can read matrix of numbers stored in an array which will be a 2D matrix that contains only the integers 1, 0, or 2. Then from the position in the matrix where a 1 is, return the number of spaces either left, right, down, or up you must move to reach an enemy which is represented by a 2
You are able to wrap around one side of the matrix to the other. For example if array is [“0000”, “1000”, “0002”, “0002”] then this is the board
For this board your program should return 2 because the closest enemy (2) is 2 spaces away from the 1 by moving left to wrap to the other side and then moving down once. The array will contain any number of 0’s and 2’s, but only a single 1. It may not contain any 2’s at all as well, where in that case your program should return a 0.
Input: [“000”, “100”, “200”] | Output: 1
Input: [“0000”, “2010”, “0000”, “2002” ] | Output: 2
'''
from typing import List
def closest_enemy(grid: List[str])->int:
    '''finds the closest 2 to the 1
    input: List of strings
    return: distance to the 2'''
    one_pos = None
    two_positions = []
    for i, rowstr in enumerate(grid):
        for j, colchr in enumerate(rowstr):
            if colchr=='2':
                two_positions.append((i,j))
            elif colchr=='1':
                ##should only be one 1
                if one_pos:
                    return 0
                one_pos=(i,j)
    if len(two_positions)==0:
        return 0
    closest_distance = pow(10,6)
    closest_i = None
    for i, pos in enumerate(two_positions):
        row_dist = abs(pos[0]-one_pos[0])
        if row_dist>len(grid)//2:
            if pos[0] > one_pos[0]:
                row_dist = len(grid)-pos[0]+one_pos[0]
            else:
                row_dist = len(grid)+pos[0]-one_pos[0]        
        col_dist = abs(pos[1]-one_pos[1])
        if col_dist>len(grid[0])//2:
            if pos[1]>one_pos[1]:
                col_dist = len(grid[0])-pos[1]+one_pos[1]
            else:
                col_dist = len(grid[0])+pos[1]-one_pos[1]
        if col_dist+row_dist<closest_distance:
            closest_distance = row_dist+col_dist
            closest_i = i
    return closest_distance

TEST_CASES = [
    (["000", 
      "100", 
      "200"], 1),
    (["0000", 
      "2010", 
      "0000",
      "2002"], 2),
    (["0000", 
      "0010", 
      "0000",
      "0000"], 0),
    (["0000", 
      "0000", 
      "0000",
      "0000"], 0),
    (["2000", 
      "0001", 
      "0000",
      "0000"], 2),
    (["0001", 
      "0000", 
      "0000",
      "0020"], 2),
    (["0001", 
      "0000", 
      "0200",
      "0000"], 4),
    (["200000", 
      "000010", 
      "020000",
      "000000"], 3),
    (["100000", 
      "000020", 
      "020000",
      "000000"], 3),
    (["000000", 
      "000010", 
      "000000",
      "020000"], 5),

]
if __name__=='__main__':
    all_passed = True
    for val, sol in TEST_CASES:
        ret = closest_enemy(val)
        if ret!=sol:
            all_passed=False
            print("Failed: \n\tvalue:", val,"\n\tsolution:" ,sol,"\n\tresult:", ret)
    if all_passed:
        print("passed all test cases")