from typing import List, Tuple
'''Given a N X N matrix Mat[N][N] of positive integers. There are only three possible moves from a cell (i, j) 

(i+1, j)
(i+1, j-1)
(i+1, j+1)
Starting from any column in row 0, return the largest sum of any of the paths up to row N-1
test_case
Input : mat[4][4] = [ [4, 2, 3, 4],
                      [2, 9, 1, 10],
                      [15, 1, 3, 0],
                      [16, 92, 41, 44] ];
Output :120
path : 4 + 9 + 15 + 92 = 120'''

test_cases = [([ [4, 2, 3, 4],
                [2, 9, 1, 10],
                [15, 1, 3, 0],
                [16, 92, 41, 44] ],120),
            ([ [0, 0, 0, 0],
                [0, 1, 2, 3],
                [0, 2, 3, 4],
                [100, 0, 1, 2] ],104),
            ([[1,0,1,0],
              [0,3,1,1],
              [2,1,5,6],
              [1,0,1,9],],18),
            ([[3,0,1,0],
              [0,3,1,1],
              [3,1,1,0],
              [1,3,1,2],],12),
            ([[1,0,0,1],
              [0,2,3,1],
              [2,5,4,3],
              [1,0,9,4],],9+5+3+1),
            ([[1,0,3,0],
              [0,3,1,1],
              [3,1,4,0],
              [1,3,1,2],],3+3+4+3),
            ]

def longest_path(mat: List[List[int]]) -> Tuple[int, List[int]]:
    '''this solution calls a recursive function that steps through all the possible paths, 
    saving all of them and looking for the largest paths. Its nice for using with a 
    debugger to see how it works as it creates, compares, and saves paths'''
    paths = []
    distances = []
    assert type(mat)==list
    assert type(mat[0])==list
    N = len(mat)
    row = 0

    for i in range(N):
        col = i
        path = [mat[row][col]]
        dist, path = step(mat, path,N, row, col)
        distances.append(dist)
        paths.append(path)
    best_dist = max(distances)
    best_path = paths[distances.index(best_dist)]
    return best_dist, best_path

def step(mat: List[List[int]], path: List[int],N: int, row: int, col: int) -> Tuple[int, List[int]]:
    '''algorithm: first check if you are at the last row - if so, return.
        if not at the last row - then try all three types of steps.
    this could easily be modified to be faster by not tracking all the paths, and the code could be 
    shorter by removing all the single use variables, but this makes it more fun to read with a debugger'''
    if row>=N-1:
        return sum(path),path
    paths = []
    distances = []    
    if col>0:
        row1 =row+1
        col1=col-1
        path_tmp = path.copy()
        path_tmp.append(mat[row1][col1])
        dist1 , path1 = step(mat, path_tmp,N, row1, col1)
        distances.append(dist1)
        paths.append(path1)
    if col <N-1:
        row2 =row+1
        col2 =col+1
        path_tmp = path.copy()
        path_tmp.append(mat[row2][col2])
        dist2 , path2 = step(mat, path_tmp,N, row2, col2)
        distances.append(dist2)
        paths.append(path2)
    row3 =row+1
    col3 =col
    path_tmp = path.copy()
    path_tmp.append(mat[row3][col3])
    dist3 , path3 = step(mat, path_tmp,N, row3, col3)
    distances.append(dist3)
    paths.append(path3)
    best_dist = max(distances)
    best_path = paths[distances.index(best_dist)]
    return best_dist, best_path

##internet copied solution
def MaximumPath(Mat):
    N = len(Mat)
    result = 0
 
    # create 2D matrix to store the sum
    # of the path
    # initialize all dp matrix as '0'
    dp = [[0 for i in range(N+2)] for j in range(N)]
 
    # copy all element of first row into
    # dp first row
    for i in range(N):
        for j in range(1, N+1):
            dp[i][j] = max( dp[i-1][j-1],
                           max(dp[i-1][j],dp[i-1][j+1]) 
                           ) + Mat[i][j-1]
 
    # Find maximum path sum that end ups
    # at any column of last row 'N-1'
    for i in range(N+1):
        result = max(result, dp[N-1][i])

    # return maximum sum path
    return result
 


for test in test_cases:
    my_sol = longest_path(test[0])
    int_sol = MaximumPath(test[0])
    print("\nmy path found")
    print(my_sol[1])
    if my_sol[0]==int_sol==test[1]:
        print("my solution and internet solution are correct")
    elif  my_sol[0]!=test[1]:
        print("Failed")
        print("my sol", my_sol[0])
        print("answer", test[1])
    elif  int_sol!=test[1]:
        print("Failed")
        print("internet sol", int_sol)
        print("answer", test[1])
