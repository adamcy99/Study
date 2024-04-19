"""
Input: "aabbbacd"
Output: "cd"
Explanation:
1. Remove 3 'b': "aabbbacd" => "aaacd"
2. Remove 3 'a': "aaacd" => "cd"
"""

def CandyCrush1D(s):
	if not s:
		return ""
	stack = []
	stack.append([s[0], 1])
	for i,c in enumerate(s[1:]):
		if c != s[i-1]:
			if stack[-1][1] >= 3:
				stack.pop()
			if stack and stack[-1][0] == c:
				stack[-1][1] += 1
			else:
				stack.append([c,1])
		else:
			stack[-1][1] += 1

	if stack[-1][1] >= 3:
		stack.pop()

	output = []

	for pair in stack:
		output += pair[0]*pair[1]

	return "".join(output)
