from typing import List 
'''Imagine an island that is in the shape of a bar graph. When it rains, certain areas of the island fill up with rainwater to form lakes. Any excess rainwater the island cannot hold in lakes will run off the island to the west or east and drain into the ocean.

Given an array of positive integers representing 2-D bar heights, design an algorithm (or write a function) that can compute the total volume (capacity) of water that could be held in all lakes on such an island given an array of the heights of the bars. Assume an elevation map where the width of each bar is 1.

Example: Given [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2], return 15 (3 bodies of water with volumes of 1,7,7 yields total volume of 15)
https://techdevguide.withgoogle.com/resources/former-interview-question-volume-of-lakes/#!'''

class Bar():
    def __init__(self,height, index):
        self.height = height
        self.index = index

def calculate_lakes(topography: List[int]) -> int:
    '''my first try, a lot more code than necessary'''
    ##list of lakes on land
    lakes = []
    ##list of bars that might make up a lake
    possible_lakes = []
    for i, height in enumerate(topography):
        if not possible_lakes:
            if height>0:
                possible_lakes = [Bar(height,i)]
        else:
            ##if the slope keeps going up or stays flat
            if len(possible_lakes)==1 and height >= possible_lakes[0].height:
                possible_lakes = [Bar(height,i)]
            ##if the slope goes down from the last bar
            elif height < possible_lakes[-1].height:
                possible_lakes.append(Bar(height,i))
            ##if the slope has gone down and goes back up, then a lake is made and it could be done
            elif len(possible_lakes)>=2 and height >= possible_lakes[-1].height:
                possible_lakes.append(Bar(height,i))
                if (i+1)<len(topography):
                    next_max = max(topography[i+1:])
                ##if we're at the end 
                elif len(topography)==(i+1):
                    lakes.append(possible_lakes)
                    possible_lakes = [Bar(height,i)]    
                ##if height is back up equal to or greater than the start of the lake, then the lake is done
                if height >= possible_lakes[0].height:
                    lakes.append(possible_lakes)
                    possible_lakes = [Bar(height,i)]
                ##if we're not at the end and another value exists that is greater than this end, then the lake isn't done, we'll keep looking              
                elif next_max > height:
                    pass
                ##if there is not a next max, then the lake is done
                elif next_max <= height:
                    lakes.append(possible_lakes)
                    possible_lakes = [Bar(height,i)] 

    volume = 0
    for lake in lakes:
        #print(lake)
        max_height = lake[0].height if lake[0].height<lake[-1].height else lake[-1].height 
        if max_height>0:
            for bar in lake:
                if bar.height <max_height:
                    volume+= max_height-bar.height 
    return volume


def trap_google(height: List[int]) -> int:
    '''copied from google sol'''
    left_index, right_index = 0, len(height) - 1
    left_max, right_max = 0, 0
    output = 0
    while left_index < right_index:
        if height[left_index] <= height[right_index]:
            left_max = max(left_max, height[left_index])
            output += max(0, left_max - height[left_index])
            left_index += 1
        else:
            right_max = max(right_max, height[right_index])
            output += max(0, right_max - height[right_index])
            right_index -= 1
    return output

def lakes3(height):
    left_index, right_index = 0, len(height) - 1
    left_max, right_max = 0, 0
    output = 0
    while left_index < right_index:
        if height[left_index]<left_max and height[left_index]<right_max:
            output+= (left_max- height[left_index]) if left_max < right_max else (right_max- height[left_index])
            left_index+=1

def lakes4(height):
  '''written from memory of how to solve it. came out a little different from the 
  google answer since its been a year, but still passes all test cases'''
  i = 0
  j = len(height)-1
  lh=0
  rh=0
  water =0
  while i<=j:
    if rh<lh:
      if height[j] <rh:
        water +=rh-height[j]
      else:
        rh = height[j]
      j-=1
    else:
      if height[i]<lh:
        water += lh-height[i]
      else:
        lh = height[i]
      i+=1
    #print("rh", rh, "lh",lh,"water", water, "i", i, "j", j)
  return water

TEST_CASES = [
                ##left cliff edge, right cliff edge, underwater hill under the lake
                ([3,1,2,1,3],5),
                ##up, down, no lakes
                ([2,10,4,2,1],0), 
                ##down up, never above ground
                ([-1,-3,-1], 0),
                ##two values
                ([1,3],0),
                ##one value
                ([1],0),
                ##downhill only
                ([4,3,2,1],0),
                ##uphill only
                ([1,2,3,4],0),
                ##given test
                ([1,3,2,4,1,3,1,4,5,2,2,1,4,2,2],15), 
                ##lake below sea level
                ([1,-1,1],2),
                ##multiple lakes below sea level
                ([1,-1,1,-2,-3,-2,1],12),
                ##left side uphill, left side lake is higher, drop off on right
                ([1,3,1,2],1),
                ##hill to left of lake
                ([1,3,2,1,2],1),
                ##mesa plateau left of lake
                ([1,2,2,2,1,2],1),
                ##slope down and platea to right of lake
                ([1,3,1,2,1,1],1),

                ([1,5,4,1,4,2,1,2],4),
                ([1,2,1,2],1),
                ##right side of lake is greater
                ([1,2,1,3],1),
                ##perfectly symetric, ramp up, then lake, ramp down
                ([1,2,1,2,1],1),
                ##steep cliff
                ([1,10,1,2],1)
                ]

def test_algorithm(alg):
    '''input: a function that takes in a list of heights'''
    failed = False
    for test in TEST_CASES:
        resp = alg(test[0])
        if test[1]!=resp:
            failed=True
            print("----------")
            print('wrong')
            print("heights", test[0])
            print("ans",test[1])
            print(alg.__name__,resp)
            print("----------")
    if not failed:
        print()
        print(alg.__name__,"all test cases passed")

test_algorithm(trap_google)
test_algorithm(calculate_lakes)
