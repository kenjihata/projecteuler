from __future__ import division
# Two eqn's: a^2 + b^2 = c^2 ; a + b + c = p
# c = p - a - b =====> a^2 + b^2 = c^2 
# a^2 + b^2 = p^2 -2ap - 2bp +2ab + a^2 + b^2
# p^2 - 2ap -2bp + 2ab = 0
# b(2a-2p) = 2ap-p^2
# b = (2ap - p^2)/(2a-2p)
def findNumTriplets(p):
	count = 0
	for a in xrange(1, p//2): 
		b = (2*a*p - p*p) / (2*a - 2*p)
		if b%1 == 0:
			count += 1
	return count/2 # method double counts

max_num_triplets = 0
max_p = 0
for i in xrange(1, 1000):
	num_triplets = findNumTriplets(i)
	if num_triplets > max_num_triplets:
		max_num_triplets = num_triplets
		max_p = i
print max_p