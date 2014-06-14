import sys
import math

def findTripletProduct(desiredSum):
	for a in xrange(2, desiredSum/3+1):
		for b in xrange(2, desiredSum/2):
			c = math.sqrt(a*a + b*b)
			if (a+b+c == desiredSum):
				return a*b*c
print findTripletProduct(int(sys.argv[1]))
