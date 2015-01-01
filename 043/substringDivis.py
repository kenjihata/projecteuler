# brute force
from __future__ import division
import itertools

divis = [2,3,5,7,11,13,17]
def checkDivisibility(str_num):
	for i in xrange(1, 8):
		if (int(str_num[i:i+3])/divis[i-1]) % 1 != 0: return False
	return True

sum_num = 0
for i in itertools.permutations(['0','1','2','3','4','5','6','7','8','9']):
	str_num = ''.join(list(i))
	if checkDivisibility(str_num): sum_num += int(str_num)
print sum_num


# TODO: non-brute force
# 4th digit must be even
# 6th digit must be 5 (cannot be 0, or it violates the divisiblity by 11)
# 500's numbers divisble by 11: 506, 517, 528, 539, 550 (not pandigital), 561, 572, 583, 594
