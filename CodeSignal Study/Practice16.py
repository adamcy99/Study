# https://leetcode.com/discuss/interview-question/2051872/codesignal-question-practice
# Define a string reflection as the result of applying the 
# alphabet to each of its characters.
# Reflect the given string

def solution(inputString):
	output = ''
	for i in inputString:
		reflect = (ord('z') - ord(i)) + ord('a')
		output += chr(reflect)
	return output