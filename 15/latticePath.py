import sys
import math

def latticePathCount(gridLength):
	if gridLength < 0: return None
	return math.factorial(gridLength*2) / (math.factorial(gridLength) ** 2)

print latticePathCount(int(sys.argv[1]))
