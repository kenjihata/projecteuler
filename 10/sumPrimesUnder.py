import sys

def generatePrimesUnder(upperBound):
	primelist = []
	isPrime = [True]*upperBound
	isPrime[0] = False
	isPrime[1] = False
	for ind,val in enumerate(isPrime):
		if val is True:
			isPrime[ind*2::ind] = [False] *(((upperBound-1)//ind)-1)
	return [i for i in range(len(isPrime)) if isPrime[i]]

primelist = generatePrimesUnder(int(sys.argv[1]))
print sum(primelist)
