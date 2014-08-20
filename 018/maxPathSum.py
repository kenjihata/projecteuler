import sys

# these methods assume your triangle is properly formatted (n numbers per row)

def maxPathSum(triangle):
	for rowIndex in xrange(len(triangle)-2, -1, -1):
		for i in xrange(0, rowIndex+1):
			triangle[rowIndex][i] += max(triangle[rowIndex+1][i], triangle[rowIndex+1][i+1])
	return triangle[0][0]

def loadTriangle(filename):
	f = open(filename)
	triangle = []
	for line in f:
		triangle.append([int(i) for i in line.split()])
	return triangle

print(maxPathSum(loadTriangle('triangle.txt')))

