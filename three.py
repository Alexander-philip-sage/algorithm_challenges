def solution(arr):
    longest = 0
    for wrd in arr:
        if len(wrd) > longest:
            longest = len(wrd)
    ret = ''
    for i in range(longest):
        for wrd in arr:
            if len(wrd) >i:
                ret += wrd[i]
    return ret

def tests():
    arr = ["Daisy", "Rose", "Hyacinth", "Poppy"]
    print(arr)
    assert solution(arr) == "DRHPaoyoisapsecpyiynth"
    print("test passed")
    arr = ['this', 'hat', 'a']
    print(arr)
    assert solution(arr) == "thahaits"
    print("test passed")

    arr = ['c', 't', 'a']
    print(arr)
    assert solution(arr) == "cta"
    print("test passed")

    arr = ['fox', 'dog', 'cat']
    print(arr)
    assert solution(arr) == "fdcooaxgt"
    print("test passed")

    arr = ['fox', 'dog', 'labrador']
    print(arr)
    assert solution(arr) == "fdlooaxgbrador"    
    print("test passed")

tests()