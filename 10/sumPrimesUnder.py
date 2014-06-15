import sys

def isPrime(num, primelist):
	for i in primelist:
		if i > num/2:
			return True
		if num % i == 0:
			return False
	return True

def generatePrimesUnder(upper):
	if(upper < 2):
		return []
	primelist = [2]
	for i in xrange(3, upper,2):
		if isPrime(i, primelist):
			primelist.append(i)
	return primelist

def generatePrimesUnder2(upper):
	if upper<2:
		return []
	primelist = [2]
	primelist.append(range(3, upper,2))
	numPrimes = 1
	while numPrimes < len(primelist):
		sieveNum = primelist[numPrimes]
		for i in primelist[numPrimes+1:]:
			if i % sieveNum == 0:
				primelist.remove(i)
	return primelist

primelist = generatePrimesUnder2(int(sys.argv[1]))
print sum(primelist)
