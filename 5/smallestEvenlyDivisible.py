def smallestEvenlyDivisible(n):
	prime_factor_list = primeFactorSieve(n)
	smallest = 1
	for i in prime_factor_list:
		smallest *= i
	return smallest

def primeFactorSieve(n):
	prime_factor_list = [2]
	for i in xrange(3,n):
		num = i
		for j in prime_factor_list:
			if num%j == 0:
				num /= j
		if num != 1:
			prime_factor_list.append(num)
	return prime_factor_list

print smallestEvenlyDivisible(20)
