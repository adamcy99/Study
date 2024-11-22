# https://leetcode.com/discuss/interview-question/1610189/Codesignal-Optimization-OA/1169819

def solution(s):
	s1,s2 = s.split("+")
	def solve(s1,s2,i,j):
		paren = int(s1[i:]) + int(s2[:j+1])
		front = 1 if i == 0 else int(s1[:i])
		back = 1 if j == len(s2)-1 else int(s2[j+1:])
		return front*paren*back

	output = int(s1) + int(s2)
	i = 0
	j = len(s2)-1
	output = solve(s1,s2,i,j)
	while i < len(s1) and j >= 0:
		nexti = i+1
		outi = float('inf')
		if nexti < len(s1):
			outi = solve(s1,s2,nexti,j)

		nextj = j-1
		outj = float('inf')
		if nextj >= 0:
			outj = solve(s1,s2,i,nextj)

		if outi < outj:
			output = min(output, outi)
			i += 1
		else:
			output = min(output,outj)
			j -= 1
	i = len(s1)-1
	j = 0
	output0 = solve(s1,s2,i,j)
	while i >= 0 and j  < len(s2):
		nexti = i-1
		outi = float('inf')
		if nexti >= 0:
			outi = solve(s1,s2,nexti,j)

		nextj = j+1
		outj = float('inf')
		if nextj < len(s2):
			outj = solve(s1,s2,i,nextj)

		if outi <= outj:
			output0 = min(output, outi)
			i -= 1
		else:
			output0 = min(output,outj)
			j+= 1


	return min(output,output0)