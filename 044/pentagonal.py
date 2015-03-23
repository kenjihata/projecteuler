def pentagonal():
	n = 1
	s = set()
	while True:
		num = n*(3*n-1)/2
		for i in s:
			if num-i in s and num-2*i in s:
				return num-2*i
		s.add(num)
		n+=1

print pentagonal()