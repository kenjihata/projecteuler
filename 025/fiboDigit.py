import sys
import math

# returns the index of the first fibonacci number with a certain number of digits
def firstFiboDigit(digitNum):
	if digitNum < 1: return None
	first = 1;
	second = 1;
	index = 1;
	while (math.log(first,10) < digitNum-1):
		second = first + second;
		first = second - first;
		index += 1
	return index

print firstFiboDigit(int(sys.argv[1]))
