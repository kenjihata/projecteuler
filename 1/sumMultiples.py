def sumMultiples(n):
	sum = 0
	for x in xrange(1,n):
		if x%3 == 0 or x%5 == 0:
			sum += x 
	return sum
		

