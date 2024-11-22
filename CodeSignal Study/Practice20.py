# https://leetcode.com/discuss/interview-question/1761341/netflix-codesignal-sum-of-two-strings


def solution(a, b):
	while len(b) < len(a):
	    b = '0' + b
    while len(a) < len(b):
        a = '0' + a
    n = len(a)
    store = ['' for i in range(n)]
    for i in range(n-1,-1,-1):
        store[i] += str(int(a[i])+int(b[i]))
		
    output = ''
    for c in store:
        output += c

    return output
    