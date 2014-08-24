import sys

# converts a number to its binary equivalent
def decToBin(num):
	return int(bin(num)[2:])

# returns if a number is a palindrome
def isPalindrome(num):
	strnum = str(num)
	ans = True
	for i in xrange(0, len(strnum)/2):
		if strnum[i] != strnum[len(strnum) - i - 1]:
			ans = False
	return ans
	
sum_pali = 0
upper_bound = int(sys.argv[1])
for i in xrange(1, upper_bound):
	if isPalindrome(i) and isPalindrome(decToBin(i)):
		sum_pali += i
print sum_pali
	
