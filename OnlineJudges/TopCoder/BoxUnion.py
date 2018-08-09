
class BoxUnion:
	def __init__(self, rect = ()):
		self.rect = rect

	def area(self,rect):
		rectangles = []
		for i in xrange(len(rect)): rectangles.append(map(int,rect[i].split()))
		rectangles.sort()
		A = rectangles[0]
		aA = aB = aC = intersecABC = intersecAB = intersecAC = intersecBC = 0

		aA = (A[2]-A[0]) * (A[3]-A[1])

		if len(rectangles)>1:
			B = rectangles[1]
			aB = (B[2]-B[0]) * (B[3]-B[1])

		if len(rectangles)>2:
			C = rectangles[2]
			aC = (C[2]-C[0]) * (C[3]-C[1])

		
		if len(rectangles)>1 and A[0] <= B[0] <= A[2]:
			intersecAB = (min(A[2],B[2]) - max(A[0],B[0])) * (min(A[3],B[3]) - max(A[1],B[1]))
			if intersecAB < 0: intersecAB = 0

		if len(rectangles)>2 and A[0] <= C[0] <= A[2]:
			intersecAC = (min(A[2],C[2]) - max(A[0],C[0])) * (min(A[3],C[3]) - max(A[1],C[1])) 
			if intersecAC < 0: intersecAC = 0

		if len(rectangles)>2 and B[0] <= C[0] <= B[2]:
			intersecBC = (min(C[2],B[2]) - max(C[0],B[0])) * (min(B[3],C[3]) - max(B[1],C[1])) 
			if intersecBC < 0: intersecBC = 0

		if len(rectangles)>2 and intersecAC and intersecAB:
			intersecABC = (min(A[2],B[2],C[2]) - max(A[0],B[0],C[0])) * (min(A[3],B[3],C[3]) - max(A[1],B[1],C[1]))
			if intersecABC < 0: intersecABC = 0
		
		return aA+aB+aC -(intersecAB+intersecAC+intersecBC) + intersecABC

def area(rectangles):
	for i in xrange(len(rectangles)): rectangles[i] = map(int,rectangles[i].split())
	rectangles.sort()
	A = rectangles[0]
	aA = aB = aC = intersecABC = intersecAB = intersecAC = intersecBC = 0

	aA = (A[2]-A[0]) * (A[3]-A[1])

	if len(rectangles)>1:
		B = rectangles[1]
		aB = (B[2]-B[0]) * (B[3]-B[1])

	if len(rectangles)>2:
		C = rectangles[2]
		aC = (C[2]-C[0]) * (C[3]-C[1])

	if len(rectangles)>1 and A[0] <= B[0] <= A[2]:
		intersecAB = (min(A[2],B[2]) - max(A[0],B[0])) * (min(A[3],B[3]) - max(A[1],B[1]))
		if intersecAB < 0: intersecAB = 0

	if len(rectangles)>2 and A[0] <= C[0] <= A[2]:
		intersecAC = (min(A[2],C[2]) - max(A[0],C[0])) * (min(A[3],C[3]) - max(A[1],C[1])) 
		if intersecAC < 0: intersecAC = 0

	if len(rectangles)>2 and B[0] <= C[0] <= B[2]:
		intersecBC = (min(C[2],B[2]) - max(C[0],B[0])) * (min(B[3],C[3]) - max(B[1],C[1])) 
		if intersecBC < 0: intersecBC = 0

	if len(rectangles)>2 and intersecAC and intersecAB:
		intersecABC = (min(A[2],B[2],C[2]) - max(A[0],B[0],C[0])) * (min(A[3],B[3],C[3]) - max(A[1],B[1],C[1]))
		if intersecABC < 0: intersecABC = 0

	return aA+aB+aC -(intersecAB+intersecAC+intersecBC) + intersecABC

print area(["1 0 3 2","1 1 3 2","2 0 4 2"])
