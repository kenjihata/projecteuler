def isPandigital(n):
	n_str = str(n)
	for i in xrange(1,10):
		if str(i) not in n_str:
			return False
	return True

# we know the largest pandigital multiple begins with a 9
# we know 9 is probably not hte right answer (trivial problem if so)
# we know that 90-100 won't work
# we know that 900-1000 won't work
# thus it must be between 9000 - 10000
# if it's between 9000-10000, then it only goes up to a multiple of 2
for i in xrange(9999, 9000, -1):
	num = i*100000 + i*2
	if isPandigital(num):
		print num
		break