import math

def findNthPrime(n):
	logn = math.log(n)
	upperBound = int(math.ceil(n*(logn + math.log(logn) - 0.9484)))
	primelist = [True]*upperBound
	primelist[0] = False
	primelist[1] = False
	numPrimes = 0
	for ind,val in enumerate(primelist):
		if val is True:
			primelist[ind*2::ind] = [False] *(((upperBound-1)//ind)-1)
			numPrimes += 1
		if numPrimes == n:
			return ind
	return None
