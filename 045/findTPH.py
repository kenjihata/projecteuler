def findTriangle(index):
	return index * (index+1)/2

def findPentagonal(index):
	return index * (3*index - 1)/2

def findHexagonal(index):
	return index * (2*index-1)

indices = [286, 166, 144]
curr = [findTriangle(286), findPentagonal(166), findHexagonal(144)]

while True:
	if curr[0] > curr[1]:
		indices[1] += 1
		curr[1] = findPentagonal(indices[1])
	elif curr[1] > curr[0]:
		indices[0] += 1
		curr[0] = findTriangle(indices[0])
	else:
		if curr[0] > curr[2]:
			indices[2] += 1
			curr[2] = findHexagonal(indices[2])
		elif curr[2] > curr[0]:
			indices[0] += 1
			curr[0] = findTriangle(indices[0])
		else: 
			break
print curr[0]




