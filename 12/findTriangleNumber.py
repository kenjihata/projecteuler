import sys

def numberOfFactors(num):
	if num < 1: return None
	if num == 1: return 1
	numFactors = 2
	for i in xrange(2,num/2):
		if num % i == 0: numFactors += 1
	return numFactors

def findSmallestTriangleNum(desiredFactorCount):
	if desiredFactorCount < 1: return None
	triangleNum = 1
	index = 1
	factorCount = 1
	while (desiredFactorCount > factorCount):
		index += 1
		triangleNum += index
		factorCount = numberOfFactors(triangleNum)
	return triangleNum

print findSmallestTriangleNum(sys.argv[1])
