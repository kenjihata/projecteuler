def sumEvenFibonacci(n):
	currFib1 = 1
	currFib2 = 1
	sumFib = 0
	while currFib2 < n:
		if currFib2%2 == 0:
			sumFib += currFib2
		currFib2 += currFib1
		currFib1 = currFib2-currFib1
	return sumFib
