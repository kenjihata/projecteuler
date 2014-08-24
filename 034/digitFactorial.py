from math import factorial

factorial_arr = [factorial(0), factorial(1), factorial(2), factorial(3), factorial(4), factorial(5), factorial(6), factorial(7), factorial(8), factorial(9)]

# given a number, determines if the sum of the factorials
# of the digits equals the number
def isFactorialDigit(num):
	if num < 0: return False
	sum_fd = 0
	for i in str(num):
		sum_fd += factorial_arr[int(i)]
	return sum_fd == num

# we know that the range of all possible numbers ranges from 
# 10 to 9!*7
ans = 0
for i in xrange(10, factorial_arr[9] * 7):
	if isFactorialDigit(i): ans += i
print ans	

