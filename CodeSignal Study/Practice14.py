# Question in: https://codesignal.com/blog/interview-prep/example-codesignal-questions/


def solution(field,figure):
	field_w = len(field[0])
	field_h = len(field)
	fig_size = len(figure)

	for col in range(field_w - fig_size + 1):
		# row is the top of fig
		# row set to 1 to peak at the next row to see if figure will fit
		row = 1
		# keep going down until figure reaches the bottom to see if it'll fit
		while row < field_h - fig_size + 1:
			can_fit = True
			# cross checking all values in figure w/ the fig_sizexfig_size box on the field we are in
			for dy in range(fig_size):
				for dx in range(fig_size):
					if field[row+dy][col+dx] == 1 and figure[dy][dx] == 1:
						can_fit = False
			# next line doesn't fit, we break and go back to prev line
			if not can_fit:
				break
			# peak into next line
			row += 1
		# when we break or reach the end, it's always keeping the next row.
		# so we must go back to previous row.
		row -= 1

		# now we know which is the lowest row, we check if any row is filled
		# only need to check fig_size number of rows
		for dy in range(fig_size):
			row_filled = True
			# check along the entire row
			for i in range(field_w):
				# row+dy is the current row we're checking. if any val is 0, return false
				# col <= i < col + fig_size means we are currently in the figure box
				# next bit is to check inside the figure box to see if we have a 1
				# basically checking inside field to see if it's 0, if it is, look at the val
				# inside the figure box to see if that value is 1, if not, we don't have a filled row
				if not (field[row+dy][i] != 1 or (col <= i < col + fig_size and figure[dy][i-col] == 1)):
					row_filled == False
			if row_filled:
				return col
	return -1