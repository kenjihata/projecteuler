import sys

numDaysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# given an int array [mm, dd, yyyy],return days after 1/1/1990
# negative numbers means before 1/1/1990
def getDayNumber(dateOrMonth, day = 0, year=0):
	month = 0
	if isinstance(dateOrMonth, int):
		month = dateOrMonth
	else:
		month = dateOrMonth[0]
		day = dateOrMonth[1]
		year = dateOrMonth[2]
	dayNum = day
	if(year > 1900):
		for i in xrange(1900, year):
			if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0): dayNum += 366
			else: dayNum += 365
	else:
		for i in xrange(year, 1900):
			if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0): dayNum -= 366
			else: dayNum -=365
	for i in xrange(0, month-1):
		dayNum += numDaysPerMonth[i]
	if year % 4 == 0 and (month > 2 or (month == 2 and day == 29)):
		dayNum += 1
	return dayNum

# given a day number, determine if it is a Sunday
def isSunday(dayNum):
	return (dayNum + 1) % 7 == 0
	
# given month and day, gives you the next month (anything after
# 12/1 gives 13, which is the following year)
def startMonth(month, day):
	if day == 1: return month
	return month+1
	
# get a list of day numbers of the first of every month between 
# two days (represented as date arrays); assumes start < end
def getFirstSundays(start, end):
	firstSundays = []
	if start[2] == end[2]:
		for month in xrange(startMonth(start[0], start[1]), end[0]):
			dayNum = getDayNumber(month, 1, start[2])
			if isSunday(dayNum):
				firstSundays.append(dayNum)
	else:
		for month in xrange(startMonth(start[0], start[1]), 13):
			dayNum = getDayNumber(month, 1, start[2])
			if isSunday(dayNum):
				firstSundays.append(dayNum)
		for year in xrange(start[2]+1, end[2]):
			for month in xrange(1,13):
				dayNum = getDayNumber(month, 1, year)
				if isSunday(dayNum):
					firstSundays.append(dayNum)
		for month in xrange(1, end[0]+1):
			dayNum = getDayNumber(month, 1, end[2])
			if isSunday(dayNum):
				firstSundays.append(dayNum)
	return firstSundays
		
	

# using the start and end given as "mm/dd/yy", returns the number  
# of Sundays that fell on the first of the month between them
def countSundays(start, end):
	startArr = [int(i) for i in start.split('/')]
	endArr = [int(i) for i in end.split('/')]
	startNum = getDayNumber(startArr)
	endNum = getDayNumber(endArr)
	if startNum > endNum: return None
	firstSundays = getFirstSundays(startArr, endArr)
	return len(firstSundays)

print countSundays(sys.argv[1], sys.argv[2])
