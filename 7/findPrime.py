import math

def findNthPrime(n):
	primelist = [2]
	currNum = 3
	for i in xrange(1,n):
		while True:
			isPrime = True
			for i in primelist:
				if currNum%i == 0:
					isPrime = False
			if isPrime:
				primelist.append(currNum)
				currNum += 1
				break
			currNum += 1
	return primelist[-1]

