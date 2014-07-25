import sys

# given input file, returns a list of the names in the file
# input file should be of this format:
# 1) A single line of names
# 2) Every name is "Name"
# 3) Each name is separated by a comma
# Example: "Bob","Kate","Stan"
def getNameList(filename):
	with open(filename, 'r') as f:
		first_line = f.readline()
		first_line = first_line.replace('\"', '')
		first_line = first_line.replace('\n', '')
		return first_line.split(',')
	return None

# returns the sum of the characters in the name
def nameSum(name):
	name = name.upper()
	nsum = 0
	for letter in name:
		nsum += ord(letter) - 64
	return nsum

# given a file, returns the name score
def totalNameScore(filename):
	namelist = getNameList(filename)
	namelist.sort()
	totalScore = 0
	for i in xrange(1,len(namelist)+1):
		totalScore += nameSum(namelist[i-1])*i
	return totalScore
	
print totalNameScore(sys.argv[1])
