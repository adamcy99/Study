# Given an array of unique integers numbers, 
# your task is to find the number of pairs of indices (i, j) 
# such that i ≤ j and the sum numbers[i] + numbers[j] is equal 
# to some power of 2.

# Note: The numbers 20  = 1, 21 = 2, 22 = 4, 23 = 8, etc. 
# are considered to be powers of 2.

def solution(numbers):
	import collections
	seen = collections.defaultdict(int)
	output = 0
	for i in numbers:
		for n in range(21):
			complement = 2**n - i
			output += seen[complement]
		seen[i] += 1
	return output