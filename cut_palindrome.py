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