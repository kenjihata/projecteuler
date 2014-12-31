from __future__ import division
from sets import Set

# this program finds the sum of all truncatable primes

# truncatable primes can only be created of these digits
prime_dig = [2, 3, 5, 7] 
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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
	return ([i for i, num in enumerate(primelist) if num], primelist)
	
# given a number and a prime sieve, determines if a number is a truncatable prime
def isTruncatablePrime(n, ps):
	if n < 10: return False
	n_str = str(n)
	for i in xrange(0,len(n_str)):
		if not ps[n//(10**i)] or not ps[n%(10**(i+1))]:
			return False
	return True
	
tp_list = []
num = 10;
while len(tp_list) < 11:
	p, ps = getPrimes(num)
	for i in p:
		if i not in tp_list and isTruncatablePrime(i,ps): tp_list.append(i)
	num *= 2
print tp_list
print sum(tp_list)
	
