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
            ]

def longest_path(mat):
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

def step(mat, path,N, row, col):
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
    print("my solution")
    print(longest_path(test[0]))
    print("internet solution")
    MaximumPath(test[0])
    print("answer", test[1])
    print()