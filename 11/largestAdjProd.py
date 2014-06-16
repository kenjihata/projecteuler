import sys

def findLargestFourDiag(mat):
	largestProd = 0
	for i in xrange(0, len(mat)-4):
		for j in xrange(0, len(mat)-4):
			prod = mat[i][j]*mat[i+1][j+1]*mat[i+2][j+2]*mat[i+3][j+3]
			if prod > largestProd: largestProd = prod
	for i in xrange(0, len(mat)-4):
		for j in xrange(4, len(mat)):
			prod = mat[i][j]*mat[i+1][j-1]*mat[i+2][j-2]*mat[i+3][j-3]
			if prod > largestProd: largestProd = prod
	return largestProd

def findLargestFourVert(mat):
	largestProd = 0
	for i in xrange(0, len(mat)-4):
		for j in xrange(0, len(mat)):
			prod = mat[i][j]*mat[i+1][j]*mat[i+2][j]*mat[i+3][j]
			if prod > largestProd: largestProd = prod
	return largestProd

def findLargestFourHoriz(mat):
	largestProd = 0
	for i in xrange(0, len(mat)):
		for j in xrange(0, len(mat)-4):
			prod = mat[i][j]*mat[i][j+1]*mat[i][j+2]*mat[i][j+3]
			if prod > largestProd: largestProd = prod
	return largestProd

def findLargestFourAdjProd(mat):
	if len(mat) == 0:
		return None
	if len(mat) < 4 or len(mat[0]) < 4:
		return None
	return max(findLargestFourDiag(mat),max(findLargestFourVert(mat),findLargestFourHoriz(mat)))

f = open(sys.argv[1], 'r')
mat = [map(int,line.split()) for line in f]
print findLargestFourAdjProd(mat)

