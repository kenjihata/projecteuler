# given a positive integer, checks whether the sum of its digits' fifth power
# is equal to the number
def isDigitFifthPower(num):
	digits = [pow(int(x),5) for x in str(num)]
	return sum(digits) == num


# since we know that 9999999 > 7*(9^5), we only have to check all valid
# 7 digit numbers up to 7*(9^5) = 413343

sum_num = 0
for i in xrange(10, 413343):
	if isDigitFifthPower(i): 
		sum_num += i
print sum_num


