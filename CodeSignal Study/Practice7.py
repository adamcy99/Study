# A sawtooth sequence is a sequence of numbers that alternate between increasing and decreasing. 
# In other words, each element is either strictly greater than its neighbouring elements or 
# strictly less than its neighbouring elements.

# examples

# Given an array of integers arr, your task is to count the number of contiguous subarrays 
# that represent a sawtooth sequence of at least two elements.

# Example

# For arr = [9, 8, 7, 6, 5], the output should be solution(arr) = 4.

# Since all the elements are arranged in decreasing order, it won't be possible to form any sawtooth subarrays of length 3 or more. There are 4 possible subarrays containing two elements, so the answer is 4.

# For arr = [10, 10, 10], the output should be solution(arr) = 0.

# Since all of the elements are equal, none of subarrays can be sawtooth, so the answer is 0.

# For arr = [1, 2, 1, 2, 1], the output should be solution(arr) = 10.

# All contiguous subarrays containing at least two elements satisfy the condition of problem. There are 10 possible contiguous subarrays containing at least two elements, so the answer is 10.

def solution(arr):
    n = len(arr)
    output = 0
    prev_slope = 0
    streak = 0
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            pre_slope = 0
            streak = 0
        else:
            cur_slope = (arr[i] - arr[i-1])//abs(arr[i]-arr[i-1])
            if cur_slope != prev_slope:
                streak += 1
                prev_slope = cur_slope
            else:
                streak = 1
            output += streak
            
    return output

OR

def solution(arr):
    mp = {0:0, 1:1}
    for i in range(2,len(arr)):
        mp[i] = mp[i-1] + i
    
    n = len(arr)
    output = 0
    prev_slope = 0
    streak = 0
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            # Streak broken so add the number of sawtooths in the streak length
            output += mp[streak]
            prev_slope = 0
            streak = 0
        else:
            cur_slope = (arr[i] - arr[i-1])//abs(arr[i]-arr[i-1])
            if cur_slope != prev_slope:
                streak += 1
                prev_slope = cur_slope
            else:
                # Streak broken so add the number of sawtooths in the streak length
                output += mp[streak]
                streak = 1
    # Add the last streak value that wasn't broken
    output += mp[streak]
            
    return output
        