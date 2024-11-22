# You are given a string s. Consider the following algorithm applied to this string:

# Take all the prefixes of the string, and choose the longest palindrome between them.
# If this chosen prefix contains at least two characters, cut this prefix from s and go back to 
# the first step with the updated string. Otherwise, end the algorithm with the current string s 
# as a result.
# Your task is to implement the above algorithm and return its result when applied to string s.

# Note: you can click on the prefixes and palindrome words to see the definition of the 
# terms if you're not familiar with them.

# Example

# For s = "aaacodedoc", the output should be solution(s) = "".

# The initial string s = "aaacodedoc" contains only three prefixes which are also palindromes - "a", "aa", "aaa". The longest one between them is "aaa", so we cut it from s.
# Now we have string "codedoc". It contains two prefixes which are also palindromes - "c" and "codedoc". The longest one between them is "codedoc", so we cut it from the current string and obtain the empty string.
# Finally the algorithm ends on the empty string, so the answer is "".


def solution(s):
    
    def checkPalindrome(s):
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
    def cutPrefix(s):
        longestPrefix = ""
        for i in range(len(s)-1,-1,-1):
            if checkPalindrome(s[:i+1]):
                longestPrefix = s[:i+1]
                if len(longestPrefix) > 1:
                    return s[i+1:]
                else:
                    return s
    
    curOut = s
    while cutPrefix(curOut) != curOut:
        if not curOut:
            break
        curOut = cutPrefix(curOut)
    
    return curOut if curOut else ""

# Better Solution in my opinion
def solution(s):
    def isPalindrome(prefix):
        l, r = 0, len(prefix)-1
        while l < r:
            if prefix[l] != prefix[r]:
                return False
            l += 1
            r -= 1
        return True
        
    l, r = 0, len(s)-1
    while l < r:
        if isPalindrome(s[l:r+1]):
            if r+1 - l > 1:
                l = r+1
                r = len(s)-1
            else:
                break
        else:
            r -= 1
            
    return s[l:]

