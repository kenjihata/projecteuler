import sys

# finds the number of factors for a given whole number
def numberOfFactors(num):
	if num < 1: return None
	if num == 1: return 1
	numFactors = 2
	for i in xrange(2,num):
		if num % i == 0: numFactors += 1
	return numFactors

# finds the smallest Triangle Number with at least a given number of factors
def findSmallestTriangleNum(desiredFactorCount):
	if desiredFactorCount < 1: return None
	triangleNum = 1
	index = 1
	factorCount = 1
	while (desiredFactorCount > factorCount):
		# we will use the fact that triangleNum(n) = n*(n+1)/2
		index += 1
		lhs = index
		rhs = index+1
		if lhs%2 == 0: lhs /= 2
		else: rhs /= 2
		triangleNum = rhs*lhs
		factorCount = numberOfFactors(lhs)*numberOfFactors(rhs)
	return triangleNum

print findSmallestTriangleNum(int(sys.argv[1]))

