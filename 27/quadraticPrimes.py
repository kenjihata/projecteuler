import sys

# finds the nth prime using prime sieve
def findPrimesUnder(n):
	if n<=1: return [] 
	# keeps track of potential prime candidates
	primelist = [True]*n
	primelist[0] = False
	primelist[1] = False
	for ind,val in enumerate(primelist):
		if val is True:
			primelist[ind*2::ind] = [False] *(((n-1)//ind)-1)
	return [i for i, num in enumerate(primelist) if num]

# given a number, determines if it is prime
def isPrime(n):
	if n <= 1: return False
	divisor = 2
	upper_bound = n
	while divisor <= upper_bound:
		if n % divisor == 0: return False
		divisor += 1
		upper_bound = n/divisor
	return True

# given a and b, finds the number of primes, k, where n^2 + an + b
# is prime given n = all integers from 0 to k. If n=0 does not
# produce a prime, then this method will return -1 
def findPrimeLimit(a,b):
	k = 0
	while (isPrime(k*k + a*k + b)): k += 1
	return k-1

# given an absolute bound k, finds the product of coefficients a and b
# where |a| < k and |b| < k, such that n^2 + an + b returns
def findCoefficientProduct(upper_bound):
	largest_prime_limit = -1
	largest_product = -1
	for a in xrange(-upper_bound+1, upper_bound):
		for b in findPrimesUnder(upper_bound):  # we know that b must be prime
			prime_limit = findPrimeLimit(a,b)
			if prime_limit > largest_prime_limit:
				largest_product = a * b
				largest_prime_limit = prime_limit
	return largest_product

print findCoefficientProduct(int(sys.argv[1])) 
