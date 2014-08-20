import sys

# given an upperBound, returns a list, where index 0 is the sum of 
# factors of 1, index 1 is the sum of factors of 2, ... index n-1 
# is the sum of the factors of n
def factorSumList(upper_bound):
	if upper_bound < 1: return None
	factor_sum_list = [1] * upper_bound
	for i in xrange (2, upper_bound+1):
		for j in xrange(2*i-1, upper_bound, i):
			factor_sum_list[j] += i
	return factor_sum_list

# finds the list of numbers that are not the sum of two non-
# abundant numbers beneath an upper bound
def nonAbundantList(upper_bound):
	factor_sum_list = factorSumList(upper_bound)
	abundant_list = []
	abundant_sum_list = []
	for i in xrange(0, upper_bound):
		if factor_sum_list[i] > i+1:
			abundant_list.append(i+1)
	for i in xrange(0, len(abundant_list)):
		for j in xrange(i, len(abundant_list)):
			abundant_sum_list.append(abundant_list[i] + abundant_list[j])
	return list(set(xrange(1,upper_bound+1)) - set(abundant_sum_list))
	
print sum(nonAbundantList(int(sys.argv[1])))
