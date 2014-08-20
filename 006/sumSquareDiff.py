def sumSquareDiff(n):
	sum = 0
	sumOfSq = 0;
	for i in xrange(1,n+1):
		sum = sum + i
		sumOfSq = sumOfSq + i*i
	return sum*sum - sumOfSq

