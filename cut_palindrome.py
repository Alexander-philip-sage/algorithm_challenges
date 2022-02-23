challenge_prompt = """
input: str
    lowercase letters with 1< length <1001 

Algorithm:
1. find the longest prefix of the string that is also a palindrome.
2. if the substring is >= 2 char: remove that substring from the string and go back to step 1. 
    else:
        return the string


For s = "bbbpalap", the output should be solution(s) = "".
For s = "tomato", the output should be solution(s) = "tomato".
For s = "", the output should be solution(s) = "".

return: str
    can be empty string, can be original string, can be substring of original"""
def palindrome(s: str) -> str:
    ret = [' ' for x in range(len(s))]
    for i in range(len(s)):
        ret[i] = s[len(s)-i-1]
    if "".join(ret)==s:
        return True
    else:
        return False

def cut_palindromes(s: str) -> str:
    ret = s
    cut = ""
    for i in range(1,len(s)+1):
        bl = palindrome(s[:i])
        if bl:
            if (len(s[:i]) > len(cut)) and (len(s[:i]) > 1):
                cut = s[:i]
    if len(cut) > 0:
        ret = ret.replace(cut, "")
    if len(ret) < len(s):
        return cut_palindromes(ret)
    else:
        return ret

def solution(s):
    return cut_palindromes(s)

#print(solution("aaacodex"))
#print(solution("aaacodocx"))
#print(solution("codocx"))
#print(solution("x"))
#print(solution("xxxxxx"))
print(solution("codedoc"))