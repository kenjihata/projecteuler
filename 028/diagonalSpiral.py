import sys

# given an odd whole number side length, returns the sum of the diagonals 
# of a clockwise spiral (starting from the center and going outward to the right)
def sumSpiralDiagonals(side_length):
	if side_length % 2 == 0 or side_length < 1: return None
	curr_length = 1
	curr_sum = 1
	curr_num = 1
	while(curr_length < side_length):
		for i in xrange(0,4): # each corner is separated by the same "distance"
			curr_num += curr_length+1
			curr_sum += curr_num
		curr_length += 2
	return curr_sum

print sumSpiralDiagonals(int(sys.argv[1]))
	
