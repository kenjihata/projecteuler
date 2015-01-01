# x = 0.5(n)(n+1)
# 2x = n^2 + n 
# n^2 + n - 2x = 0
# n = (-1 +/- (1+8x)^.5)/2
def isTriangleNum(x):
	n = (-1 + (1+8*x)**.5)/2
	# (-1 - (1+8*x)**.5)/2 is negative, dont' need to process
	return n%1==0 

def sumChar(word):
	sum_char = 0
	for c in word:
		sum_char += ord(c)-ord('A')+1
	return sum_char

f = open('p042_words.txt')
num_words = 0
allWords = ''
for line in f:
	allWords += line
for word in allWords.replace('"', '').split(','):
	if isTriangleNum(sumChar(word)): num_words+=1
print num_words