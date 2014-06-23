import sys

def collatzLength(num, arr):
	if num < 1:
		return None
	length = 0
	while num != 1:
		if num % 2 == 1:
			num = 3*num + 1
		else:
			num /= 2
		if num >= 1 and num <= len(arr):
			arr[num-1] = False
		length += 1
	return length

def longestCollatzSequence(upperBound):
	if upperBound < 1:
		return None
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
