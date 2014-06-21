import sys

f = open(sys.argv[1])
lines = f.readlines()
f.close()
sum = 0
for i in lines:
	sum += int(i)
print sum

