import sys
import math

# find the product of a pythagorean triplet (a,b,c, where a^2+b^2 = c^2) whose sum a+b+c = desiredSum
def findTripletProduct(desiredSum):
	for a in xrange(2, desiredSum/3+1):
		for b in xrange(2, desiredSum/2):
			c = math.sqrt(a*a + b*b)
			if (a+b+c == desiredSum):
				return a*b*c
	return None

print findTripletProduct(int(sys.argv[1]))
