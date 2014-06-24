import sys

# sums the digits of base ^ exponent (e.g. sum of digits of 2^4 is 7)
def powerDigitSum(base, exponent):
	num = base ** exponent
	num = str(num)
	digitSum = 0
	for i in num:
		digitSum += int(i)
	return digitSum

print(powerDigitSum(int(sys.argv[1]), int(sys.argv[2])))
