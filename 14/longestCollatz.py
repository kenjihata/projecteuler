import sys

# finds the collatz length of a given whole number. 
# arguments are the whole number and a list, by reference, where we keep track of potential longest candidates.
def collatzLength(num, longestList):
	if num < 1:
		return None
	length = 0
	while num != 1:
		if num % 2 == 1:
			num = 3*num + 1
		else:
			num /= 2
		if num >= 1 and num <= len(arr):
			longestList[num-1] = False
		length += 1
	return length

# finds the longest collatz sequence of whole numbers up to upperBound
def longestCollatzSequence(upperBound):
	if upperBound < 1:
		return None
	# keep track of which number is potentially the longest (true if so)
	longestTracker = [True] * upperBound
	longestLength = 0
	longestNum = 1
	for i in range(upperBound, 0, -1):
		if longestTracker[i-1]:
			length = collatzLength(i, longestTracker)
			if length > longestLength:
				longestNum = i
				longestLength = length
	return longestNum

print longestCollatzSequence(int(sys.argv[1]))
