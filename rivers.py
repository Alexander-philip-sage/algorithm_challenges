'''a river is a series of ones touching. input is a matrix. river size is the sum of all the touching ones. create a list of all rivers and return size of the biggest'''
tests = [
        ([[1,0,0,1],
          [1,1,0,1],
          [0,1,0,1],
          ] ,4),
        ([[1,0,0,1],
          [0,1,0,1],
          [0,1,0,0],
          ] ,3),
        ([[1,0,0,1],
          [0,1,0,1],
          [0,0,1,0],
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

        ]
def count_rivers(topography):

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
                possible_edges = []
                if y>0 and x < (len(topography[y])-1):
                    possible_edges.append((y-1,x+1))
                if x > 0 and y < (len(topography)-1):
                    possible_edges.append((y+1,x-1))
                if x < (len(topography[y])-1):
                    possible_edges.append((y,x+1))
                if  y < (len(topography)-1):
                    possible_edges.append((y+1,x))
                if y <( len(topography)-1) and x < (len(topography[y])-1):
                    possible_edges.append((y+1,x+1))
                for e in possible_edges:
                    if e not in checked:
                        checked.add(e)
                        if topography[e[0]][e[1]]==1:
                            edges.append(e)
                            river.append(e)
            if len(river)>=1:
                rivers.append(river)
            
    largest_river = []
    for river in rivers:
        if len(largest_river)< len(river):
            largest_river=river
    return len(largest_river)

if __name__=='__main__':
    for test in tests:
        res = count_rivers(test[0])
        if res!=test[1]:
            for i in range(len(test[0])):
                print(test[0][i])
            print("answer", test[1])
            print("result", res)            
            print()


