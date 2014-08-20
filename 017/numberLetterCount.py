import sys

countMap = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 1000:'thousand'}

# returns the digit at a given place (e.g if you want tens digit, give digitPlace = 10)
def findDigitAt(num, digitPlace): 
	if digitPlace%10 != 0 and digitPlace != 1:
		print "not correct digitPlace format"
		return None
	return int(num/digitPlace) % 10

#
# argument must be at most 3 digits long
def findHundredsWord(num):
	if num < 0 or num > 999: return None
	if num <= 20:
		return countMap[num]
	elif num < 100: 
		tens = findDigitAt(num,10)*10
		onesDigit = findDigitAt(num,1)
		return countMap[tens] + countMap[onesDigit]
	else: 
		hundredsDigit = findDigitAt(num,100)
		tens = findDigitAt(num,10)*10
		onesDigit = findDigitAt(num,1)
		word = countMap[hundredsDigit] + countMap[100]
		if tens+onesDigit == 0:
			return word
		else: word += 'and'
		if tens+onesDigit <= 20:
			return word + countMap[onesDigit+tens]
		return word + countMap[tens] + countMap[onesDigit]
	
# counts the number of letters in a given number between 1-999999
def letterCount(num):
	if num < 1000:
		word = findHundredsWord(num)
		return len(word)
	else:
		return len(findHundredsWord(int(num/1000))+countMap[1000]+findHundredsWord(num%1000))
		
# counts the number of letters between a range, which must be a subset of 1-999999
def numberLetterCount(lowerBound, upperBound):
	if lowerBound < 0 or lowerBound > 999999 or upperBound < 0 or upperBound > 99999: return None
	count = 0
	for i in xrange(lowerBound, upperBound+1):
		count += letterCount(i)
	return count

print(numberLetterCount(int(sys.argv[1]), int(sys.argv[2])))
