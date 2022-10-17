'''Imagine an island that is in the shape of a bar graph. When it rains, certain areas of the island fill up with rainwater to form lakes. Any excess rainwater the island cannot hold in lakes will run off the island to the west or east and drain into the ocean.

Given an array of positive integers representing 2-D bar heights, design an algorithm (or write a function) that can compute the total volume (capacity) of water that could be held in all lakes on such an island given an array of the heights of the bars. Assume an elevation map where the width of each bar is 1.

Example: Given [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2], return 15 (3 bodies of water with volumes of 1,7,7 yields total volume of 15)'''

class Lake():
    def __init__(self,height, index):
        self.height = height
        self.index = index

def calculate_lakes(topography):
    lakes = []
    possible_lakes = []
    for i, height in enumerate(topography):
        if not possible_lakes:
            if height>0:
                possible_lakes = [(height,i)]
        else:
            ##if the slop keeps going up or stays flat
            if len(possible_lakes)==1 and height >= possible_lakes[0][0]:
                possible_lakes = [(height,i)]
            ##if the slope goes down from the last bar
            elif height < possible_lakes[-1][0]:
                possible_lakes.append((height,i))
            ##if the slope has gone down and goes back up, then a lake is made and it could be done
            elif len(possible_lakes)>=2 and height >= possible_lakes[-1][0]:
                possible_lakes.append((height,i))
                if i+1<len(topography):
                    next_max = max(topography[i+1:])
                ##if it goes back up equal to or greater than the start of the lake, then the lake is done
                if height >= possible_lakes[0][0]:
                    lakes.append(possible_lakes)
                    possible_lakes = [(height,i)]
                ##if we're at the end 
                elif len(topography)==(i+1):
                    lakes.append(possible_lakes)
                    possible_lakes = [(height,i)]    
                ##if we're not at the end and another value exists that is greater than this end, then the lake isn't done, we'll keep looking              
                elif next_max > height:
                    pass
                ##if there is not a next max, then the lake is done
                elif next_max < height:
                    lakes.append(possible_lakes)
                    possible_lakes = [(height,i)] 

    volume = 0
    for lake in lakes:
        print(lake)
        max_height = lake[0][0] if lake[0][0]<lake[-1][0] else lake[-1][0] 
        if max_height>0:
            for bar in lake:
                if bar[0] <max_height:
                    volume+= max_height-bar[0] 
    return volume


test_cases = [([1,3,2,4,1,3,1,4,5,2,2,1,4,2,2],15), ([2,10,4,2,1],0), ([-1,-3,-1], 0),
                ([1,2,1,2],1),
                ([1,2,1,3],1),
                ([1,2,1,2,1],1),
                ([1,3],0),
                ([1,3,1,2],1),
                ([1,3,2,1,2],1),
                ([1,2,2,2,1,2],1),
                ([1,3,1,2,1,1],1),
                ([1,3,1,2,1,3],5),
                ([1,5,4,1,4,2,1,2],4),]



for test in test_cases:
    print()
    print(test[0])
    resp = calculate_lakes(test[0])
    if test[1]==resp:
        print("correct")
    else:
        print("----------")
        print('wrong')
        print("ans",test[1])
        print("mine",resp)
        print("----------")
