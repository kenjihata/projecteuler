import sys

coin_values = [1, 2, 5, 10, 20, 50, 100, 200]

# given a goal amount, find the number of ways that you can make 
# that amount out of the coins given above
def findNumWays(goal):
	# dynamic programming - keeps track of the number of ways per amount
	# index 19 corresponds to the number of ways you can make 19
	num_ways = [0]*(goal + 1) 
	num_ways[0] = 1
	for i in xrange(0, len(coin_values)):
		for j in xrange(coin_values[i], goal+1):
			num_ways[j] += num_ways[j - coin_values[i]]
	return num_ways[-1]	

print findNumWays(int(sys.argv[1]))
