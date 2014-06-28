import sys
import math

# given an integer argument n, return the sum of the digits of n!
def factorialDigitSum(n):
	strFactorial = str(int(math.factorial(n)))
	sum = 0
	for i in strFactorial:
		sum += int(i)
	return sum
	
print factorialDigitSum(int(sys.argv[1]))

