# https://www.spoj.com/problems/AGGRCOW/

def agressive_cows(x):

	cowsplaced = 1
	previous = positions[0]

	for i in range(1,n):		
		if positions[i] - previous >= x:	
			cowsplaced += 1
			if cowsplaced == c:
				return True
			previous = positions[i]

	return False

t = int(input().strip())

for i in range(t):
	n, c = map(int,input().strip().split())
	positions = []

	for i in range(n):
		positions.append(int(input().strip()))

	positions.sort()

	left = 0
	right = positions[n-1] - positions[0] + 1

	while right - 1 > left:
		mid = (left + right) // 2
		if agressive_cows(mid):
			left = mid
		else:
			right = mid

	print(left)
