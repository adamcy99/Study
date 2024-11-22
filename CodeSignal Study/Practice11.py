# You are given an array of integers a, where each element a[i] represents the length of a ribbon.

# Your goal is to obtain k ribbons of the same length, 
# by cutting the ribbons into as many pieces as you want.

# Your task is to calculate the maximum integer length L for which it is 
# possible to obtain at least k ribbons of length L by cutting the given ones.

# Example

# For a = [5, 2, 7, 4, 9] and k = 5, the output should be solution(a, k) = 4.

def solution(a, k):
    def isValid(size):
        count = 0
        for r in a:
            count += r//size
        if count >= k:
            return True
        return False
        
    size = sum(a)//k
    l, r = 1, size
    while l+1 < r:
        mid = (r+l)//2
        if isValid(mid):
            l = mid
        else:
            r = mid-1
    if isValid(r):
        return r
    if isValid(l):
        return l