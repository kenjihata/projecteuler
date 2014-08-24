import sys

# finds all primes under a bound using prime sieve
def findPrimesUnder(n):
	if n<=1: return [] 
	# keeps track of potential prime candidates
	primelist = [True]*n
	primelist[0] = False
	primelist[1] = False
	for ind,val in enumerate(primelist):
		if val is True:
			primelist[ind*2::ind] = [False] *(((n-1)//ind)-1)
	return primelist
	
# given a number, returns a list of the circular values
def circular(num):
	clist  = []
	ten_power = len(str(num))-1
	for i in xrange(0, ten_power+1):
		first_digit = num//(10**ten_power)
		num = (num - first_digit * (10**ten_power)) * 10 + first_digit
		clist.append(num)
	return clist

# given a number and a prime-sieved array, determines if a number
# is a circular prime. 
def isCircularPrime(num, sieve):
	ans = True
	for p in circular(num):
		if not sieve[p]: ans = False
	return ans

# given a upper bound, find the number of circular primes 
# beneath that value
def numCircularPrimes(upper_bound):
	num_cp = 0
	prime_sieve = findPrimesUnder(upper_bound)
	prime_list = [i for i, num in enumerate(prime_sieve) if num]
	# check only primes to see if they are circular
	for i in prime_list:
		if isCircularPrime(i, prime_sieve): 
			num_cp += 1
	return num_cp

print numCircularPrimes(int(sys.argv[1]))
