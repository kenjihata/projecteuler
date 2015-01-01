# returns primes from 0 to n
def getPrimes(n):
	if n<=1: return [] 
	# keeps track of potential prime candidates
	primelist = [True]*n
	primelist[0] = False
	primelist[1] = False
	for ind,val in enumerate(primelist):
		if val is True:
			primelist[ind*2::ind] = [False] *(((n-1)//ind)-1)
	return ([i for i, num in enumerate(primelist) if num])

def isPandigital(n):
	n_str = str(n)
	for i in xrange(1, len(n_str)+1):
		if str(i) not in n_str:
			return False
	return True

# pandigital numbers with 8 or 9 digits are divisible by 3
primelist = getPrimes(9999999)
for i in reversed(primelist):
	if isPandigital(i):
		print i
		break