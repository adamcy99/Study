# Given an array of integers a, your task is to calculate the digits that occur 
# the most number of times in the array. Return the array of these digits in ascending order.

# Example

# For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2, 3, 5].

# Here are the number of times each digit appears in the array:

# 0 -> 0
# 1 -> 1
# 2 -> 2
# 3 -> 2
# 4 -> 1
# 5 -> 2
# 6 -> 0
# 7 -> 1
# 8 -> 1
# The most number of times any number occurs in the array is 2, and the digits which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5].

def solution(a):
    d = [0 for i in range(10)]
    
    for num in a:
        n_str = str(num)
        for i in n_str:
            key = int(i)
            d[key] += 1
    output = []
    max_d = max(d)
    for i in range(len(d)):
        if d[i] == max_d:
            output.append(i)
    return output