import sys

# given a number, returns the length of the repeating cycle of its reciprocal
# for example, given 3, returns 1 since 1/3 = 0.3333333...
# if there is no repeating cycle, returns 0.
def reciprocalCycleLen(num):
	remainder = 1;
	remainderSet = []
	while (remainder % num != 0):
		for i in xrange(0, len(remainderSet)):
			if remainderSet[i] == remainder:
				return len(remainderSet) - i
		remainderSet.append(remainder)
		remainder = remainder*10 % num
	return 0

# given an upper bound, returns the number with the longest reciprocal cycle 
# of all whole numbers less than or equal to that upper bound
def findLongestReciprocalCycleUnder(num):
	longest = -1
	longestNum = -1
	if num < 1: return None
	for i in xrange(1, num+1):
		currLen = reciprocalCycleLen(i)
		if currLen > longest:
			longest = currLen
			longestNum = i
	return longestNum

print findLongestReciprocalCycleUnder(int(sys.argv[1]))
