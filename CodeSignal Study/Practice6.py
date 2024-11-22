# You are given two arrays of integers a and b of the same length, and an integer k. 
# We will be iterating through array a from left to right, and simultaneously through 
# array b from right to left, and looking at pairs (x, y), where x is from a and y is from b. 
# Such a pair is called tiny if the concatenation xy is strictly less than k.

# Your task is to return the number of tiny pairs that you'll encounter during the simultaneous 
# iteration through a and b.

# Example

# For a = [1, 2, 3], b = [1, 2, 3], and k = 31, the output should be
# solution(a, b, k) = 2.

# We're considering the following pairs during iteration:

# (1, 3). Their concatenation equals 13, which is less than 31, so the pair is tiny;
# (2, 2). Their concatenation equals 22, which is less than 31, so the pair is tiny;
# (3, 1). Their concatenation equals 31, which is not less than 31, so the pair is not tiny.
# As you can see, there are 2 tiny pairs during the iteration, so the answer is 2.

def solution(a, b, k):
    p1 = 0
    p2 = len(b)-1
    output = 0
    while p1 < len(a):
        pair = int(str(a[p1]) + str(b[p2]))
        if pair < k:
            output += 1
        p1 += 1
        p2 -= 1

    return output