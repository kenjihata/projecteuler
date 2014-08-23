from __future__ import division

# given a numerator and denominator, determines if they digit cancel correctly
# while not being trivial
def isDigitCanceling(num, denom):
	if denom < num or denom %10 == 0 or denom//10 == 0: return False
	return num%10 == denom//10 and num/denom == (num//10) / (denom%10) and not (num/denom == (num%10) / (denom//10))

# returns the greatest common factor of two numbers
def gcf(x,y):
	if x < y:
		tmp = x
		x = y
		y = tmp
	while x % y != 0:
		remainder = x % y
		x = y
		y = remainder
	return y


nums = 1
denoms = 1
# find all digit canceling fractions
for i in xrange(10, 100):
	for j in xrange(i, 100):
		if isDigitCanceling(i,j):
			nums *= i
			denoms *= j
while gcf(nums, denoms) != 1:
	f = gcf(nums, denoms)
	nums /= f
	denoms /= f
print denoms


	
