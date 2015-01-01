# given n, such that n >= 1, gives the digit of the champernowne 
def findChampernowneDigit(n):
	digitsPassed = 0
	currNum = 1
	numDigits = 1
	currPower = 1
	while digitsPassed < n:
		digitsPassed += numDigits
		currNum += 1
		if currNum == 10**currPower:
			currPower += 1
			numDigits += 1
	diff = digitsPassed - n
	currNum -= 1
	return int(str(currNum)[-1-diff])

product = 1
for i in xrange(1,7):
	product *= findChampernowneDigit(10**i)
print product
