# Given an array of integers a, your task is to find how many of its contiguous subarrays 
# of length m contain a pair of integers with a sum equal to k.

# More formally, given the array a, your task is to count the number of indices 0 ≤ i ≤ a.length - m 
# such that a subarray [a[i], a[i + 1], ..., a[i + m - 1]] contains at least 
# one pair (a[s], a[t]), where:

# s ≠ t
# a[s] + a[t] = k
# Example

# For a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7], m = 4, and k = 10, the output should be solution(a, m, k) = 5.

# Let's consider all subarrays of length m = 4 and see which fit the description conditions:

# Subarray a[0..3] = [2, 4, 7, 5] doesn't contain any pair of integers with a sum of k = 10. Note that although the pair (a[3], a[3]) has the sum 5 + 5 = 10, it doesn't fit the requirement s ≠ t.
# Subarray a[1..4] = [4, 7, 5, 3] contains the pair (a[2], a[4]), where a[2] + a[4] = 7 + 3 = 10.
# Subarray a[2..5] = [7, 5, 3, 5] contains two pairs (a[2], a[4]) and (a[3], a[5]), both with a sum of k = 10.
# Subarray a[3..6] = [5, 3, 5, 8] contains the pair (a[3], a[5]), where a[3] + a[5] = 5 + 5 = 10.
# Subarray a[4..7] = [3, 5, 8, 5] contains the pair (a[5], a[7]), where a[5] + a[7] = 5 + 5 = 10.
# Subarray a[5..8] = [5, 8, 5, 1] contains the pair (a[5], a[7]), where a[5] + a[7] = 5 + 5 = 10.
# Subarray a[6..9] = [8, 5, 1, 7] doesn't contain any pair with a sum of k = 10.
# So the answer is 5, because there are 5 contiguous subarrays that contain a pair with a sum of k = 10.

# For a = [15, 8, 8, 2, 6, 4, 1, 7], m = 2, and k = 8, the output should be solution(a, m, k) = 2.

# There are 2 subarrays satisfying the description conditions:

# a[3..4] = [2, 6], where 2 + 6 = 8
# a[6..7] = [1, 7], where 1 + 7 = 8
# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] array.integer a

# The given array of integers.

# Guaranteed constraints:
# 2 ≤ a.length ≤ 105,
# 0 ≤ a[i] ≤ 109.

# [input] integer m

# An integer representing the length of the contiguous subarrays being considered.

# Guaranteed constraints:
# 2 ≤ m ≤ a.length.

# [input] integer k

# An non-negative integer value representing the sum of the pairs we're trying to find within each subarray.

# Guaranteed constraints:
# 0 ≤ k ≤ 109.

# [output] integer

# An integer representing the number of subarrays that contain a pair of integers with a sum of k.





def solution(a, m, k):
    seen = {}
    output = 0

    # Index of the first element of the last pair we encountered that adds up to
    # k
    first_element_index = -1

    for i, num in enumerate(a):
        diff = k - num
        # Check if there is addend in the current subarray.
        if diff in seen and i - seen[diff] < m:
            first_element_index = max(first_element_index, seen[diff])
        # If we have m elements in the subarray the last pair that adds up to k
        # is within the bounds the subarray, increment the counter.
        if i >= m-1 and i - first_element_index < m:
            output += 1
        seen[num] = i

    return output
    