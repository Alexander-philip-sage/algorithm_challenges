h1. Sub Array with Sorted Objects

h2. Problem Statement
 
* you get a lot of objects with locations on (x,y). Each with a rank.
* you get a rectangle/border. 
* copy the M smallest points within the border into an Array

h2. Approaches

* wrote a slow version for comparing against that sorts all points, then filters based on if they are in the border
* wrote a slow version that filters all the points into a vector. Then sorts all points in the border. I wrote this version because it was easiest to do with STL.
* wrote the final faster version, and didn't find a binary search tree in the STL, maybe its there, I'm not proficient with C++. Every point that 

h2. If I had more time

* I'd figure out why my code passes my tests but not Shotover's tests.
* I'd modify the BST more, s.t. it saves and checks the max value. if a new value in the border is > than the max value and we already have M points, then don't even do the log(W) insert into the BST. This would cut down some time and memory.
* I'd play with the const Rect rect param in the search function. I think its supposed to be a pointer, but it says its a value.

h1. Prompt from Shotover

Welcome to the Churchill Navigation Programming Exercise

We appreciate your interest in working on our team!  We want you to know that your Programming Exercise submission will never be used for any purpose other than as a way for us to have some idea of your coding skills.

Here are the files to get you started:
point_search.h   : Header file containing the precise problem definition and describing the DLL's interface.
point_search.exe : The testing framework that can load one or more DLLs, evaluate their performance and compare their results.
reference.dll    : Reference solution that is used to test other solutions for correctness.


