import itertools
from sets import Set

# given a list of numbers, returns the number which concatenates the digits
# example: [1,2,3] returns 123
def convertToInt(l):
	ret_val = 0
	for i in xrange(len(l)-1, -1, -1):
		ret_val += l[i] * 10**(len(l)-i-1)
	return ret_val


pan_prod = []
all_num = [1,2,3,4,5,6,7,8,9]
for p  in (itertools.permutations(all_num)):
	# we know that only a 1-digit number * 4 digit number
	# or 2-digit number * 3-digit number can give us the 
	if p[0] * convertToInt(p[1:5]) == convertToInt(p[5:]) or convertToInt(p[0:2]) * convertToInt(p[2:5]) == convertToInt(p[5:]):
		pan_prod.append(convertToInt(p[5:]))
unique = Set(pan_prod)
print sum(unique)

