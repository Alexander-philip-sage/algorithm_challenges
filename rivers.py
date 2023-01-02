from typing import List, Tuple, MutableSet
'''a river is a series of ones touching. input is a matrix. river size is the sum of all the touching ones. create a list of all rivers and return size of the biggest'''
TESTS = [
        ([[1,0,0,1],
          [1,1,0,1],
          [0,1,0,1],
          ] ,4),
        ([[1,0,0,0],
          [0,1,0,0],
          [0,0,1,0],
          ] ,3),
        ([[0,0,0,1],
          [0,0,1,0],
          [0,1,0,0],
          ] ,3),
        ([[1,0,0,1],
          [0,1,0,1],
          [0,1,0,0],
          ] ,3),
        ([[1,0,0,1],
          [0,1,0,1],
          [0,0,1,0],
          ] ,5),
        ([[0,1,0,0],
          [1,0,1,0],
          [0,0,0,1],
          ] ,4),
        ([[1,0,0,1],
          [0,1,0,1],
          [0,0,0,1],
          ] ,3),
        ([[0,0,0,1],
          [0,1,0,0],
          [0,0,0,1],
          ] ,1),
        ([[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          ] ,0),
        ([[0,0,0,0],
          [0,1,0,0],
          [0,1,0,0],
          ] ,2),
        ([[1,0, 0,0,1],
          [1,1,0, 0,1],
          [0,1,1, 0,1],
          [0,0,1, 0,1],
          [0,0,0, 0,0],
          [1,1,1, 1,1],
          ] ,6),
        ([[1,0, 0,0,1],
          [1,1,0, 0,1],
          [0,1,0, 0,1],
          [0,0,0, 0,1],
          [0,0,0, 0,0],
          [1,1,1, 1,1],
          ] ,5),
        ([[1,1,0,0],
          [0,0,0,0],
          [0,0,0,1],
          [0,0,1,1],
          [0,1,1,1]],6),
        ([[1,1,0,0],
          [0,0,0,0],
          [0,0,0,1],
          [0,0,0,1],
          [0,1,1,1]],5),
        ([[0,0,0,1],
          [0,0,0,1],
          [0,0,0,1],
          [0,1,0,1],
          [0,0,1,1]],7),
        ([[0,0,0],
          [0,0,1],
          [0,1,1],
          [0,1,0],], 4),

        ]
class Topography():
  def __init__(self, topography: List[List[int]]):
    self.topography = topography
    self.glength =0 
  def set_glength(self, glength: int):
    self.glength = glength

def find_longest_river(topography: List[List[int]]):
  topo = Topography(topography)
  rstep(0,0,0,topo)
  return topo.glength

def rstep(col: int, row: int, length: int, topo: Topography):
  '''glength is the globally longest river in the topography
  topo is a matrix with either ones or zeros representing river or land
  returns: glength'''
  ##at right corner. no where else to search
  at_corner = ((col == len(topo.topography[0])-1) and (row == len(topo.topography)-1))
  if (topo.topography[row][col]==0) or at_corner:
    if length > topo.glength:
      topo.glength = length
    length = 0
  if (topo.topography[row][col]==1):
    length +=1
  if not at_corner:
    if (col < len(topo.topography[0])-1) and (row < len(topo.topography)-1):
      ncol = col +1
      nrow = row +1
      rstep(ncol, nrow, length, topo)    
    if (col >0) and (row < len(topo.topography)-1):
      ncol = col -1
      nrow = row +1
      rstep(ncol, nrow, length, topo)    
    if (row < len(topo.topography)-1):
      nrow = row +1
      rstep(col, nrow, length, topo)    
    if (col < len(topo.topography[0])-1) :
      ncol = col +1
      rstep(ncol, row, length, topo)    

def possible_edges(pos: Tuple[int], checked: MutableSet[Tuple[int]], edges: List[Tuple[int]], river: List[Tuple[int]], topography):
  if pos not in checked:
    checked.add(pos)
    if topography[pos[0]][pos[1]]==1:
      edges.append(pos)
      river.append(pos)

def count_rivers(topography: List[List[int]]):
    '''input: topography: a list of lists of ints that make up a matrix of topography, either 0s or 1s
    return max river length
    algorithm: tracks the positions on topography that have been visited. loops through every position in O(n) 
        then if it finds a rivier edge, it traverses the topography to find all the adjacent rivers blocks.
        meaning that most positions with a river are visited twice, once by the for loop and once by the traversal
         '''
    checked = set()
    rivers = []
    for i in range(len(topography)):
        for j in range(len(topography[i])):
            pos = (i,j)
            val = topography[i][j]
            if pos in checked or topography[i][j]==0:
                continue
            edges = [pos]
            river = [pos]
            checked.add(pos)
            while edges:
                edge = edges.pop()
                y = edge[0]
                x = edge[1]

                ##up right
                if y>0 and x < (len(topography[y])-1):
                    possible_edges((y-1,x+1), checked, edges, river,topography)
                ##up left
                if y>0 and x > 0:
                    possible_edges((y-1,x-1), checked, edges, river,topography)
                ##up 
                if y>0 :
                    possible_edges((y-1,x), checked, edges, river,topography)
                ##down left
                if x > 0 and y < (len(topography)-1):
                    possible_edges((y+1,x-1), checked, edges, river,topography)
                ##right
                if x < (len(topography[y])-1):
                    possible_edges((y,x+1), checked, edges, river,topography)
                ##left
                if x > 0:
                    possible_edges((y,x-1), checked, edges, river,topography)
                ##down
                if  y < (len(topography)-1):
                    possible_edges((y+1,x), checked, edges, river,topography)
                ##down right
                if y <( len(topography)-1) and x < (len(topography[y])-1):
                    possible_edges((y+1,x+1), checked, edges, river,topography)

            if len(river)>=1:
                rivers.append(river)
            
    largest_river = []
    for river in rivers:
        if len(largest_river)< len(river):
            largest_river=river
    return len(largest_river)

def test_func(func):
  print("testing", func.__name__)
  failed = False
  for test in TESTS:
    res = func(test[0])
    if res!=test[1]:
      failed = True          
      for i in range(len(test[0])):
          print(test[0][i])
      print("answer", test[1])
      print("result", res)            
      print()

  if not failed:
    print("all tests passed")


if __name__=='__main__':
  test_func(find_longest_river)
  test_func(count_rivers)