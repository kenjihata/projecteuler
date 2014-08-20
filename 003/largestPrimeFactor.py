def largestPrimeFactor(n):
	i = 2
	largestPrime = 1
	while i<=n:
		while n%i == 0:
			n/=i
			largestPrime = i
		i+=1
	return largestPrime
