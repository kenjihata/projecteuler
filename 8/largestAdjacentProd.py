import sys

# finds the product of the digits of a string of numbers
def adjacentProduct(string):
	prod = 1
	for i in xrange(0,len(string)):
		prod *= int(string[i])
	return prod

inpStr = sys.argv[1]
adjLen = int(sys.argv[2])

maxProd = 0
for i in xrange(0, len(inpStr) - adjLen):
	prod = adjacentProduct(inpStr[i:i+adjLen])
	if prod > maxProd:
		maxProd = prod
print maxProd
