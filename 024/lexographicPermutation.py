import sys

# program works by giving two arguments:
# 1) the permutation index, where 1 is the identity of the original
# permutation
# 2) the permutation itself

# given a number (as a list of characters), return the next 
# lexographic permutation. If at the final permutation, return none
def nextLexographicPermutation(listNum):
	for i in xrange(len(listNum)-2, -1, -1):
		if listNum[i] < listNum[i+1]:
			for j in xrange(len(listNum)-1, i, -1):
				if listNum[i] < listNum[j]:
					temp = listNum[i]
					listNum[i] = listNum[j]
					listNum[j] = temp
					listNum[i+1:] = reversed(listNum[i+1:])
					return listNum
	return None

lexographicIndex = int(sys.argv[1])
listNum = list(sys.argv[2])
for i in xrange(1, lexographicIndex):
	listNum = nextLexographicPermutation(listNum)
print ''.join(listNum)
