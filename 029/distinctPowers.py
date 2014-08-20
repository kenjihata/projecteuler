import sys
from sets import Set

# given integer bounds for the base and exponent, find the number
# of distinct base ^ exp.
def countDistinctPowers(base_lb, base_ub, exp_lb, exp_ub):
	powers = []
	for base in xrange(base_lb, base_ub+1):
		for exp in xrange(exp_lb, exp_ub+1):
			powers.append(pow(base,exp))
	distinct_set = Set(powers)
	return len(distinct_set)

print countDistinctPowers(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
