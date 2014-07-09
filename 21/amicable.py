import sys

def amicableSumUnder(upperBound):
	if upperBound < 1: return None
	
	# keeps track of all the sums from 1 to upperBound
	factorSum = [0] * upperBound
	for i in xrange (1, upperBound+1):
		for j in xrange(2*i-1, upperBound, i):
			factorSum[j] += i
	sumUnder = 0
	for i in xrange(0, upperBound):
		j = factorSum[i]
		if j <= upperBound and j > 0:
			if factorSum[j-1] == i+1 and factorSum[i] == j and i+1!=j:
				sumUnder += i+1+j
				
	# each pair is counted twice
	return sumUnder/2
	
print amicableSumUnder(int(sys.argv[1]))
		
