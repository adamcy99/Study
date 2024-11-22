# Question can be found here: https://leetcode.com/discuss/interview-question/1510714/how-to-approach-this-problem-codesignal-practise

def solution(matrix, queries):
	white = []
	black = []

	for j in range(len(matrix)):
		for i in range(len(matrix[0])):
			# rows 0, 2, 4, etc start with white
			if j%2 == 0:
				# col 0, 2, 4 are white
				if i%2 == 0:
					white.append([matrix[j][i],j,i])
				else:
					black.append([matrix[j][i],j,i])
			else:
				if i%2 == 0:
					black.append([matrix[j][i],j,i])
				else:
					white.append([matrix[j][i],j,i])

	for i,j in queries:
		white.sort(key = lambda x: (x[0], x[1], x[2]))
		black.sort(key = lambda x: (x[0], x[1], x[2]))

		b = black[i]
		w = white[j]
		m = (b[0] + w[0])//2

		bj, bi = b[1], b[2]
		wj, wi = w[1], w[2]
		if (b[0] + w[0])%2 == 0:
			matrix[bj][bi] = m
			matrix[wj][wi] = m
		else:
			temp = [b,w]
			temp.sort(key = lambda x: (x[0], x[1], x[2]))
			smallerj, smalleri = temp[0][1], temp[0][2]
			largerj, largeri = temp[1][1], temp[1][2]
			matrix[smallerj][smalleri] = m
			matrix[largerj][wlargerii] = m + 1
				