# You are given two strings - pattern and source. The first string pattern contains only 
# the symbols 0 and 1, and the second string source contains only lowercase English letters.

# Let's say that pattern matches a substring source[l..r] of source if the following three 
# conditions are met:

# they have equal length,
# for each 0 in pattern the corresponding letter in the substring is a vowel,
# for each 1 in pattern the corresponding letter is a consonant.
# Your task is to calculate the number of substrings of source that match pattern.

# Note: In this task we define the vowels as 'a', 'e', 'i', 'o', 'u', and 'y'. All other letters are consonants.

# Example

# For pattern = "010" and source = "amazing", the output should be solution(pattern, source) = 2.

def solution(pattern, source):
    vowels = set(['a','e','i','o','u','y'])
    l = 0
    r = len(pattern)-1
    output = 0
    while r < len(source):
        count = 0
        for i in range(l,r+1):
            if source[i] in vowels and pattern[i-l] == '1':
                break
            if source[i] not in vowels and pattern[i-l] == '0':
                break
            count += 1
        if count == len(pattern):
            output += 1
        l += 1
        r += 1
    
    return output