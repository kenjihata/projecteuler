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

curr = 3
curr_prime = 3
primelist = getPrimes(curr_prime)
while True:
	if curr >= curr_prime:
		curr_prime *= 2
		primelist = getPrimes(curr_prime)
	should_break = False
	for i in xrange(0, curr):
		for j in primelist:
			if 2*i*i+j > curr:
				break
			if 2*i*i+j == curr:
				should_break = True
				
	if not should_break:
		break
	curr+=2 
print curr