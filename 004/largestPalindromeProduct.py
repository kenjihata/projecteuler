def largestPalindromeProduct():
	maxNumber = 0
	for i in xrange(999,100,-1):
		for j in xrange(999, 100,-1):
			if isPalindrome(i*j) and i*j > maxNumber:
				maxNumber = i*j
	return maxNumber

def isPalindrome(n):
	copy = n
	reverse = 0
	while (n > 0):
		LSD = n%10
		reverse = reverse*10 + LSD
		n = (n-LSD)/10
	return copy == reverse
