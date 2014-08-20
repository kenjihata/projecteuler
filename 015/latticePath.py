import sys
import math

# counts the number of ways to go from upper left corner to bottom right corner on a grid
# Every route, you can go left gridWidth (w) times and down gridLength (l) times. Thus, using basic permutations, we see the number of unique paths is (w+l)!/(w!l!)
def latticePathCount(gridWidth, gridLength):
	if gridLength < 0 or gridWidth < 0: return None
	return math.factorial(gridLength+gridWidth) / (math.factorial(gridLength) * math.factorial(gridWidth))

print latticePathCount(int(sys.argv[1]),int(sys.argv[1]))
